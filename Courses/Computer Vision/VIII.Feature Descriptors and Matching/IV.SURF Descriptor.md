### 1.Detection

> It uses the determinant of a Hessian matrix to find points of interest across multiple scales. It achieves high speed by using integral images to approximate image convolutions

### 2.Description

* A window of sizw 20 * scale is divided inrto 4x4 subregions around the keypoint
* In each subregion, Haar wavelet responses are calculated for the x and y directions
* For values are summed for each subregion: $\sum d_x \sum d_y \sum |d_x| \sum |d_y|$
* This results in a 64-dimensional descriptor vector
