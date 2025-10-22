import cv2
import numpy as np
from matplotlib import pyplot as plt

try:
    image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise FileNotFoundError

except FileNotFoundError:
    print("未找到图像，创建测试图像")
    image = np.zeros((300, 400), dtype=np.uint8)
    cv2.rectangle(image, (50, 50), (150, 150), 255, -1)
    cv2.circle(image, (250, 150), 60, 128, -1)

def display_image(title,img):
    plt.imshow(img,cmap='gray')
    plt.title(title)
    plt.xticks([]), plt.yticks([])
    plt.show()

display_image("Original Image", image)

# 1.filter2D

kernel_sharpen = np.array([[-1,-1,-1],
                          [-1, 9,-1],
                          [-1,-1,-1]])
sharpen_image = cv2.filter2D(image, -1, kernel_sharpen)
# display_image("Sharpen Image (filter2D)", sharpen_image)

# 2.blur

blurred_image = cv2.blur(image,(5,5))
# display_image("Averaging Blur (blur)", blurred_image)

# 3.GaussianBlur

gaussian_blurred_image = cv2.GaussianBlur(image, (5,5), 0)
# display_image("Gaussian Blur", gaussian_blurred_image)

# 4.medianBlur

noisy_image = image.copy()
noise = np.zeros(noisy_image.shape, np.uint8)
cv2.randu(noise, 0, 255)
noisy_image[noise < 10] = 0
noisy_image[noise > 245] = 255

median_filtered_image = cv2.medianBlur(noisy_image, 5)
# display_image("Noisy Image",noisy_image)
# display_image("Median Filtered", median_filtered_image)

# 5.bilateralFilter

bilateral_filtered_image = cv2.bilateralFilter(image,9,75,75)
display_image("Bilateral Filter", bilateral_filtered_image)