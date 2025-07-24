import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# Simulation settings
dt = 0.001  # Each step ~8.76 hours
simulation_years = 1
steps_total = int(simulation_years / dt)
weeks_total = int(simulation_years * 52)

# Discrete replenishment version of the new model
def simulate(res_init, growth_rate, consumption, Q, tau_weeks):
    P = 100  # initial population
    R = res_init
    P_vals = []
    R_vals = []

    steps_per_week = int((1 / 52) / dt)
    steps_per_tau = int((tau_weeks / 52) / dt)

    R0 = 20
    k = 3

    P_vals.append(P)
    R_vals.append(R)

    for step in range(1, steps_total + 1):
        dP = growth_rate * P * (1 + P / (k * R))
        dR = -consumption * P * (R / (R + R0))

        P += dP * dt
        R += dR * dt

        if step % steps_per_tau == 0:
            R += Q  # Discrete jump in resource

        if step % steps_per_week == 0:
            P_vals.append(P)
            R_vals.append(R)

    time_vals = np.arange(len(P_vals))
    return P_vals, R_vals, time_vals

# Initial params
init_res = 40
init_growth = 0.02
init_consumption = 0.25
init_replenish_amt = 1.0
init_tau_weeks = 2

# Precompute
pop_vals, res_vals, time_vals = simulate(init_res, init_growth, init_consumption, init_replenish_amt, init_tau_weeks)

# Plot Setup
fig, ax = plt.subplots(figsize=(13, 10))
plt.subplots_adjust(left=0.1, bottom=0.5)

line_pop, = ax.plot(time_vals, pop_vals, label='Population', color='tab:blue')
line_res, = ax.plot(time_vals, res_vals, label='Resource', color='tab:green')

ax.set_xlabel("Time (weeks)")
ax.set_ylabel("Population / Resource")
ax.set_title("Population Dynamics with Discrete Replenishment (Updated Model)")
ax.legend()
ax.grid(True)
ax.set_xlim(0, weeks_total)
ax.set_ylim(0, max(max(pop_vals), max(res_vals)) * 1.1)

# Sliders
slider_res = Slider(plt.axes([0.15, 0.41, 0.7, 0.03]), "Initial Resource", 1, 100, valinit=init_res, valstep=1)
slider_growth = Slider(plt.axes([0.15, 0.36, 0.7, 0.03]), "Growth Rate (r)", 0.001, 0.2, valinit=init_growth)
slider_consumption = Slider(plt.axes([0.15, 0.31, 0.7, 0.03]), "Consumption Rate (c)", 0.01, 1.0, valinit=init_consumption)
slider_replenish = Slider(plt.axes([0.15, 0.26, 0.7, 0.03]), "Replenish Amount (Q)", 0.01, 3.0, valinit=init_replenish_amt)
slider_tau = Slider(plt.axes([0.15, 0.21, 0.7, 0.03]), "Replenish Every (weeks)", 1, 52, valinit=init_tau_weeks, valstep=1)
slider_time = Slider(plt.axes([0.15, 0.16, 0.7, 0.03]), "Week", 0, weeks_total, valinit=weeks_total, valstep=1)

text_pop = fig.text(0.15, 0.12, f"Population at week={weeks_total} = {pop_vals[-1]:.2f}", fontsize=11, color='tab:blue')
text_res = fig.text(0.15, 0.08, f"Resource at week={weeks_total} = {res_vals[-1]:.2f}", fontsize=11, color='tab:green')

def update_model(val):
    new_res = slider_res.val
    new_growth = slider_growth.val
    new_cons = slider_consumption.val
    new_Q = slider_replenish.val
    new_tau = slider_tau.val

    global pop_vals, res_vals, time_vals
    pop_vals, res_vals, time_vals = simulate(new_res, new_growth, new_cons, new_Q, new_tau)

    line_pop.set_data(time_vals, pop_vals)
    line_res.set_data(time_vals, res_vals)
    ax.set_xlim(0, len(time_vals) - 1)
    ax.set_ylim(0, max(max(pop_vals), max(res_vals)) * 1.1)

    slider_time.valmax = len(time_vals) - 1
    slider_time.ax.set_xlim(slider_time.valmin, slider_time.valmax)
    slider_time.set_val(min(slider_time.val, slider_time.valmax))

    update_time(slider_time.val)
    fig.canvas.draw_idle()

def update_time(t_val):
    t_index = int(t_val)
    if t_index < len(pop_vals):
        text_pop.set_text(f"Population at week={t_index} = {pop_vals[t_index]:.2f}")
        text_res.set_text(f"Resource at week={t_index} = {res_vals[t_index]:.2f}")
    fig.canvas.draw_idle()

for s in [slider_res, slider_growth, slider_consumption, slider_replenish, slider_tau]:
    s.on_changed(update_model)

slider_time.on_changed(update_time)

plt.show()
