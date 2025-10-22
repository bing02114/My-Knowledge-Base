import cv2
import numpy as np
from matplotlib import pyplot as plt

try:
    image = cv2.imread('images/image.jpg', cv2.IMREAD_GRAYSCALE)
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

# 1.dft & idft

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = image.shape
crows, ccols = rows // 2, cols // 2
mask = np.ones((rows,cols,2),np.uint8)
mask[crows-30:crows+30, ccols-30:ccols+30] = 0

fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)

image_back = cv2.idft(f_ishift)
image_back = cv2.magnitude(image_back[:,:,0],image_back[:,:,1])
image_back = np.uint8(cv2.normalize(image_back, None, 0, 255, cv2.NORM_MINMAX))

display_image("Low-pass Filtered Image (FFT)", image_back)