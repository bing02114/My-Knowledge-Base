### 1.1D Fourier Analysis and Fourier Descriptors
#### 1.1 The Fourier Descriptor for Shape Analysis

**Concept**

>The idea is to classify objects using their features in the frequency domain instead of the spatial domain

**Shape to Periodic Function**

>A closed shape's boundary can be converted into a 1D periodic function by plotting the radial distance from the center against the arc length along the boundary

**Classification**

>The frequency components of this periodic function can be calculated and used as a feature vector to classify the shape

#### 1.2 Fourier Series and Harmonics

**Fundamental Principle**

>Any function f(x) can be broken down and represented as a weighted sum of sine and cosine waves of different frequencies

**Mathematical Representation**

$$f(x)=a_{0}+a_{1}cos\theta+b_{1}sin\theta+a_{2}cos2\theta+b_{2}sin2\theta +\dots$$

$$f(x)=\sum^{\infty}_{h=0}a_{h}\cos(2\pi h\frac{x}{N})+b_{h}sin(2\pi h\frac{x}
{N})$$

**Calculating Coefficients**

$$F_c(u)=\frac{1}{N}\sum^{N-1}_{x=0}f(x)\cos(2\pi u\frac{x}{N})$$

$$F_c(u)=\frac{1}{2}a_u$$

$$F_s(u)=\frac{1}{N}\sum^{N-1}_{x=0}f(x)\sin(2\pi u\frac{x}{N})$$

$$F_s{u}=\frac{1}{2}b_{u}$$

***
### 2.The Fourier Transform and its Properties

