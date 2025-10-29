* Real lenses, especially wide-angle ones, cause straight lines in the world to appear curved in the image

### 1.Type of Distortion

* **Barrel Distortion**: Points are displaced away from the image center
* **Pincushion Distoriton**: oints are displaced towards the image cente

### 2.Correction Model

* It can be modeled using a low-order polynomial. Distorted coordinates (xd​,yd​) are calculated from ideal normalized coordinates (xn​,yn​)

$$x_d=x_n(1+k_1 r^2 + k_2r^4)$$

$$y_d=y_n(1+k_1r^2+k_2r^4)$$

where $r^2=x_n^2+y_n^2$ and $k_1,k_2$ are distortion coefficients