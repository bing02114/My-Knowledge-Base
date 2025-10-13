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

**Orthogonal Functions**

if $p\neq q$, 

$$\int^{2\pi}_{0}sin(p\theta)sin(q\theta)d\theta=0$$

$$\int^{2\pi}_{0}cos(p\theta)cos(q\theta)d\theta=0$$

**Different Forms**

Amplitude-phase

$$f(x)=\frac{A_0}{2}+\sum^{N}_{h=1}(A_{h}cos(2\pi h\frac{x}{N}-φ_h))$$

Exponential form

$$f(x)=\sum^{N}_{h=-N}c_{h}e^{i2\pi h\frac{x}{N}}$$

***
### 2.The Fourier Transform and its Properties

#### 2.1 The Discrete Fourier Transform (DFT)

**Definition**

>A tool that converts a function from its original domain (e.g., spatial or time) into its frequency domain representation

**Complex Form**

>The DFT is typically expressed using complex numbers, where the output F(u) is a complex value for each frequency u

$$F(u)=\frac{1}{N}\sum^{N-1}_{x=0}f(x)(e^{-2j\pi u\frac{x}{N}})$$

$$e^{ik}=\cos k+i\sin k$$
$$F(u)=\frac{1}{N}\sum^{N-1}_{x=0}f(x)(cos(2\pi u\frac{x}{N}-jsin(2\pi u \frac{x}{N})))$$

$$F(u)=F_c(u)-jF_{s}(u)$$

**Amplitude**

$$|F(u)|=\sqrt{F^{2}_{s}(u)+F^{2}_{c}(u)}$$

**Phase**

$$𝜑(u)=\tan^{-1}\frac{F_{s}(u)}{F_{c}(u)}$$

**Inverse**

$$f(x)=\sum^{N-1}_{u=0}F(u)(e^{2j\pi u\frac{x}{N}})$$
#### 2.2 Key Properties of the Fourier Transform

**Linearity, Scaling, Shifting, etc**

**Convolution Theorem**:

>Convolution in the spatial domain is equivalent to simple multiplication in the frequency domain. This property can significantly simplify filtering operations


$$G(u)=\int^{\infty}_{-\infty}g(x)e^{-2i\pi ux}dx$$

Convolution:

$$=\int^{\infty}_{-\infty}\int^{\infty}_{-\infty}f(\tau)h(x-\tau)e^{-2i\pi ux}d\tau dx$$

Remove:

$$=\int^{\infty}_{-\infty}\int^{\infty}_{-\infty}[f(\tau)e^{-2i\pi u\tau}d\tau][h(x-\tau)e^{-2i\pi u(x-\tau)}dx]$$

$$=\int^{\infty}_{-\infty}[f(\tau)e^{-2i\pi u\tau}d\tau]\int^{\infty}_{-\infty}[h(x')e^{-2i\pi ux'}dx']$$

$$=F(u)H(u)$$

**Invariance for Object Recognition**

**Rotation Invariance:** Rotating an object only changes the phase of the Fourier components, while the magnitude (spectrum) remains the same.

**Rotation Invariance:** Rotating an object only changes the phase of the Fourier components, while the magnitude (spectrum) remains the same.

**Noise Robustness:** Noise and quantization errors primarily affect high-frequency components. By ignoring these high frequencies, the descriptor remains robust.


### 3.2D Fourier Transform for Images

#### 3.1 2D DFT Definition

**Extension from 1D:** The transform is extended to two dimensions (u,v) to analyze images (x,y)

**Separability:** A 2D FFT can be efficiently computed as a series of 1D FFTs: first, transform every row of the image, and then transform every column of the resulting intermediate image.

#### 3.2 Amplitude vs. Phase in Images

**Importance of Phase:** Experiments show that most of the structural information of a natural image is carried in the **phase** information, not the amplitude. Reconstructing an image from phase alone yields a recognizable structure, while reconstruction from magnitude alone does not.

#### 3.3 Filtering in the Frequency Domain

**Low-Pass Filtering:** Keeping only the low frequencies (center of the spectrum) and eliminating high frequencies results in a blurred image, preserving the overall shading but losing sharp details.

**High-Pass Filtering:** Keeping only the high frequencies (outer parts of the spectrum) acts like an edge enhancer, preserving details and sharp transitions while removing the overall shape and shading