import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# Simulation settings
dt = 0.001  # Each time step is ~8.76 hours
simulation_time = 100  # Simulate for 100 years
time_vals = np.arange(0, simulation_time + 1)  # Only sample each year

# Simulation functions
def rate_pop_time(pop, res, growth_rate, consumption):
    return growth_rate * pop * (1 - (consumption * pop / res))

def rate_res_time(pop, consumption, replenish):
    return replenish - consumption * pop

def simulate(res_init, growth_rate, consumption, replenish):
    initial_pop = 100
    current_pop = initial_pop
    current_res = res_init
    pop_vals = [100.0]  # Percentage
    res_vals = [current_res]

    for step_num in range(1, int(simulation_time / dt) + 1):
        dP_dt = rate_pop_time(current_pop, current_res, growth_rate, consumption)
        dR_dt = rate_res_time(current_pop, consumption, replenish)

        current_pop += dP_dt * dt
        current_res += dR_dt * dt

        if step_num % int(1 / dt) == 0:
            pop_vals.append(current_pop / initial_pop * 100)  # as percentage
            res_vals.append(current_res)

    return pop_vals, res_vals

# Initial values
init_res = 11
init_growth = 0.01
init_consumption = 0.2422
init_replenishment = 0.989

# Precompute
pop_vals, res_vals = simulate(init_res, init_growth, init_consumption, init_replenishment)

# Plot setup
fig, ax = plt.subplots(figsize=(12, 10))
plt.subplots_adjust(left=0.1, bottom=0.45)

line_pop, = ax.plot(time_vals, pop_vals, label='Population (%)', color='tab:blue')
line_res, = ax.plot(time_vals, res_vals, label='Resource', color='tab:green')

ax.set_xlabel("Time (years)")
ax.set_ylabel("Population (%) / Resource Value")
ax.set_title("Population Dynamics Under Resource Limitation")
ax.legend()
ax.grid(True)
ax.set_ylim(0, max(max(pop_vals), max(res_vals)) * 1.1)

# Sliders
slider_res = Slider(plt.axes([0.15, 0.36, 0.7, 0.03]), "Initial Resource", 1, 100, valinit=init_res, valstep=1)
slider_growth = Slider(plt.axes([0.15, 0.31, 0.7, 0.03]), "Growth Rate", 0.001, 0.2, valinit=init_growth)
slider_consumption = Slider(plt.axes([0.15, 0.26, 0.7, 0.03]), "Consumption Rate", 0.01, 1.0, valinit=init_consumption)
slider_replenishment = Slider(plt.axes([0.15, 0.21, 0.7, 0.03]), "Replenishment Rate", 0.01, 3.0, valinit=init_replenishment)

slider_time = Slider(plt.axes([0.15, 0.16, 0.7, 0.03]), "Time", 0, simulation_time, valinit=simulation_time, valstep=1)

# Text outputs
text_pop = fig.text(0.15, 0.12, f"Population at t={simulation_time}s = {pop_vals[-1]:.2f}%", fontsize=11, color='tab:blue')
text_res = fig.text(0.15, 0.08, f"Resource at t={simulation_time}s = {res_vals[-1]:.2f}", fontsize=11, color='tab:green')

# Core update when sliders change
def update_model(val):
    new_res = slider_res.val
    new_growth = slider_growth.val
    new_cons = slider_consumption.val
    new_repl = slider_replenishment.val

    global pop_vals, res_vals
    pop_vals, res_vals = simulate(new_res, new_growth, new_cons, new_repl)

    line_pop.set_ydata(pop_vals)
    line_res.set_ydata(res_vals)
    ax.set_ylim(0, max(max(pop_vals), max(res_vals)) * 1.1)

    update_time(slider_time.val)
    fig.canvas.draw_idle()

# Time-dependent text update
def update_time(t_val):
    t_index = int(t_val)
    if t_index < len(pop_vals):
        text_pop.set_text(f"Population at t={t_index} years = {pop_vals[t_index]:.2f}%")
        text_res.set_text(f"Resource at t={t_index} years = {res_vals[t_index]:.2f}")
    fig.canvas.draw_idle()

# Connect everything
for s in [slider_res, slider_growth, slider_consumption, slider_replenishment]:
    s.on_changed(update_model)

slider_time.on_changed(update_time)

plt.show()
