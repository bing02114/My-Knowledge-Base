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

# 1.Sobel
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)

sobel_combined = cv2.magnitude(sobel_x, sobel_y)
sobel_combined = np.uint8(sobel_combined)

# display_image("Sobel Edge Detection", sobel_combined)

# 2.Laplacian
laplacian = cv2.Laplacian(image,cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# display_image("Laplacian Edge Detection", laplacian)

# 3.Canny
canny_edges = cv2.Canny(image, 100, 200)
display_image("Canny Edge Detection", canny_edges)

