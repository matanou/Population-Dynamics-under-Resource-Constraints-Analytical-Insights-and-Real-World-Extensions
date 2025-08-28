# Population Dynamics under Resource Constraints: Analytical Insights and Real World Extensions

In humanitarian crises such as natural disasters or conflicts, population survival often hinges on external aid delivery. The delivery of food, water, and medicine must match the consumption needs of the affected population.  

This project investigates how aid delivery timing and quantity affect long-term population sustainability using a logistic growth model constrained by dynamically changing resources.

**Research Question:**  
*How do delivery frequency and quantity of resources affect long-term population sustainability in a logistic growth system constrained by resources?*

---

## Initial Model Setup (Continuous Replenishment)

For analytical tractability, we begin with **continuous replenishment**.

- **\(P(t)\):** Population at time \(t\)  
- **\(R(t)\):** Available resources at time \(t\)  
- **\(r\):** Intrinsic growth rate  
- **\(c\):** Resource consumption per capita  
- **\(q\):** Continuous replenishment rate  

The coupled system is:

$
\frac{dP}{dt} = rP\left(1 - \frac{cP}{R}\right),
$
$
\frac{dR}{dt} = q - kP.
$

Equilibrium analysis gives:

$
P^* = \frac{q}{c}, \quad R^* = q.
$

Stability is assessed by computing the Jacobian at equilibrium and checking eigenvalues.

---

## Transition to Realistic Models (Discrete Replenishment)

In practice, resources arrive at **discrete time intervals** rather than continuously.  

Between deliveries, the system evolves as:

$
\frac{dP}{dt} = rP\left(1 - \frac{cP}{R}\right), \quad \frac{dR}{dt} = -kP.
$

At delivery times \(t = n\tau\) (with \(n \in \mathbb{N}\)):

$
R(t^+) = R(t^-) + Q, \quad P(t^+) = P(t^-).
$

This defines an **impulsive differential system**, which we simulate numerically (Euler method) to explore how \(Q\) (delivery size) and \(\tau\) (frequency) affect sustainability.

---

## Possible Extensions for Depth and Realism

### 1. Stochastic Delivery (Bernoulli Model)

Aid delivery is not always successful. Model each delivery with a Bernoulli random variable:

$
Q_n =
\begin{cases}
Q & \text{with probability } p, \\
0 & \text{with probability } 1-p.
\end{cases}
$

This is simulated over many runs. **Monte Carlo methods** are used to compute expected survival and variance, invoking the Law of Large Numbers.

---

### 2. Advanced Stochastic Delivery (Poisson Process)

Deliveries may follow a **Poisson process** with rate \(\lambda\). Inter-arrival times are exponentially distributed:

$
\Delta t \sim \text{Exponential}(\lambda).
$

This produces irregular replenishment schedules, allowing analysis of variability in population outcomes.

---

### 3. Age-Structured Population Dynamics

We can split the population into age groups with different consumption and growth rates:

- $P_y(t)$: Youth  
- $P_a(t)$: Adults  
- $P_e(t)$: Elderly  

Each subpopulation satisfies a variant of the logistic-resource model, with group-specific parameters $(r_i, c_i, k_i)$.  

This extension allows investigation of **resource allocation strategies** (e.g. prioritising food for children or adults to maximise long-term survival).

---

## Summary

- **Continuous model:** Analytical insight and equilibrium analysis.  
- **Discrete model:** More realistic impulsive dynamics.  
- **Stochastic models:** Capture uncertainty via Bernoulli and Poisson deliveries.  
- **Extensions:** Age-structured populations for richer humanitarian applications.  
