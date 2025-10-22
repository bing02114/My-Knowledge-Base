### 1.cv2.cornerHarris

#### 1.1 Goal

>To implement the Harris Corner Detection algorithm. Its main goal is to identify pixels in an image that are corners by analyzing the local intensity changes. It produces a "cornerness" score for every pixel.

#### 1.2 Input

>The function requires a single-channel, floating-point image. Therefore, you must first convert your input image to grayscale and then to `np.float32` format.

#### 1.3 Parameter Settings

``` python
dst = cv2.cornerHarris(src, blockSize, ksize, k)
```

- `src`: The input grayscale, float32 image.
    
    - 输入的灰度、float32格式的图像。
        
- `blockSize`: The size of the neighborhood considered for corner detection. A typical value is 2 or 3. It defines the size of the window `W` used to compute the structure tensor matrix `M`.
    
    - 用于角点检测的邻域大小。典型值为2或3。它定义了用于计算结构张量矩阵 `M` 的窗口 `W` 的大小。
        
- `ksize`: The aperture parameter for the Sobel operator, which is used internally to calculate the image gradients (Ix​ and Iy​). It must be an odd number (e.g., 3, 5, 7).
    
    - Sobel算子的孔径参数，该算子在函数内部用于计算图像梯度（Ix​ 和 Iy​）。它必须是一个奇数（例如3, 5, 7）。
        
- `k`: The Harris detector's free parameter in the corner response equation (R=det(M)−k(trace(M))2). Its value is usually between 0.04 and 0.06.
    
    - Harris角点响应方程（R=det(M)−k(trace(M))2）中的自由参数。其值通常在0.04到0.06之间。

#### 1.4 Output

>`dst`: The output is a single-channel floating-point array of the same size as the input image. This array is the **corner response map**. Each pixel's value in this map represents its "cornerness" score `R`. High positive values indicate strong corners, negative values indicate edges, and small values indicate flat regions. You need to apply a threshold to this map to select the actual corner points.

***
### 2.cv2.goodFeaturesToTrack

#### 2.1 Goal

>To implement the Shi-Tomasi corner detector. Its goal is to find the N strongest corners in an image. It's often considered an improvement over Harris for tracking applications because the selection criterion (R=min(λ1​,λ2​)) ensures that the detected points are well-defined in all directions.

#### 2.2 Input

>A single-channel (grayscale) 8-bit or 32-bit floating-point image.

#### 2.3 Parameter Settings

```python
corners = cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance)
```

- `image`: The input grayscale image.
    
    - 输入的灰度图像。
        
- `maxCorners`: The maximum number of corners to return. If more corners are detected, the function will return only the strongest ones.
    
    - 返回的角点最大数量。如果检测到的角点超过此数目，函数将只返回最强的那些角点。
        
- `qualityLevel`: A value between 0 and 1. It characterizes the minimal accepted quality of image corners. The function rejects all corners with a quality measure less than `qualityLevel` * (best corner's quality measure).
    
    - 一个介于0和1之间的值。它代表了可接受的图像角点的最低质量。函数会拒绝所有质量分数低于 `qualityLevel` * (最强角点的质量分数) 的角点。
        
- `minDistance`: The minimum possible Euclidean distance between the returned corners. This parameter is useful for ensuring the corners are well-distributed across the image and not clustered together.
    
    - 返回的角点之间可能的最小欧几里得距离。这个参数对于确保角点在图像上分布均匀、而不是聚集在一起非常有用。


#### 2.4 Output

>`corners`: A NumPy array of shape `(N, 1, 2)`, where `N` is the number of detected corners. Each entry contains the floating-point `(x, y)` coordinates of a detected corner.

***
### 3.cv2.SIFT_create & detectAndCompute

#### 3.1 Goal

>To create a SIFT (Scale-Invariant Feature Transform) object that can detect keypoints and compute their descriptors. The overall goal is to find features that are robust to changes in scale, rotation, illumination, and viewpoint, and describe them with a unique numerical vector for matching purposes.

#### 3.2 Input

>The primary method, `detectAndCompute`, takes a single-channel, 8-bit grayscale image (`np.uint8`).

#### 3.3 Parameter Settings

``` python
# Create the SIFT object
sift = cv2.SIFT_create(nfeatures=0, nOctaveLayers=3, contrastThreshold=0.04, edgeThreshold=10, sigma=1.6)

# Use its method to find keypoints and descriptors
keypoints, descriptors = sift.detectAndCompute(gray_image, None)
```

**`cv2.SIFT_create()` Parameters:**

- `nfeatures`: The number of best features to retain. The features are ranked by their scores. `0` means retain all.
    
    - 要保留的最佳特征的数量。特征按其分数进行排序。`0` 表示保留所有特征。
        
- `nOctaveLayers`: The number of layers in each octave. The default is 3.
    
    - 每个八度（octave）中的层数。默认为3。
        
- `contrastThreshold`: Used to filter out weak features in semi-uniform regions. The larger the threshold, the fewer features are produced. Default is 0.04.
    
    - 用于过滤掉半均匀区域中的弱特征的阈值。阈值越大，产生的特征越少。默认为0.04。
        
- `edgeThreshold`: Used to filter out edge-like features. The higher the threshold, the more features are retained. Default is 10.
    
    - 用于过滤掉类边缘特征的阈值。阈值越高，保留的特征越多。默认为10。
        
- `sigma`: The sigma of the Gaussian applied to the input image at the first octave. Default is 1.6.
    
    - 在第一个八度应用于输入图像的高斯模糊的sigma值。默认为1.6。

#### 3.4 Output

The `detectAndCompute` method returns two values:

`detectAndCompute` 方法返回两个值：

- `keypoints`: A list of `cv2.KeyPoint` objects. Each `KeyPoint` object is a complex data structure that contains:
    
    - `pt`: The `(x, y)` coordinates of the keypoint.
        
    - `size`: The diameter of the keypoint's neighborhood, representing its **scale**.
        
    - `angle`: The orientation of the keypoint (from 0 to 360 degrees), representing its **rotation**.
        
    - `response`: The strength of the keypoint.
        
    - 一个 `cv2.KeyPoint` 对象的列表。每个 `KeyPoint` 对象是一个复杂的数据结构，包含：
        
        - `pt`：关键点的 `(x, y)` 坐标。
            
        - `size`：关键点邻域的直径，代表其**尺度**。
            
        - `angle`：关键点的方向（0到360度），代表其**旋转**。
            
        - `response`：关键点的响应强度。
            
- `descriptors`: A NumPy array of shape `(N, 128)`, where `N` is the number of keypoints. Each of the `N` rows is a 128-dimensional floating-point vector that serves as the unique "fingerprint" for the corresponding keypoint in the `keypoints` list. This array is used for matching features between different images.
    
    - 一个形状为 `(N, 128)` 的NumPy数组，其中 `N` 是关键点的数量。`N`行中的每一行都是一个128维的浮点向量，作为 `keypoints` 列表中对应关键点的独特“指纹”。这个数组用于在不同图像之间进行特征匹配。