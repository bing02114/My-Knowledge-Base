### 1.Introduction

>A Convolutional Neural Network (CNN or ConvNet) is a class of deep neural networks, most commonly applied to analyzing visual imagery. They are inspired by the biological processes in the animal visual cortex, where individual neurons respond to stimuli only in a restricted region of the visual field known as the Receptive Field.

**Why use CNNs over standard Neural Networks for images**

**Parameter Sharing:** A feature detector (filter) that is useful in one part of the an image is likely to be useful in another part. This greatly reduces the total number of parameters

**Parameter Sharing:** A feature detector (filter) that is useful in one part of the an image is likely to be useful in another part. This greatly reduces the total number of parameters

**Translation Invariance:** The network learns to recognize patterns regardless of where they appear in the image

***
### 2.Core Components of a CNN

#### 2.1 Convolutional Layer

**Filter / Kernel**: 

A small matrix of weights that slides over the input data to produce a feature map.  The filter learns to detect specific features like edges

**Stride**

The number of pixels the filter moves over the input matrix at a time. A stride of 1 means moving one pixel at a time, while a stride of 2 means moving two pixels

**Padding**

Adding pixels (usually zeros) to the border of the input image. This is done to:

- Control the spatial size of the output feature map.
    
- Prevent the filter from losing information at the edges of the image.

**Feature Map**

The output of the convolution operation. It represents the presence of a specific feature in different spatial locations of the input.

#### 2.2 Activation Function

**ReLU**

$$f(x)=max(0,x)$$

#### 2.3 Pooling Layer

**Purpose**

* To reduce the number of parameters and computational complexity.
* To make the feature representations mode robust to small translations and distortions in the input

**Type of Pooling**

* **Max Pooling**: Selects the maximum value from the region covered by the pooling window. It is the most common type as it effectively captures the most prominent features
* **Avergae Pooling**: Calculates the average value of the region

#### 2.4 Fully Connected Layer

**Function**

The neurons in a fully connected layer have connections to all activations in the previous layer. Its purpose is to take the high-level features extracted by the convolutional and pooling layers and use them to classify the image

**Output**

The final FC layer usually has an output size equal to the number of classes and is often followed by a **Softmax** activation function to produce a probability distribution over the classes.

***
### 3.Extensions

#### 3.1 Grouped Convolution

#### 3.2 Depthwise Separable Convolution

#### 3.3 Dilated Convolution

#### 3.4 Transposed Convolution
