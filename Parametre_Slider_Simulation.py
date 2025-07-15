import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# Simulation settings
dt = 0.01
simulation_time = 1000
time_vals = np.arange(0, simulation_time + 1)  # Only every full second


def rate_pop_time(pop, res, growth_rate, consumption):
    return growth_rate * pop * (1 - (consumption * pop / res))

def rate_res_time(pop, consumption, replenish):
    return replenish - consumption * pop

def simulate(pop_init, res_init, growth_rate, consumption, replenish):
    current_pop = pop_init
    current_res = res_init
    pop_vals = [current_pop]
    res_vals = [current_res]

    for step_num in range(1, int(simulation_time / dt) + 1):
        dP_dt = rate_pop_time(current_pop, current_res, growth_rate, consumption)
        dR_dt = rate_res_time(current_pop, consumption, replenish)

        current_pop += dP_dt * dt
        current_res += dR_dt * dt

        if step_num % int(1 / dt) == 0:
            pop_vals.append(current_pop)
            res_vals.append(current_res)

    return pop_vals, res_vals

# Initial values
init_pop = 50
init_res = 10
init_growth = 0.2
init_consumption = 0.2
init_replenishment = 1

# Precompute
pop_vals, res_vals = simulate(init_pop, init_res, init_growth, init_consumption, init_replenishment)

# Plot setup
fig, ax = plt.subplots(figsize=(12, 10))
plt.subplots_adjust(left=0.1, bottom=0.55)

line_pop, = ax.plot(time_vals, pop_vals, label='Population (P)', color='tab:blue')
line_res, = ax.plot(time_vals, res_vals, label='Resource (R)', color='tab:green')

ax.set_xlabel("Time (seconds)")
ax.set_ylabel("Value")
ax.set_title("Population and Resource Dynamics")
ax.legend()
ax.grid(True)
ax.set_ylim(0, max(max(pop_vals), max(res_vals)) * 1.1)


slider_pop = Slider(plt.axes([0.15, 0.47, 0.7, 0.03]), "Initial Population", 1, 100, valinit=init_pop, valstep=1)
slider_res = Slider(plt.axes([0.15, 0.42, 0.7, 0.03]), "Initial Resource", 1, 100, valinit=init_res, valstep=1)
slider_growth = Slider(plt.axes([0.15, 0.37, 0.7, 0.03]), "Growth Rate", 0.01, 1.0, valinit=init_growth)
slider_consumption = Slider(plt.axes([0.15, 0.32, 0.7, 0.03]), "Consumption Rate", 0.01, 1.0, valinit=init_consumption)
slider_replenishment = Slider(plt.axes([0.15, 0.27, 0.7, 0.03]), "Replenishment Rate", 0.01, 3.0, valinit=init_replenishment)
slider_time = Slider(plt.axes([0.15, 0.21, 0.7, 0.03]), "Time", 0, simulation_time, valinit=simulation_time, valstep=1)


text_pop = fig.text(0.15, 0.14, f"Last population value = {pop_vals[-1]:.2f}", fontsize=11, color='tab:blue')
text_res = fig.text(0.15, 0.10, f"Last resource value = {res_vals[-1]:.2f}", fontsize=11, color='tab:green')


def update_model(val):
    new_pop = slider_pop.val
    new_res = slider_res.val
    new_growth = slider_growth.val
    new_cons = slider_consumption.val
    new_repl = slider_replenishment.val

    global pop_vals, res_vals
    pop_vals, res_vals = simulate(new_pop, new_res, new_growth, new_cons, new_repl)

    line_pop.set_ydata(pop_vals)
    line_res.set_ydata(res_vals)
    ax.set_ylim(0, max(max(pop_vals), max(res_vals)) * 1.1)

    update_time(slider_time.val)
    fig.canvas.draw_idle()


def update_time(t_val):
    t_index = int(t_val)
    if t_index < len(pop_vals):
        text_pop.set_text(f"Population at t={t_index}s = {pop_vals[t_index]:.2f}")
        text_res.set_text(f"Resource at t={t_index}s = {res_vals[t_index]:.2f}")
    fig.canvas.draw_idle()


for s in [slider_pop, slider_res, slider_growth, slider_consumption, slider_replenishment]:
    s.on_changed(update_model)

slider_time.on_changed(update_time)

plt.show()
