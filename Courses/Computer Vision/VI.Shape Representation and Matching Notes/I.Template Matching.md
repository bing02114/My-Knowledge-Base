
>Template matching is a fundamental technique for object recognition where the goal is to find the best match for a "template" image within a larger source image.


### 1.Method: Cross-Correlation

>The matching process is typically performed using cross-correlation, which systematically compares the template against all possible positions in the source image

The discrete formula for 2D cross-correlation is:

$$C(x,y)=\sum^{x_{res}}_{p=1}\sum^{y_{res}}_{q=1}f(p,q)h(p+x,q+y)$$

>The location (x,y) where the correlation function C(x,y) reaches its maximum value is considered the best match for the template's position

### 2.Cross-Correlation vs. Convolution

>The key difference is that in convolution, the kernel (template) is flipped before the sliding sum operation, whereas in cross-correlation, it is not flipped.

>If the kernel `h` is symmetric (i.e., h[i,j]=h[−i,−j]), then convolution and cross-correlation produce the same result.

### 3.Template Matching with Fourier Transform

>According to the convolution theorem, correlation in the spatial domain is equivalent to a pointwise multiplication in the frequency domain, where one of the functions is represented by its complex conjugate

The process involves:

- Computing the Fourier Transform (FT) of both the source image and the template.
    
- Taking the complex conjugate of the template's FT.
    
- Multiplying the two results.
    
- Performing an Inverse Fourier Transform on the product to get the correlation map.

>While theoretically sound, this method is rarely used in practice because the theory for continuous space does not generalize well to discrete pixel grids.

