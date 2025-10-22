### 1.cv2.dft

#### 1.1 Purpose

- To perform the Discrete Fourier Transform (DFT) on a given array (typically an image).
    
- Its main purpose is to convert a signal from its spatial domain representation (pixels and coordinates) into its frequency domain representation (frequencies and their magnitudes/phases).
#### 1.2 Input

>A source array, `src`, which should be a `numpy.ndarray` of data type `np.float32` or `np.float64`.

#### 1.3 Parameter Settings

| **Parameter (参数)** | **Data Type (数据类型)** | **Description (说明)**                                                                         | **Common Settings (常用设置)**                                                                                                                                          |
| ------------------ | -------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`              | `numpy.ndarray`      | The input array. (输入数组。)                                                                     | Your `np.float32` converted image. (您转换成 `np.float32` 的图像。)                                                                                                         |
| `flags`            | `int`                | A combination of flags that control the behavior of the transform. (控制变换行为的标志组合。)            | `cv2.DFT_COMPLEX_OUTPUT`: This is the most important flag. It ensures the output is a 2-channel array (Real part, Imaginary part). (这是最重要的标志。它确保输出是一个双通道数组（实部，虚部）。) |
| `nonzeroRows`      | `int` (Optional)     | Can be used to optimize the calculation for arrays with many zero rows. (可用于优化包含很多零行的数组的计算。) | Usually left at the default value of 0. (通常保持默认值0。)                                                                                                                 |

#### 1.4 Output

- A `numpy.ndarray` representing the frequency spectrum of the input.
    
- If `flags=cv2.DFT_COMPLEX_OUTPUT` is used, the output will be a **2-channel array** of the same size as the input. The first channel contains the real part of the complex numbers, and the second channel contains the imaginary part.

***
### 2.np.fft.fftshift

#### 2.1 Purpose

- To rearrange the quadrants of a frequency spectrum array.
    
- It shifts the zero-frequency component (the "DC component," representing the average intensity) from the top-left corner **to the center** of the array. This is done for easier visualization and filtering, as low frequencies will be clustered in the middle.

#### 2.2 Input

>An array `x`, which is typically the output of a Fourier Transform like `cv2.dft`.

#### 2.3 Parameter Settings

|**Parameter (参数)**|**Data Type (数据类型)**|**Description (说明)**|**Common Settings (常用设置)**|
|---|---|---|---|
|`x`|`numpy.ndarray`|The input array to be shifted. (要移位的输入数组。)|The output from `cv2.dft`. (来自 `cv2.dft` 的输出。)|
|`axes`|`tuple` or `int` (Optional)|The axes over which to perform the shift. If `None`, all axes are shifted. (要执行移位的轴。如果为 `None`，则所有轴都会被移位。)|For a 2D image, you can leave it as the default `None`. (对于2D图像，可以保持默认值 `None`。)|

#### 2.4 Output

>A `numpy.ndarray` of the same shape and type as the input, but with its quadrants swapped.

***
### 3.np.fft.ifftshift

#### 3.1 Purpose

- To perform the **inverse** operation of `np.fft.fftshift`.
    
- It rearranges the quadrants of a shifted spectrum, moving the zero-frequency component from the center **back to the top-left corner**. This is a necessary step before applying the Inverse DFT.

#### 3.2 Input

>An array `x` that has been shifted by `np.fft.fftshift`.

#### 3.3 Parameter Settings

>Same as `np.fft.fftshift`

#### 3.4 Output

>A `numpy.ndarray` with the original frequency spectrum layout, ready for the inverse transform.

***
### 4.cv2.idft

#### 4.1 Goal

- To perform the Inverse Discrete Fourier Transform (IDFT).
    
- Its purpose is to convert a signal from the frequency domain **back into the spatial domain**.

#### 4.2 Input

>A source array `src`, which is the frequency spectrum (typically a 2-channel complex array).

#### 4.3 Parameter Settings

| **Parameter (参数)** | **Data Type (数据类型)** | **Description (说明)**                                                                                             | **Common Settings (常用设置)**                                                                                                                                                                                          |
| ------------------ | -------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src`              | `numpy.ndarray`      | The input frequency spectrum. Must be in the original layout (zero-frequency at corners). (输入频谱。必须是原始布局（零频在角落）。) | The output of `np.fft.ifftshift`. (来自 `np.fft.ifftshift` 的输出。)                                                                                                                                                      |
| `flags`            | `int`                | Flags that control the behavior.                                                                                 | `cv2.DFT_INVERSE` is required to specify it's an inverse transform. `cv2.DFT_SCALE` is often used to scale the result back to its original range. (需要 `cv2.DFT_INVERSE` 来指定它是逆变换。通常使用 `cv2.DFT_SCALE` 将结果缩放回其原始范围。) |
| `nonzeroRows`      | `int` (Optional)     | Same as in `cv2.dft`. (与 `cv2.dft` 中相同。)                                                                         | Usually left at the default value of 0. (通常保持默认值0。)                                                                                                                                                                 |

#### 4.4 Output

- A `numpy.ndarray` representing the image in the spatial domain.
    
- The output is typically a 2-channel complex array (real, imaginary). You must calculate its magnitude (`cv2.magnitude`) to get a viewable single-channel image.
