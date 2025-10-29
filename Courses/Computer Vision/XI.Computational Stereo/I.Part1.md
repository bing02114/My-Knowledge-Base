### 1.Introduction to Stereo Vision

**Goal**:

>To recover 3D information from two or more 2D images taken from different viewpoints. This is analogous to how human eyes perceive depth

**The Correspondence Problem**

>The fundamental challenge in stereo vision is the "correspondence problem

* Given a feature point `x` in the first image, how do we find the corresponding feature point `x'` in the second image
* The search space could potentially be the entire second image, which is inefficient and prone to errors


### 2.Epipolar Geometry

>Epipolar geometry is the intrinsic projective geometry between two views that provides a powerful constraint to solve the correspondence problem. It reduces the 2D search for a point to a 1D search along a line.

#### 2.1 Key Components

* **Camera Centers**: The optical centers of the two cameras
* **Baseline**: The line connecting the two camera centers
* **Epipoles**: The projection of one camera's center onto the other camera's image plane.
* **Epipolar Plance**: Any plane that contains the baseline. A 3D point X and the two camera centers C and C' define a unique epipolar plane
* **Epipolar Line**: The intersection of an epipolar plane with an image plane. All points on an epipolar line in one image correspond to points on the matching epipolar line in the other image

#### 2.2 The Epipolar Constraint

>For any point `x` in the first image, its corresponding point `x'` in the second image **must lie on the epipolar line** `l'` defined by `x`


### 3.The Fundamental Matrix (F)

* The Fundamental Matrix `F` is the **algebraic representation** of the epipolar geometry. It is a 3x3 matrix that mathematically connects corresponding points between two images

#### 3.1 Defining Equation

$$x'^{T}Fx=0$$

>The equation means that the point x' lies on the epipolar line l'=Fx

**Properties**

* `F` is a 3x3 matrix with **7 degrees of freedom**
* It is a rank-deficient
* It encapsulates both the intrinsic and extrinsic parameters of the stereo camera setup

$$F=[K't]_{\times}K'RK^{-1}$$

* The epipoles e and e' are the null spaces of F and FT, respectively Fe=0 and FTe'=0

### 4.The Essential Matrix (E)

>The Essential Matrix E is a specialized version of the Fundamental Matrix that applies only to calibrated cameras

#### 4.1 Context: 