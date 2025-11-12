根据提供的课件 `cv14_-_Photometric_Stereo.pdf` 以及近五年（2020-2025）的考试真题，**CV14 (Photometric Stereo)** 是考试中关于 **“3D 重建 (3D Reconstruction)”** 的核心章节。

这部分内容通常出现在 **第 1 题 (Image Formation/Filtering)** 或单独的大题中，考查形式以 **计算题** 为主，要求利用光照模型反推物体表面的几何形状。

以下是详细的考点分析及考察形式：

### 1. 核心考点：光度立体视觉计算 (Photometric Stereo Calculation)

这是本章最核心的考点，几乎所有的计算题都围绕这个模型展开。

- **考点内容：**
    
    - **基本原理：** 利用**固定视点**下，**三个或更多不同方向的光源**拍摄的图像，来消除未知反照率 $\rho$ (Albedo) 的影响，从而求解表面法向量 $n$。
        
    - **朗伯模型 (Lambertian Model):** $I = \rho (n \cdot s)$。其中 $I$ 是观测亮度，$n$ 是表面法线，$s$ 是光源方向。
        
    - **矩阵求解:** 将三个方程联立为矩阵形式 $I = S \cdot M$（其中 $S$ 是光源矩阵，$M = \rho n$ 是表面属性），利用最小二乘法或直接求逆解出 $M$。
        
    - **求解法向量与反照率:**
        
        - 反照率 $\rho = |M|$（模长）。
            
        - 法向量 $n = M / |M|$（单位化）。
            
- **考察形式：**
    
    - **数值计算 (高频):** 题目给出 3 个光源的方向向量 $s_1, s_2, s_3$ 和对应像素的亮度值 $I_1, I_2, I_3$，要求计算该点的 **表面法向量 (Surface Normal)** 和 **反照率 (Albedo)**。
        
        - _例如：2020-21 Q1(b) 给出了具体的 $s$ 和 $I$，要求证明并计算 $n$ 和 $\rho$。_
            
    - **光源检测:** 给出法向量和观测到的亮度，反推光源的方向。
        

### 2. 核心考点：梯度空间与表面法线 (Gradient Space & Surface Normals)

这部分考查对几何参数 $p, q$ 的理解，它们是连接“图像亮度”与“3D 深度”的桥梁。

- **考点内容：**
    
    - **梯度定义:** $p = \frac{\partial z}{\partial x}, \quad q = \frac{\partial z}{\partial y}$。
        
    - **法向量表示:** 表面法向量可以表示为 $n = \frac{(-p, -q, 1)}{\sqrt{1 + p^2 + q^2}}$。
        
    - **反射图 (Reflectance Map):** $R(p,q)$ 是关于 $p, q$ 的函数，描述了特定光源下表面取向与亮度的关系。等亮度线 (Iso-brightness contours) 是 $R(p,q)$ 的轮廓。
        
- **考察形式：**
    
    - **公式推导/转换:** 题目可能给出 $n$ 要求求 $p, q$，或者给出 $(p, q)$ 要求写出 $n$。
        
    - **概念解释:** 解释什么是梯度空间，或者为什么仅凭一张图片无法确定唯一的 $(p, q)$（因为一个亮度值对应反射图上的一条曲线，有无数个可能的 $p, q$ 组合，这就是 Shape from Shading 的歧义性）。
        

### 3. 核心考点：表面重建/积分 (Surface Reconstruction / Integration)

计算出法向量或梯度 $(p, q)$ 后，如何恢复深度 $Z$。

- **考点内容：**
    
    - **积分法:** $Z(x, y) = Z(x_0, y_0) + \int_{(x_0, y_0)}^{(x, y)} (p dx + q dy)$。
        
    - **路径无关性:** 在理想无噪声情况下，沿着不同路径积分得到的深度应该是一样的（即 $\frac{\partial p}{\partial y} = \frac{\partial q}{\partial x}$）。
        
- **考察形式：**
    
    - **简答/设计题:** 问“得到梯度场 $(p, q)$ 后，如何恢复物体的 3D 形状？” 答案是**沿路径积分**。
        
    - **误差分析:** 可能会问如果数据有噪声，直接积分会发生什么（路径依赖，导致表面撕裂或不闭合），以及如何解决（使用全局优化算法或正则化）。
        

### 4. 辅助考点：Shape from Shading (SfS) vs Photometric Stereo

这部分通常作为对比考查，用于体现 Photometric Stereo 的优势。

- **考点内容：**
    
    - **SfS (单张图):** 这是一个**病态问题 (Ill-posed problem)**，因为未知数（$p, q$）多于方程数（1个亮度方程）。需要引入平滑性约束 (Smoothness constraint) 或可积性约束。
        
    - **Photometric Stereo (多张图):** 通过增加光源（增加方程数），将问题转化为**线性可解**问题，精度更高且无需平滑假设。
        
- **考察形式：**
    
    - **对比题:** 问“为什么 Photometric Stereo 比 Shape from Shading 更鲁棒？”或者“列举 Shape from X 的几种方法并简述原理”。
        
        - _例如：20-21 Q1(a) 要求对比 Photometric Stereo 和 Stereo Vision（双目立体视觉），指出适用场景（Photometric Stereo 适合光滑无纹理表面，Stereo Vision 需要纹理特征）。_
            

### 总结建议 (Summary for Preparation)

针对 CV14 的复习，重点在于**计算模型**：

1. **熟练掌握矩阵运算:** 确保你能手算 $3 \times 3$ 矩阵的逆（或者利用题目给出的特殊条件简化计算），这是解决 Photometric Stereo 题目的关键。
    
2. **牢记法向量公式:** 记住 $n = (-p, -q, 1)$ 的形式及其归一化。
    
3. **理解梯度物理意义:** $p$ 是表面沿 x 轴的倾斜度，$q$ 是沿 y 轴的倾斜度。
    
4. **区分应用场景:**
    
    - **有纹理 (Textured):** 用特征匹配 + 双目立体视觉 (Stereo Vision, CV12/13)。
        
    - **光滑无纹理 (Smooth/Textureless):** 用光度立体视觉 (Photometric Stereo, CV14)。