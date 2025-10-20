>To make detectors scale-invariant, we need a way to automatically find the "characteristic scale" of a feature


### 1.Laplacian of Gaussian

> The LoG function is well-suited for finding the characteristic scale of blobs and corners. A feature's scale is identified where the LoG response reaches an extremum.

$$LoG(x,y,\sigma)=\nabla^{2}G(x,y,\sigma)=I_{xx}(x,y,\sigma)+I_{yy}(x,y,\sigma)$$

***
### 2.Difference of Gaussian

>DoG is highly efficient approximation of the LoG. It is calculated by subtracting two Gaussian-blurred versions of an image

$$DoG(x,y,\sigma)=I * G(K\sigma)-I*G(\sigma)$$

***
### 3.Scale-Invariant Feature Transform (SIFT)

>SIFT is a popular algorithm that uses the DoG for scale-invariant interest point detection

#### 3.1 Scale-Space Extrema Detection

>Construct a DoG pyramid by blurring and downsampling the image across different "octaves". Find candidate keypoints by comparing each pixel to its 26 neighbors in 3D (spatial and scale) space

**Goal**

>To find points in the image that are potential features and are stable across different levels of zoom (scales). An ideal feature should be detectable whether you are looking at it from far away (blurry, low scale) or up close (sharp, high scale).

**Constructing the Scale-Space**

>**Gaussian Blurring**: The fundamental operation is convolution with a Gaussian kernel. The image is repeatedly blurred with a Gaussian filter of increasing standard deviation, σ. A small σ corresponds to a fine scale (sharp details), while a large σ corresponds to a coarse scale (only large structures are visible)
>
>**Octaves and Intervals**: To make this process efficient, SIFT organizes the scale space into **octaves**.
>- An **Octave** is a set of blurred images at one resolution.
>- Within an octave, the value of σ is progressively doubled (e.g., σ,kσ,k2σ,k3σ,…). The individual blurred images are called **intervals** or layers.
>- To start a new octave, the image from the previous octave is down-sampled by a factor of 2 (its width and height are halved), and the blurring process is repeated. This pyramid structure allows the algorithm to find features of all sizes without having to use enormous filter kernels on the original large image.

**Difference of Gaussians (DoG) Appproximation**

>The true mathematical operator for finding scale-space blobs is the Laplacian of Gaussian (LoG). However, LoG is computationally expensive. SIFT's key insight was to use a highly efficient approximation: the **Difference of Gaussians (DoG)**.
>
>**Calculation**: A DoG image is created by simply taking two adjacent Gaussian-blurred images within the same octave and subtracting one from the other
>
>**Why it works**: This simple subtraction is mathematically a very good approximation of the scale-normalized LoG. The resulting DoG images are band-pass filters, meaning they enhance features (like blobs and corners) of a specific size while suppressing uniform areas.

**Finding Local Extrema**

>This is the core step of the detection process. The algorithm searches for candidate keypoints by looking for local maxima and minima in the DoG scale-space.
>
>**3D Neighborhood Comparison**: For every pixel in a DoG image, it is compared to its **26 neighbors**:
>- Its 8 immediate neighbors in the **same DoG image**.
>- The 9 corresponding neighbors in the DoG image **above it** (the next, more blurred level). 
>- The 9 corresponding neighbors in the DoG image **below it** (the previous, less blurred level).
>
>**Selection**: If the pixel's value is greater than all 26 neighbors (a local maximum) or less than all 26 neighbors (a local minimum), it is marked as a **candidate keypoint**.

<font color="red">This 3D search ensures that the selected point is a prominent feature not only in 2D image space but also across different scales, making it a stable point of interest.</font>

#### 3.2 Keypoint Localization

>Refine the location of keypoints to sub-pixel accuracy using a Taylor expansion. Then, filter out unstable keypoints that have low contrast or are located on an edge

**Goal**: 

>The candidate points from Stage 1 are rough estimates. They are located on a discrete pixel grid and at discrete scale levels. This stage refines their location to sub-pixel accuracy and filters out poor-quality points.

**The Process**

**1.Sub-pixel and Sub-scale Refinement**

>To find a more accurate location, SIFT fits a 3D quadratic model to the local DoG values around the candidate keypoint.

- **Taylor Expansion :** The algorithm uses a Taylor expansion of the DoG function up to the quadratic terms around the sample point. 
    
- **Finding the True Extremum:** By taking the derivative of this quadratic function with respect to `(x, y, σ)` and setting it to zero, we can solve for the location of the true extremum. This gives an offset `(Δx, Δy, Δσ)` from the initial integer coordinates. 
    
- **Update:** If the offset in any dimension is greater than 0.5, it means the true extremum is closer to another sample point. In this case, the process is iterated from that new point. Otherwise, the final refined keypoint location is the initial integer coordinate plus the calculated offset. 

**2.Discarding Low-Contrast Keyponts**

>Some of the refined extrema might still be noise. To filter them, SIFT checks the magnitude of the DoG function at the refined location.

**Contrast Check:** The value of the fitted quadratic function at the refined location, ∣D(x^)∣, is calculated. If this value is less than a certain contrast threshold (e.g., 0.03 in the original paper), the keypoint is discarded. This effectively removes points that are not prominent enough and are likely due to noise.

**3.Eliminating Edge Responses**

>The DoG function produces strong responses along edges, even if the edge is poorly defined in the perpendicular direction. Edges are not ideal features because they are not distinctive (you don't know _where_ along the edge you are). SIFT needs features that are well-localized in all directions (like corners).

**Hessian Matrix**

>To detect edges, SIFT computes the 2x2 Hessian matrix (H) of second-order derivatives at the keypoint's location.

$$H=\left(
\begin{matrix}
D_{xx} & D_{xy} \\
D_{xy} & D_{yy} \\
\end{matrix}
\right)$$

**Principal Curvatures**

>The eigenvalues of this Hessian, $\alpha$ and $\beta$, are proportional to the principal curvatures of the DoG function. The ratio of these eigenvalues tells us about the local geometry

- For a **corner-like feature**, the curvatures in both directions will be large and roughly equal. Thus, the eigenvalues α and β will be of similar magnitude.
    
- For an **edge-like feature**, there will be a large curvature across the edge but a very small curvature along the edge. This leads to one eigenvalue being much larger than the other.

**Ratio Check**

Let α be the larger eigenvalue and β be the smaller one. SIFT checks the ratio r=α/β. A threshold is set for this ratio (e.g., 10). If $\frac{(\alpha+\beta)^{2}}{\alpha \beta}\gt \frac{(r+1)^{2}}{r}$​, the keypoint lies on an edge and is rejected. This check is more numerically stable than calculating the eigenvalues directly and is derived from the trace and determinant of the Hessian, similar to the Harris corner detector

>After this second stage, the remaining points are high-quality, stable, and precisely located keypoints, ready for the next stages of orientation assignment and descriptor generation.