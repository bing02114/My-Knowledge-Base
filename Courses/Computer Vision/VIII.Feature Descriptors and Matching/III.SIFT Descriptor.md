### 1.Scale-space Extrema Detection

>Detects keypoints using Difference-of-Gaussian filters

### 2.Keypoint Localization

>Refines the location and scale of keypoints and filters out unstable ones

### 3.Orientation Estimation

>Assigns an orientation to each keypoint based on local image gradients to achieve rotation invariance. This is done by creating a histogram of gradient orientations from the keypoint's neighborhood and finding the peak

### 4.Keypoint Descriptor Generation

* A 16x16 window is taken around the keypoint
* This window is divided into a 4x4 grid of cells
* For each cell, an 8-bin orientation histogram of the gradients is created
* The 16 histograms are concatenated to form a 128-dimensional descriptor vector