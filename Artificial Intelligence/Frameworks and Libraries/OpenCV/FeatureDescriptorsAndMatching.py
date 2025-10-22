# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# # --- English ---
# # Load the two images.
# # --- 中文 ---
# # 加载两张图片。
# img1_bgr = cv2.imread('images/image1.jpg') # Load color image for display
# img2_bgr = cv2.imread('images/image2.jpg') # Load color image for display
#
# if img1_bgr is None or img2_bgr is None:
#     print("Error: Could not load one or both images.")
# else:
#     # --- English ---
#     # Convert to grayscale for feature detection
#     # --- 中文 ---
#     # 转换为灰度图以进行特征检测
#     img1_gray = cv2.cvtColor(img1_bgr, cv2.COLOR_BGR2GRAY)
#     img2_gray = cv2.cvtColor(img2_bgr, cv2.COLOR_BGR2GRAY)
#
#     # 1. Initialize the SIFT detector.
#     sift = cv2.SIFT_create()
#
#     # 2. Find the keypoints and descriptors with SIFT for both images.
#     kp1, des1 = sift.detectAndCompute(img1_gray, None)
#     kp2, des2 = sift.detectAndCompute(img2_gray, None)
#
#     # 3. Create a BFMatcher object with cross-checking.
#     bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
#
#     # 4. Match the descriptors.
#     matches = bf.match(des1, des2)
#
#     # 5. Sort the matches by distance.
#     matches = sorted(matches, key=lambda x: x.distance)
#
#     # --- English ---
#     # 6. Draw the first 50 matches.
#     #    Note: We need to use the original color images for drawing.
#     # --- 中文 ---
#     # 6. 绘制前50个匹配结果。
#     #    注意：我们需要使用原始的彩色图像进行绘制。
#     img_matches = cv2.drawMatches(img1_bgr, kp1, img2_bgr, kp2, matches[:50], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
#
#     # --- English ---
#     # 7. Display the result using Matplotlib.
#     #    cv2.drawMatches creates a BGR image, so we need to convert it to RGB for Matplotlib.
#     # --- 中文 ---
#     # 7. 使用Matplotlib显示结果。
#     #    cv2.drawMatches创建的是BGR图像，因此我们需要将其转换为RGB以供Matplotlib使用。
#     plt.figure(figsize=(20, 10)) # English: Create a large figure to display the result / 中文: 创建一个大窗口来显示结果
#     plt.imshow(cv2.cvtColor(img_matches, cv2.COLOR_BGR2RGB))
#     plt.title('BFMatcher - Simple Matches')
#     plt.axis('off') # English: Hide the axes / 中文: 隐藏坐标轴
#     plt.show()


#################################
import cv2
import numpy as np
import matplotlib.pyplot as plt

# --- English ---
# Load the two images.
# --- 中文 ---
# 加载两张图片。
img1_bgr = cv2.imread('images/image1.jpg') # Load color image
img2_bgr = cv2.imread('images/image.jpg') # Load color image

if img1_bgr is None or img2_bgr is None:
    print("Error: Could not load one or both images.")
else:
    # --- English ---
    # Convert to grayscale for feature detection
    # --- 中文 ---
    # 转换为灰度图以进行特征检测
    img1_gray = cv2.cvtColor(img1_bgr, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2_bgr, cv2.COLOR_BGR2GRAY)

    # 1. Initialize the SIFT detector.
    sift = cv2.SIFT_create()

    # 2. Find the keypoints and descriptors with SIFT.
    kp1, des1 = sift.detectAndCompute(img1_gray, None)
    kp2, des2 = sift.detectAndCompute(img2_gray, None)

    # 3. Create a BFMatcher object.
    bf = cv2.BFMatcher(cv2.NORM_L2)

    # 4. Find the 2 nearest neighbors for each descriptor.
    matches = bf.knnMatch(des1, des2, k=2)

    # 5. Apply Lowe's Ratio Test (NNDR).
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    # --- English ---
    # 6. Draw the good matches.
    # --- 中文 ---
    # 6. 绘制好的匹配结果。
    img_matches_nndr = cv2.drawMatches(img1_bgr, kp1, img2_bgr, kp2, good_matches, None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    # --- English ---
    # 7. Display the result using Matplotlib.
    #    Convert the final BGR image to RGB for correct color display.
    # --- 中文 ---
    # 7. 使用Matplotlib显示结果。
    #    将最终的BGR图像转换为RGB以正确显示颜色。
    plt.figure(figsize=(20, 10)) # English: Make the window large enough / 中文: 让窗口足够大
    plt.imshow(cv2.cvtColor(img_matches_nndr, cv2.COLOR_BGR2RGB))
    plt.title('BFMatcher - NNDR Matches')
    plt.axis('off')
    plt.show()