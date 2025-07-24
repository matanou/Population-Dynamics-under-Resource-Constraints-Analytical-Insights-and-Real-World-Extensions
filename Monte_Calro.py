import numpy as np
import matplotlib.pyplot as plt

# Simulation Settings
dt = 0.001  # time step in years (~8.76 hours)
simulation_years = 1
steps_total = int(simulation_years / dt)
weeks_total = int(simulation_years * 52)

# Model Parameters
initial_pop = 100
R0 = 20
k = 3

def simulate_one_run(res_init, growth_rate, consumption, Q, tau_weeks, prob_replenish):
    P = initial_pop
    R = res_init
    steps_per_tau = int((tau_weeks / 52) / dt)

    for step in range(1, steps_total + 1):
        dP = growth_rate * P * (1 - P / (k * R))
        dR = -consumption * P * (R / (R + R0))

        P += dP * dt
        R += dR * dt

        # Discrete stochastic replenishment
        if step % steps_per_tau == 0:
            if np.random.rand() < prob_replenish:
                R += Q

    return P

runs = 1000

def monte_carlo_average_population(
    runs=1000,
    res_init=20,
    growth_rate=0.03,
    consumption=0.1,               # These hyperparam are arbitrary but based on realistic datas and papers
    Q=1.0,
    tau_weeks=1,
    prob_replenish=0.4
):
    final_populations = []

    for i in range(runs):
        np.random.seed(i)  # Different seed per run
        final_P = simulate_one_run(res_init, growth_rate, consumption, Q, tau_weeks, prob_replenish)
        final_populations.append(final_P)

    avg_final_population = np.mean(final_populations)
    return avg_final_population, final_populations

# --- Run the Monte Carlo Simulation ---
avg_pop, all_pops = monte_carlo_average_population()

# --- Plot the Distribution ---
plt.hist(all_pops, bins=40, color='skyblue', edgecolor='black')
plt.axvline(avg_pop, color='red', linestyle='dashed', linewidth=2, label=f'Avg Final Pop = {avg_pop:.2f}')
plt.title(f"Distribution of Final Population ({runs} Stochastic Runs)")
plt.xlabel("Final Population")
plt.ylabel("Frequency")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
