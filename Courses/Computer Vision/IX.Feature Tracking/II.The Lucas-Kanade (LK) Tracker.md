>The LK method solves the optical flow problem by using the **spatial coherence** assumption. It assumes that all pixels within a small NxN window have the same displacement (u,v)

* **Method**: This creates an over-determined system of equations (one for each pixel in the window), which can be solved using the **Least Squares** method
* **The LK Equation**: The optimal solution for the displacement $d=[u,v]^{T}$ is found by solving

$$(A^{T}A)d=A^{T}B$$

* Where the matrix ATA is a 2x2 matrix composed of sums of the products of image gradients within the window
* **Conditions for Solvability**: For the system to have a reliable solution, the matrix ATA must be

1. Invertible
2. Well-conditioned
3. Its eigenvalues must be sufficiently large to overcome noise, often checked with a threshold: $min(\lambda_1,\lambda_2)\gt threshold$

* **Multiscale Implementation**: The standard LK tracker only works for small motions. To handle larger displacement, a multi-resolution image pyramid is used. The tracker starts at the coarsest (lowest resolution) level to get a rough motion estimate and refines it progressively at higher-resolution levels

