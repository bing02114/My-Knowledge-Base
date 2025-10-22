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

_, thresh = cv2.threshold(image,127,255,cv2.THRESH_BINARY)

# 1.cv2.findContours
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_image = cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_image, contours, -1, (0,255,0), 2)

if contours:
    cnt = max(contours, key=cv2.contourArea)

    # 2.contourArea
    area = cv2.contourArea(cnt)
    print(f"最大轮廓面积: {area:.2f}")

    # 3.arcLength
    perimeter = cv2.arcLength(cnt,True)
    print(f"最大轮廓周长: {perimeter:.2f}")

    # 4.moments
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cx = int(M["m10"] / M["m00"])  # 计算质心x坐标
        cy = int(M["m01"] / M["m00"])  # 计算质心y坐标
        print(f"最大轮廓的质心 (Centroid): ({cx}, {cy})")
        # 在图上标记质心
        cv2.circle(contour_image, (cx, cy), 5, (0, 0, 255), -1)

# display_image("Contours and Centroid", contour_image)

# 假设你有一张 'image.jpg' 和一张更小的 'template.jpg'
try:
    img_gray = cv2.imread('image.jpg', 0)
    template = cv2.imread('template.jpg', 0)
    if img_gray is None or template is None:
        raise FileNotFoundError

    w, h = template.shape[::-1]

    # 执行模板匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 找到最佳匹配位置
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    # 在原图上绘制矩形框
    img_bgr = cv2.imread('image.jpg')
    cv2.rectangle(img_bgr, top_left, bottom_right, (0, 0, 255), 2)

    # display_image("Template Matching Result", cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))

except FileNotFoundError:
    print("\n跳过模板匹配示例，因为需要 'image.jpg' 和 'template.jpg'。")


# 3.Feature Point Matching
# 假设有两张图片，'image1.jpg' 和 'image2.jpg'
try:
    img1 = cv2.imread('image1.jpg', 0)
    img2 = cv2.imread('image2.jpg', 0)
    if img1 is None or img2 is None:
        raise FileNotFoundError

    # 1. cv2.ORB_create() - 创建ORB检测器
    orb = cv2.ORB_create()

    # 找到关键点和描述子
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # 2. cv2.BFMatcher_create() - 创建暴力匹配器
    bf = cv2.BFMatcher_create(cv2.NORM_HAMMING, crossCheck=True)

    # 匹配描述子
    matches = bf.match(des1, des2)

    # 根据距离排序
    matches = sorted(matches, key=lambda x: x.distance)

    # 3. 绘制前10个最佳匹配
    img_matches = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    display_image("Feature Matches", img_matches)

except FileNotFoundError:
    print("\n跳过特征匹配示例，因为需要 'image1.jpg' 和 'image2.jpg'。")