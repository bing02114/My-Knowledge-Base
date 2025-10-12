### 1.Elementary Noise Reduction

#### 1.1 Local Average:

>to make use of the redundancy of the data and replace the current pixel with the average of its neighbouring pixels

$$g(i,j)=\frac{1}{w}\sum_{(m,n)\in \Omega_{ij}}f(m,n)$$
Where:

* g(i,j) : Filtered image
	
* w: Normalisation Factor (number of pixels in the neighbourhood)
	
* $(m,n)\in \Omega_{ij}$ : For all pixels that belong to the neighbourhood of pixels (i,j)
	
* f(m,n): Original image

**Drawback:**

>This method tends to blur the image and compromises high-resolution details in order to remove noise

#### 1.2 Median Filtering

>rather than using arithmetic average, choose the median of the rank list for all pixels within the neighbourhood

$$g(i,j)=Median_{(m,n)\in \Omega_{ij}}f(m,n)$$
Where:

* **Median**: Rank all neighbouring pixels in ascending/descending order and choose the mid-ranked value
