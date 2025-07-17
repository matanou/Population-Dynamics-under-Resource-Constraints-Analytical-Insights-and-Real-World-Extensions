# Population Dynamics under Resource Constraints: Analytical Insights and Real World Extensions
In humanitarian crises such as natural disasters or conflicts, population survival often
 hinges on external aid delivery. The delivery of food, water, and medicine must match
 the consumption needs of the affected population. This project investigates how aid
 delivery timing and quantity affect long-term population sustainability using a logistic
 growth model constrained by dynamically changing resources.
 The project aims to answer the following question: Given a population that grows
 logistically with a carrying capacity dependent on food availability, how do the delivery
 frequency and quantity of food affect population survival over time

## Initial Model Setup (Continuous Replenishment)
Initially, consider continuous replenishment for analytical tractability. Let:
  
  • **P(t)**: Population at time t
   
  • **R(t)**: Available resources at time t
   
  • **r**: Intrinsic growth rate
   
  • **c**: Resource consumption per capita per day
   
  • **q**: Continuous replenishment rate
 
The model equations are:

<img width="355" height="272" alt="Capture" src="https://github.com/user-attachments/assets/4cf7a195-4b64-4f36-a754-fbdddc6be8d0" />

## Transition to Realistic Models (Discrete Replenishment)
Real-world scenarios usually involve discrete replenishments:

<img width="493" height="87" alt="image" src="https://github.com/user-attachments/assets/3751f03e-9f0d-4493-8d4a-96558cafdcf8" />

We can numerically simulate this using Euler method:

<img width="548" height="291" alt="image" src="https://github.com/user-attachments/assets/a2cd97aa-b94a-444e-bbd2-13b81c7e1d1b" />

## Extensions for Depth and Realism
### 1. Stochastic Delivery (Bernoulli)
We can consider delivery failures modeled by a Bernoulli random variable:

<img width="554" height="138" alt="image" src="https://github.com/user-attachments/assets/96d7e854-a22a-42df-89e5-025a2b26cb4d" />

And sse Monte Carlo simulations to study expected population survival.
 
### 2. Advanced Stochastic Delivery (Poisson Process)
Deliveries follow a Poisson process with rate λ. Inter-arrival times between deliveries are
exponentially distributed:
 
<img width="397" height="144" alt="image" src="https://github.com/user-attachments/assets/59c1ad8f-e0ed-4472-81fb-5f8510eb2c34" />

We can numerically simulate this process to analyze the variability in population outcomes.

### 3. Age-Structured Population Dynamics
Dividing the population into age groups with different consumption rates and growth rates (Py, Pa, Pe):

<img width="589" height="188" alt="image" src="https://github.com/user-attachments/assets/c16f5f43-9cae-4309-ab80-bf6be68365e6" />
 
Investigate resource allocation strategies prioritizing specific age groups.
