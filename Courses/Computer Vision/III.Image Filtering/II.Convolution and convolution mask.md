### 1.Convolution and Convolution Masks

#### 1.1 Continuous

$$g(x)=\int^{\infty}_{-\infty}f(u)h(x-u)du$$

Where:

* g(x):  Filtered Signal
* f(u):  Original Signal
* h(x-u):  Convolution Mask

$$g(x,y)=\int^{\infty}_{-\infty}\int^{\infty}_{-\infty}f(u,v)h(x-u,y-v)dudv$$

Where:

* h(x-u,y-v): Convolution mask also called a filter

#### 1.2 Discrete

$$g(i,j)=\sum \sum_{(m,n)\in \Omega_{ij}}f(m,n)h(i-m,j-n)$$
* Usually the convolution kernel only has non-zero value in a small neighbourhood, and therefore is also called a convolution mask. Rectangular neighbourhoods are often used with an odd number of pixels in rows and columns, enabling the specification of the central pixel of the neighbourhood.
	
*  The local average process mentioned in the previous section can then be expressed in terms of convolution of the original image with mask:

$$\frac{1}{9}\left[\begin{matrix}
1 & 1 & 1 \\
1 & 1 & 1 \\
1 & 1 & 1 \\
\end{matrix}
\right]$$


### 2.Properties of Convolution

**Commutativity**

$$f * h = h * f$$

**Associativity**

$$f * (g * h) = (f * g) * h$$

**Distributivity**

$$f * (g + h) = (f*g)+(f*h)$$

**Differentiation**

$$\frac{d}{dx}(f*g)=\frac{df}{dx}*g=f\frac{dg}{dx}$$


### 3.Computational Complexity

#### 3.1 Calculation

* Image size : NxN
* Kernal size : KxK
* **Complexity**: $O(N^{2}K^{2})$

#### 3.2 Accelerate

**Separable Filter**

$$f*(g*h)=(f*g)*h$$

* If a big filter can be separated as the convolution of two small filters, such as g * h, then we can first convolve the image f with g, then with h

* $2N^{2}K$ multiplications and $2N^{2}(K-1)$ summations

* Complexity: $O(N^{2}K)$

* It makes a difference if K is large

