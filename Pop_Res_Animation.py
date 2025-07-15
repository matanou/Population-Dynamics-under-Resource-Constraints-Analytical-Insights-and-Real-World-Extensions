import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
growth_rate = 0.2
resource_consumption_pc_pd = 0.5
replenishment_rate = 0.5
initial_pop = 10
initial_resource = 10

dt = 0.01

current_pop = initial_pop
current_resource = initial_resource

time_vals = [0]
pop_vals = [current_pop]
res_vals = [current_resource]

def rate_pop_time(pop, res):
    return growth_rate * pop * (1 - (resource_consumption_pc_pd * pop / res))

def rate_res_time(pop):
    return replenishment_rate - resource_consumption_pc_pd * pop

def step():
    global current_pop, current_resource

    dP_dt = rate_pop_time(current_pop, current_resource)
    dR_dt = rate_res_time(current_pop)

    current_pop += dP_dt * dt
    current_resource += dR_dt * dt

# set up the plot
fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Population (P)')
line2, = ax.plot([], [], label='Resource (R)')
ax.set_xlim(0, 100)
ax.set_ylim(0, max(initial_resource, initial_pop) * 1.1)
ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Value")
ax.legend()


def update(frame):
    if (current_pop < 1) or (current_resource < 1):
        return  # terminate the program if the population reaches 0

    for _ in range(int(1 / dt)):  # simulate 1 second worth of steps
        step()

    time_vals.append(time_vals[-1] + 1)
    pop_vals.append(current_pop)
    res_vals.append(current_resource)

    line1.set_data(time_vals, pop_vals)
    line2.set_data(time_vals, res_vals)

    ax.set_xlim(0, time_vals[-1] + 10)
    max_y = max(max(pop_vals), max(res_vals)) * 1.1
    ax.set_ylim(0, max_y)

    return line1, line2

ani = animation.FuncAnimation(fig, update, interval=1000)
plt.show()
