### 1.Computation of the Fundamental Matrix

#### 1.1 The 8-Point Algorithm

* The relationship for any pair of corresponding points `x` and `x'` is given by the epipolar constraint: `x'ᵀFx = 0`.
* This equation can be expanded into a linear equation with the 9 elements of F as unknowns.
* Each pair of matching points provides one such linear equation. To solve for the 8 degrees of freedom of F (9 elements minus one for scale), at least 8 point-pairs are needed.
* These equations can be stacked into a matrix form `Aψ = 0`, where `ψ` is a 9x1 vector of the flattened F matrix elements, and `A` is constructed from the coordinates of the matching points.
* The solution for `ψ` is found using Singular Value Decomposition (SVD). Specifically, it is the singular vector corresponding to the smallest singular value of A (the last column of V in the decomposition `A = UDVᵀ`).

#### 1.2 Practical Issues and Solutions

**Problem 1: Numerical Instability.** The columns of matrix A can have vastly different numerical scales, which leads to poor and unstable results from least-squares methods.

**Solution: Normalization.** Before constructing the A matrix, the coordinates of the points are normalized, for example, by mapping them to the range [-1, 1]. This significantly improves the numerical stability of the calculation

**Problem 2: Rank Constraint.** The F matrix calculated via the least-squares approach may not satisfy the geometric constraint that its rank must be 2 (i.e., `det(F) = 0`).

**Solution: Enforce Constraint via SVD.** To fix this, perform SVD on the calculated F (`F = USVᵀ`), set the smallest singular value in S to zero, and then recompute F. The result is the closest possible rank-2 matrix to the original solution

### 2.Stereo Constraints and Priors

>Even with epipolar geometry, feature matching can still be error-prone, especially in areas with little texture or with repetitive structures. Additional constraints can help

**Uniqueness Constraint**

>For any point in one image, there should be at most one matching point in the other image.

**Smoothness Constraint**

>Disparity values, which relate to depth, tend to change slowly and smoothly across most parts of an image

**Ordering Constraint**

>If a point A is to the left of a point B in the left image, their corresponding points A' and B' should appear in the same left-to-right order in the right image (unless an occlusion occurs)


### 3.Stereo Image Rectification

#### 3.1 The Goal

* Searching for matching points along obliquely oriented epipolar lines is computationally complex and can be inaccurate
* Stereo image rectification is a process that re-projects the two images onto a new common plane that is parallel to the camera baseline (the line connecting the camera centers)
* After rectification, all epipolar lines become horizontal lines that share the same vertical coordinate
* This simplifies the correspondence search from a 2D problem to a much simpler and faster 1D search along the same horizontal scanline

#### 3.2 The Mechanism

* The process is effectively a "virtual rotation" of each camera so that their image planes become parallel.
* When a camera only rotates, the mapping between the original and new image is a 3x3 Homography matrix (H). Rectification is achieved by applying a specific homography transformation (image warping) to each image.


### 4.Depth Calculation

* Once corresponding points `x` and `x'` are found on the rectified images, the **disparity** (horizontal difference) is computed.
* The depth `d` (or distance) to the 3D point can then be calculated using the disparity, the camera baseline `t`, and the focal length `f`

$$d=(t * f) / disparity$$
* With the depth (Z) known, the full 3D world coordinates (X, Y) can be recovered using the camera's intrinsic parameters and the point's 2D image coordinates