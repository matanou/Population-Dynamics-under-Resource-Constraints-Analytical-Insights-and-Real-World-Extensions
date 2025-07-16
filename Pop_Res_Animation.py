import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters (using years as time units)
init_pop = 100  # fixed as 100%, population values shown as percentages
init_res = 11
init_growth = 0.01
init_consumption = 0.2422
init_replenishment = 0.989

dt = 0.001  # time step in years

current_pop = init_pop
current_resource = init_res

time_vals = [0]
pop_vals = [100.0]  # population as a percentage
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
fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Population (%)', color='tab:blue')
line2, = ax.plot([], [], label='Resource', color='tab:green')
ax.set_xlim(0, 10)
ax.set_ylim(0, max(init_res, init_pop) * 1.1)
ax.set_xlabel("Time (years)")
ax.set_ylabel("Population (%) / Resource")
ax.set_title("Real-Time Population and Resource Dynamics")
ax.legend()

# Update function
def update(frame):
    for _ in range(int(1 / dt)):  # simulate 1 year worth of steps
        step()

    time_vals.append(time_vals[-1] + 1)
    pop_vals.append(current_pop)  # still in percentage (100 = 100%)
    res_vals.append(current_resource)

    line1.set_data(time_vals, pop_vals)
    line2.set_data(time_vals, res_vals)

    ax.set_xlim(0, time_vals[-1] + 5)
    max_y = max(max(pop_vals), max(res_vals)) * 1.1
    ax.set_ylim(0, max_y)

    return line1, line2

ani = animation.FuncAnimation(fig, update, interval=10)
plt.show()
