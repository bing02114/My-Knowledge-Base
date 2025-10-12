### 1.The Gaussian Filter

#### 1.1 Definition

>This is a filter whose convolution kernel is a 2D Gaussian function

$$h(i,j)=\frac{1}{2\pi\sigma^{2}}e^{\frac{i^2+j^2}{2\sigma^2}}$$
* ignore small values outside $[-k\sigma,k\sigma]$
#### 1.2 Advantages

>It is a smoothing filter that **gives more weight to the central pixel** and less weight to its neighbors, resulting in a more natural blur compared to a simple average filter.

>**A key advantage is that the Gaussian filter is <font color="Red">separable</font>, which allows for highly efficient computation.**

$$h(i,j)=h(i)*h{j}$$

$$h(i)=\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{i^2}{2\sigma^2}}$$


### 2.Structure Adaptive Filtering

#### 2.1 Motivation

>Fixed filters (like averaging or Gaussian) are applied uniformly across the image, which can blur important structures like edges and fine details. Structure adaptive methods adjust the filtering based on local image content to preserve these details.

#### 2.2 Methods

**Averaging according to Inverse Gradient:** 

The filter weights are calculated at each pixel based on the intensity difference, so that averaging happens more within homogeneous regions and less across sharp edges.

**Averaging with Rotating Masks:** 

This method avoids blurring edges by searching for the most homogeneous (least varied) orientation in a pixel's neighborhood and performing the averaging only in that direction.