### 1.Problem

>The optimization process for a neural network is not guaranteed to find the "global minimum" of the error function and may get stuck in a "local minimum".

### 2.Strategies to "Escape" Local Minima

* **Multiple Initializations**: Initialize multiple networks with different random parameters, train them, and select the solution with the lowest error.
* **Simulated Annealing**: At each step, accept a worse solution with a certain probability, with this probability decreasing over time
* **Stochastic Gradient Descent**: By adding random factors into the gradient calculation, it's possible that even when trapped in a local minimum, the calculated gradient may not be zero, giving it a chance to continue searching.