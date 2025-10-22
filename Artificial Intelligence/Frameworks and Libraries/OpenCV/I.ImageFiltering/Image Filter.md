### 1.cv.filter2D

<font color="Red">Cross-Correlation</font>

**Input**

>A source image in `numpy.ndarray` format

**Parameter Settings**

| **参数 (Parameter)** | **数据类型 (Data Type)** | **说明 (Description)**                       | **常用设置 (Common Settings)**                            |
| ------------------ | -------------------- | ------------------------------------------ | ----------------------------------------------------- |
| `src`              | `numpy.ndarray`      | 输入图像 (Source image)。                       | 你的原始图像变量。                                             |
| `ddepth`           | `int`                | 输出图像的深度（数据类型）。设置为-1表示输出图像的深度与输入图像相同。       | `-1` 是最常用的设置。有时为了避免数据溢出（如梯度计算），会设为 `cv2.CV_64F`。      |
| `kernel`           | `numpy.ndarray`      | 卷积核（或称为滤波器）。它是一个二维的浮点数数组。                  | 自定义一个 `numpy` 数组，例如一个 `(3, 3)` 或 `(5, 5)` 的锐化核或边缘检测核。 |
| `anchor`           | `tuple` (可选)         | 核的锚点（中心点）的相对位置。默认值为 `(-1, -1)`，表示锚点位于核的中心。 | 通常保持默认值 `(-1, -1)`。                                   |
| `delta`            | `float` (可选)         | 在卷积结果存入输出图像前，额外加到每个像素上的值。                  | 通常保持默认值 `0`。                                          |
| `borderType`       | `int` (可选)           | 像素外推方法，用于处理图像边界。                           | `cv2.BORDER_DEFAULT`。                                 |

**Output**

>A filtered image in numpy.ndarray format

***
### 2.cv2.blur (Averagin Filter)

**Input**

>image in np.ndarray

**Parameter Settings**

| **参数 (Parameter)** | **数据类型 (Data Type)** | **说明 (Description)**       | **常用设置 (Common Settings)**      |
| ------------------ | -------------------- | -------------------------- | ------------------------------- |
| `src`              | `numpy.ndarray`      | 输入图像。                      | 你的原始图像变量。                       |
| `ksize`            | `tuple`              | 卷积核的大小，格式为 `(宽度, 高度)`。     | `(3, 3)` 或 `(5, 5)`。值越大，模糊效果越强。 |
| `anchor`           | `tuple` (可选)         | 核的锚点。默认值为 `(-1, -1)`，表示中心。 | 保持默认值 `(-1, -1)`。               |
| `borderType`       | `int` (可选)           | 边界处理方式。                    | `cv2.BORDER_DEFAULT`。           |

**Output**

>A blurred image in np.ndarray

***
### 3.cv2.GaussianBlur (Gaussian Filtering)

**Input**

>an image in np.ndarray

**Parameter Settings**

| **参数 (Parameter)** | **数据类型 (Data Type)** | **说明 (Description)**                                | **常用设置 (Common Settings)**                                        |
| ------------------ | -------------------- | --------------------------------------------------- | ----------------------------------------------------------------- |
| `src`              | `numpy.ndarray`      | 输入图像。                                               | 你的原始图像变量。                                                         |
| `ksize`            | `tuple`              | 高斯核的大小，格式为 `(宽度, 高度)`。宽度和高度必须是**正奇数**。              | `(3, 3)` 或 `(5, 5)`。                                              |
| `sigmaX`           | `float`              | 高斯核在X方向上的标准差。这是控制模糊程度的关键参数。                         | 通常设为 `0`，此时 `sigmaX` 会根据 `ksize` 自动计算。如果想精确控制，可以设为 `1.5`, `2` 等值。 |
| `sigmaY`           | `float` (可选)         | 高斯核在Y方向上的标准差。如果设为 `0` 或省略，则 `sigmaY` 与 `sigmaX` 相等。 | 通常设为 `0` 或省略。                                                     |
| `borderType`       | `int` (可选)           | 边界处理方式。                                             | `cv2.BORDER_DEFAULT`。                                             |

**Output**

>A Gaussian Blurred image in np.ndarray

***
### 4.cv2.medianBlur

**Purpose**

>Median filtering, excellent for removing salt-and-pepper noise.

**Parameter Settings**

|**参数 (Parameter)**|**数据类型 (Data Type)**|**说明 (Description)**|**常用设置 (Common Settings)**|
|---|---|---|---|
|`src`|`numpy.ndarray`|输入图像。|你的原始图像变量。|
|`ksize`|`int`|滤波器孔径大小。必须是一个**大于1的奇数**。|`3`, `5`, `7`。值越大，模糊效果越强。|

***
### 5.cv2.bilateralFilter

>Bilateral filtering, a non-linear, **edge-preserving** noise reduction and smoothing filter.

**Parameter Settings**

| **常用设置 (Common Settings)**                         | **参数 (Parameter)** | **数据类型 (Data Type)** | **说明 (Description)**                              |
| -------------------------------------------------- | ------------------ | -------------------- | ------------------------------------------------- |
| 你的原始图像变量。                                          | `src`              | `numpy.ndarray`      | 输入图像。                                             |
| 通常设为 `5` 到 `9` 之间的一个正整数。值越大，计算越慢。                  | `d`                | `int`                | 在滤波期间使用的每个像素邻域的直径。如果设为非正数，则会从 `sigmaSpace` 计算得到。  |
| `75` 到 `150` 之间。这是控制滤波效果的关键参数之一。                   | `sigmaColor`       | `float`              | **色彩空间**的滤波标准差。值越大，意味着越远的颜色也会被混合在一起，产生更大区域的半均匀颜色。 |
| `75` 到 `150` 之间。当 `d > 0` 时，它指定邻域大小；否则，邻域大小取决于此参数。 | `sigmaSpace`       | `float`              | **坐标空间**的滤波标准差。值越大，意味着越远的像素会相互影响（只要它们的颜色足够接近）。    |
| `cv2.BORDER_DEFAULT`。                              | `borderType`       | `int` (可选)           | 边界处理方式。                                           |
