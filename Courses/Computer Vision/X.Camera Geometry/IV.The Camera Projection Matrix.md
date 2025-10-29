>The complete process of mapping a 3D world point to 2D pixel coordinates is encapsulated in a single 3x4 matrix **P**, called the Camera Projection Matrix. It is a combination of extrinsic and intrinsic parameters

### 1.From World Coordinates to Camera Coordinates (Extrinsic Parameters)

* This step describes the camera's position and orientation in the world. It involves a transformation from the world coordinate frame to the camera's coordinate frame.
* It is defined by a **Rotation matrix R** (3x3) and a **Translation vector t** (3x1). In homogeneous coordinates, this is a 4x4 matrix

$$\left[ \begin{matrix}
R & t \\
0 & 1
\end{matrix}\right]$$


### 2.From Camera Coordinates to Pixel Coordinates (Intrinsic Parameters)

* This step describes the internal properties of the camera itself
* These parameters are represented by the **Calibration Matrix K** (a 3x3 upper triangular matrix)

$$\left( \begin{matrix}
\alpha_x & s & x_0 \\
0 & \alpha_y & y_0 \\
0 & 0 & 1
\end{matrix}\right)$$

* αx​,αy​: Focal lengths in terms of pixel dimensions (αx​=f⋅kx​).
* (x0​,y0​): The coordinates of the **Principal Point** (where the optical axis intersects the image plane)
* s: A skew parameter, which is often 0 for modern cameras.

### 3.The Full Equation

>The projection of a 3D world point Xworld​=(X,Y,Z,1)T to a 2D image point xpix​=(u,v,w)T is given by

$$\left( \begin{matrix}
u\\ v\\ w
\end{matrix}\right)=P\left( \begin{matrix}
X\\ Y\\ Z\\ 1
\end{matrix}\right)=k[R|t]\left( \begin{matrix}
X \\ Y \\ Z \\ 1
\end{matrix}\right)$$

* The full projection matrix P has **11 degrees of freedom** (5 from K, 3 from R, 3 from t).