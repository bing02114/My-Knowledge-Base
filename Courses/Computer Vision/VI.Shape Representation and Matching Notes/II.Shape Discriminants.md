>Since exhaustive template matching is very time-consuming, a more efficient approach is to use shape discriminants. These are simple, calculated properties of an object that are independent of its position and often its orientation and scale.

### 1.Basic Discriminants

**Area and Perimeter**

>The simplest features to extract from an object's shape. For a polygon, the area can be calculated from its edge vectors, and the perimeter is the sum of the lengths of its edges.

**Elongatedness**

>A measure of how long and thin an object is. It can be defined as

* The ratio of length to width of the minimum-area bounding rectangle around the object

* The ratio of the area to the square of its maximum thickness $Area/(2d)^2$, where thickness is found using morphological erosion. This measure is invariant to translation, rotation, and scaling

**Signatures**

>A 1D function derived from the shape's boundary, such as plotting the distance from the centroid to the boundary points as a function of angle

***
### 2.Moments

>Moments treat the grey level of each pixel as a weight, analogous to moments in mechanics. The general moment $m_{pq}$ is calculated as: $m_{pq}=\sum_{i}\sum_{j}i^{p}j^{q}f(i,j)$

**Translation Invariance**

>Achieved by using **central moments** (μpq​), which are calculated relative to the object's center of gravity (centroid). The centroid is found using the zeroth (m00​, which is the area) and first (m10​,m01​) moments

**Second Moments**

>These measure how "spread out" an object is and can be used to determine its orientation. The eigenvectors of the covariance matrix of the central moments correspond to the major and minor axes of the object. However, second moments cannot distinguish between an object and its reflection

**Direction**

>For elongated objects, the orientation can be calculated from the second central moments using the formula:

$$\theta=\frac{1}{2}tan^{-1}(\frac{2\mu_{11}}{\mu_{20}-\mu_{02}})$$

**Texture-Based Discriminants**

* **Energy and Entropy:** These are useful for objects with characteristic textures or grey-level distributions. They are calculated from the histogram (probability of each grey level) of the object's pixels

**Geometric Feature-Based Discriminants:**

* When the above discriminants are not sufficient, specific geometric features can be used, especially for polygonal objects
* Examples include:
	* Number of vertices
	* Distance of each vertex from the centroid
	* Angles between vertices relative to the centroid