### 1.cv2.matchTemplate

#### 1.1 Goal

>To find the location of a small "template" image within a larger source image by sliding the template over the source and calculating a similarity metric at each location

#### 1.2 Input

* image
* template

#### 1.3 Parameter Settings

| **Parameter (参数)** | **Data Type (数据类型)** | **Description (说明)**                                                   | **Common Settings (常用设置)**                                                                                                                                                                                                                                                        |
| ------------------ | -------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `image`            | `numpy.ndarray`      | The source image. (源图像。)                                               | Your main image.                                                                                                                                                                                                                                                                  |
| `template`         | `numpy.ndarray`      | The template image. Must be smaller than the source. (模板图像。尺寸必须小于源图像。) | Your template.                                                                                                                                                                                                                                                                    |
| `method`           | `int`                | The comparison method to use for matching. (用于匹配的比较方法。)                | `cv2.TM_CCOEFF_NORMALISED`: Normalized cross-correlation. This is often the most robust choice as it is insensitive to global brightness changes. For this method, the highest value in the result map is the best match. (归一化互相关。这通常是最鲁棒的选择，因为它对全局亮度变化不敏感。对于此方法，结果图中的最大值即为最佳匹配。) |

#### 1.4 Output

>A **result map** (or correlation map). This is a grayscale image where each pixel `(x, y)` represents how well the template matches the source image region whose top-left corner is `(x, y)`. You need to use `cv2.minMaxLoc()` on this map to find the location of the best match.


***
### 2.cv2.findContours

#### 2.1 Goal

>To find and extract the outlines (contours) of all continuous shapes in a **binary image**. It treats all white pixels as part of an object and finds the boundary between the white and black regions.

#### 2.2 Input

>A single-channel, 8-bit binary image (values are 0 for background, 255 for foreground). **This is a strict requirement.**

#### 2.3 Parameter Settings

|**Parameter (参数)**|**Data Type (数据类型)**|**Description (说明)**|**Common Settings (常用设置)**|
|---|---|---|---|
|`image`|`numpy.ndarray`|The input binary image. **Note:** This function modifies the source image, so it's best to pass a copy (e.g., `thresh.copy()`). (输入的二值图像。**注意**：此函数会修改源图像，所以最好传入一个副本。)|A thresholded or Canny edge map.|
|`mode`|`int`|The contour retrieval mode, which defines the hierarchy of the contours. (轮廓检索模式，定义了轮廓的层级结构。)|`cv2.RETR_EXTERNAL`: Retrieves only the outermost parent contours. Fast and simple. `cv2.RETR_TREE`: Retrieves all contours and reconstructs the full hierarchy of nested shapes (e.g., a circle inside a square). (`RETR_EXTERNAL`：只检索最外层的父轮廓。快速且简单。 `RETR_TREE`：检索所有轮廓并重建完整的嵌套形状层级。)|
|`method`|`int`|The contour approximation method, which determines how the points of the contour are stored. (轮廓逼近方法，决定了轮廓的点如何存储。)|`cv2.CHAIN_APPROX_SIMPLE`: Compresses segments and leaves only their end points. Saves memory and is efficient. `cv2.CHAIN_APPROX_NONE`: Stores all the boundary points. (`CHAIN_APPROX_SIMPLE`：压缩线段，只保留端点。节省内存且高效。 `CHAIN_APPROX_NONE`：存储所有的边界点。)|
#### 2.4 Output

A tuple of two items: `(contours, hierarchy)`

- `contours`: A Python **list** of all the contours found in the image. Each individual contour in this list is a **NumPy array** of `(x, y)` coordinates that form the outline of the shape. 一个包含图像中所有轮廓的Python**列表**。此列表中的每个独立轮廓都是一个由构成形状轮廓的`(x, y)`坐标组成的**NumPy数组**。
    
- `hierarchy`: An array that describes the parent-child relationships between contours. 一个描述轮廓之间父子关系的数组。

***
### 3.Discriminants

#### 3.1 cv2.contourArea
#### 3.2 cv2.arcLength
#### 3.3 cv2.moments
#### 3.4 cv2.minAreaRect