import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Parameters (time in years)
init_pop = 100
init_res = 11
init_growth = 0.01
init_consumption = 0.2422
init_replenishment = 0.989

simulation_time = 1  # 1 year
dt = 0.001
days_total = 365  # simulate 365 days
days_per_frame = 1  # simulate one day per animation frame

day_length_years = 1 / 365
steps_per_day = int(day_length_years / dt)

# Initialize state
current_pop = init_pop
current_resource = init_res
time_vals = [0]  # in weeks
pop_vals = [current_pop]
res_vals = [current_resource]

def rate_pop_time(pop, res):
    return init_growth * pop * (1 - (init_consumption * pop / res))

def rate_res_time(pop):
    return init_replenishment - init_consumption * pop

def step():
    global current_pop, current_resource
    dP_dt = rate_pop_time(current_pop, current_resource)
    dR_dt = rate_res_time(current_pop)
    current_pop += dP_dt * dt
    current_resource += dR_dt * dt

# Set up the plot
fig, ax = plt.subplots(figsize=(16, 6)) 
line1, = ax.plot([], [], label='Population (%)', color='tab:blue')
line2, = ax.plot([], [], label='Resource', color='tab:green')

ax.set_xlim(0, 52)
ax.set_ylim(0, max(init_res, init_pop) * 1.1)

ax.set_xlabel("Time (weeks)")
ax.set_ylabel("Population (%) / Resource")
ax.set_title("Population Dynamics with Continuous Replenishment (1 Year)")
ax.legend()

# Set ticks every week
ax.set_xticks(np.arange(0, 53, 1))
ax.grid(True, which='both', linestyle='--', linewidth=0.5)


def update(frame):
    for _ in range(steps_per_day):
        step()

    time_vals.append(time_vals[-1] + 1/7)  # 1 day = 1/7 week
    pop_vals.append(current_pop)
    res_vals.append(current_resource)

    line1.set_data(time_vals, pop_vals)
    line2.set_data(time_vals, res_vals)

    ax.set_xlim(0, max(52, time_vals[-1] + 1))
    ax.set_ylim(0, max(max(pop_vals), max(res_vals)) * 1.1)

    return line1, line2

ani = animation.FuncAnimation(fig, update, frames=days_total, interval=100, repeat=False)
plt.show()
