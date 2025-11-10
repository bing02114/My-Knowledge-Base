### 1.Light, Shading, Texture and Surfaces

**Image Brightness (图像亮度):** The image of a 3D object depends on its shape, reflectance properties, and the distribution of light sources (3D 对象的图像取决于其形状、反射特性以及光源的分布).

**Impact of Lighting (光照的影响):** Images taken from a fixed camera can show significant differences (e.g., different visible edges) based only on the lighting conditions (仅凭光照条件，固定相机拍摄的图像就可能显示出显著差异（例如，不同的可见边缘）).

**Reflectance (反射):** This is a measure of the visible light reflected from a surface when illuminated (这是对表面被照射时反射的可见光的度量). It is formally described by the **Bidirectional Reflectance Distribution Function (BRDF)** (它由**双向反射分布函数 (BRDF)** 正式描述).

**Type of Reflectors**

* ***Specular (镜面反射):** Mirror-like reflection (镜面般的反射).
* **Diffuse / Lambertian (漫反射 / 朗伯体):** Scatters light equally in all directions. These surfaces appear matte (向所有方向均匀散射光线。这些表面呈现哑光

***
### 2.Introduction to Photometric Stereo

**Core Idea (核心思想):** An alternative to traditional stereo (which uses two cameras).

**Method (方法):** Photometric Stereo uses **one fixed camera** but multiple (one or more) light sources illuminating the object from different directions (光度立体使用**一台固定相机**，但有多个（一个或多个）光源从不同方向照射物体).

**Key Assumption (关键假设):** This method requires assumptions about the surface properties, most commonly that the surface is **Lambertian** (该方法需要对表面特性进行假设，最常见的是假设表面是**朗伯体**).

**Best Use Case (最佳用例):** Appropriate for applications where lighting can be easily controlled (适用于可以轻松控制照明的应用).

**Lambert's Cosine Law (朗伯余弦定律):** For Lambertian surfaces, the emitted light is proportional to the cosine of the angle (θi​) between the surface normal (n) and the light source direction (s) (对于朗伯表面，其发出的光与表面法线 (n) 和光源方向 (s) 之间的夹角 (θi​) 的余弦成正比).

***
### 3.The Reflectance Map (R)

**Definition (定义):** The reflectance map R(p,q) gives the relationship between the surface brightness and the **gradient space** parameters (p,q) (反射图 R(p,q) 给出了表面亮度与**梯度空间**参数 (p,q) 之间的关系).

**Surface Gradient**

>A surface can be parameterized as Z=f(X,Y) (表面可以参数化为 Z=f(X,Y)).

>The gradient parameters p and q are defined as the partial derivatives of the surface (梯度参数 p 和 q 定义为表面的偏导数)

$$p=-(\frac{\partial Z}{\partial X})$$

$$q=-(\frac{\partial Z}{\partial Y})$$

The **surface normal vector (n)** can then be represented as n=[p,q,1]T (表面**法向量 (n)** 继而可以表示为 n=[p,q,1]T). (This is a non-unit vector used for convenience (这是一个为方便而使用的非单位向量) ).

**Reflectance Map Equation (反射图方程):**

$$R(p,q)=\rho\frac{n·s}{|n||s|}$$

$$R(p,q)=\rho\frac{s_xp+s_yq+s_z}{\sqrt{p^2+q^2+1}}$$

**Properties**

This equation is **non-linear** (a second-order equation of p and q) (这个方程是**非线性**的（一个关于 p 和 q 的二阶方程）)

Contours of constant R(p,q) are conic sections (恒定 R(p,q) 的等值线是圆锥截线).

In the special case where the light is aligned with the camera (s=[0,0,1]), the contours are simple circles (在光线与相机对齐（s=[0,0,1]）的特殊情况下，等值线是简单的圆形).

***
### 4.Solving for (p,q) with Photometric Stereo

**The Challenge (挑战):** With one light source, we have one non-linear equation with three unknowns (p, q, and ρ). With two light sources, we have two non-linear equations, which can have multiple or no solutions (一个光源时，我们有一个非线性方程和三个未知数（p, q, 和 ρ）。两个光源时，我们有两个非线性方程，这可能有多个解或无解)

**The Solution (解决方案):** Use **three** independent lighting conditions (使用**三个**独立的照明条件).

**After solving**

* We have the p and q values (gradients) for every pixel (我们得到了每个像素的 p 和 q 值（梯度）).
* We find the 3D depth (Z) by performing a 2D **integration** of p and q across the surface (我们通过对 p 和 q 在表面上进行 2D **积分**来找到 3D 深度（Z）).
* **Problem with Integration (积分的问题):** Image noise introduces errors in p and q. These errors will propagate and accumulate along the integration path, leading to distorted results (图像噪声会在 p 和 q 中引入误差。这些误差会沿着积分路径传播和累积，导致结果失真).


***
### 5.Shape from Shading (SFS)

**Local vs. Global (局部 vs. 全局):** Photometric stereo is a **local** method; it calculates each pixel independently (光度立体是一种**局部**方法；它独立计算每个像素).

**Shape-from-Shading (SFS):** A **global** method that typically uses only **one** light source (明
暗恢复形状 (SFS) 是一种**全局**方法，通常只使用**一个**光源).

**SFS Assumption (SFS 假设):** It assumes the object's surface is **smooth** (它假设物体表面是**光滑的**).

**Method (方法):** SFS finds the p and q values that minimize a total error function (E) across the whole image (SFS 通过最小化整个图像的总误差函数 (E) 来找到 p 和 q 值). The error function has two parts (该误差函数有两部分):

1. **Brightness Error (亮度误差):** (I(x,y)−R(p,q))2. This tries to match the estimated brightness R(p,q) with the actual measured image intensity I(x,y) (这试图使估计的亮度 R(p,q) 与实际测量的图像强度 I(x,y) 相匹配).
2. **Smoothness Constraint (平滑度约束):** λS(...)=λ((∂x∂p​)2+(∂y∂p​)2+...). This penalizes rapid changes in the surface gradient, forcing a smooth result (这会对表面梯度的快速变化进行惩罚，从而强制产生平滑的结果).

**Solving SFS (求解 SFS):** This minimization problem is complex and solved using a method called the **calculus of variations** (这个最小化问题很复杂，需要使用一种称为**变分法**的方法来解决).
***
### 6.Limitations and Other Shape from X Methods

**Limitations of Photometric Methods (光度法的局限性):**

* Assumes distant/uniform light sources (假设光源在远处或是均匀的).
* Assumes **orthogonal projection** (orthographic projection), which is inaccurate for close-ups or large depth variations. (Perspective projection is more realistic)
* Assumes perfectly **Lambertian** surfaces, but most real objects have specular (shiny) components (假设表面是完美的**朗伯体**，但大多数真实物体都有镜面（闪亮）成分).

**Other "Shape from X" Methods (其他“Shape from X”方法):**

* **Shape from Stereo (立体恢复形状):** Uses two or more views and feature correspondence (使用两个或更多视图及特征对应).
* **Shape from Motion (运动恢复形状):** Infers 3D structure from 2D motion sequences (从 2D 运动序列推断 3D 结构).
* **Shape from Texture (纹理恢复形状):** Estimates shape from texture distortion (从纹理的扭曲估计形状).
* **Shape from Focus/Defocus (聚焦/散焦恢复形状):** Uses multiple images with different focal lengths to infer depth from blur (使用不同焦距的多张图片，从模糊程度推断深度).