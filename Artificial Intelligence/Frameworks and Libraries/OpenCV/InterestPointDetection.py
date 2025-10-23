# # Import necessary libraries
# # 导入必要的库
# import cv2
# import numpy as np
#
# # --- 1. Load the Image ---
# # --- 1. 加载图像 ---
# image_path = 'images/image.jpg'
# try:
#     # Read the original image in color
#     # 读取原始的彩色图像
#     original_image = cv2.imread(image_path)
#     if original_image is None:
#         raise FileNotFoundError(f"Image not found at path: {image_path}")
#
#     # Create a grayscale version for the detector
#     # 创建一个灰度版本用于检测
#     gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
#
# except FileNotFoundError as e:
#     print(e)
#     print("Creating a dummy image for demonstration purposes.")
#     print("请确保在 'image' 文件夹中有名为 'image.jpg' 的图片。")
#     # Create a simple test image if the file is not found
#     # 如果找不到文件，则创建一个简单的测试图像
#     original_image = np.zeros((400, 600, 3), dtype=np.uint8)
#     cv2.rectangle(original_image, (100, 100), (250, 250), (255, 255, 255), -1)
#     cv2.rectangle(original_image, (250, 250), (400, 400), (200, 200, 200), -1)
#     cv2.line(original_image, (50, 50), (450, 350), (128, 0, 128), 5)
#     gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
#
# # --- 2. Apply the Harris Corner Detector ---
# # --- 2. 应用Harris角点检测器 ---
#
# # The Harris detector requires the input image to be in float32 format.
# # Harris检测器要求输入图像为float32格式。
# gray_image_float = np.float32(gray_image)
#
# # cv2.cornerHarris(image, blockSize, ksize, k)
# # image: Input image, should be grayscale and float32 type. (输入图像，应为灰度和float32类型。)
# # blockSize: The size of the neighborhood considered for corner detection. (用于角点检测的邻域大小。)
# # ksize: Aperture parameter for the Sobel operator used internally. (内部使用的Sobel算子的孔径参数，必须是奇数。)
# # k: Harris detector free parameter in the equation (R = det(M) - k * (trace(M))^2). (Harris检测器方程中的自由参数。)
# dst = cv2.cornerHarris(gray_image_float, blockSize=2, ksize=3, k=0.04)
#
# # --- 3. Visualize the Results ---
# # --- 3. 可视化结果 ---
#
# # To better visualize the corners, we can dilate the result. This makes the corner points larger.
# # 为了更好地可视化角点，我们可以对结果进行膨胀操作，这会使角点变得更大。
# dst = cv2.dilate(dst, None)
#
# # Threshold for an optimal value, it may vary depending on the image.
# # We will mark corners where the Harris response is greater than 1% of the maximum response.
# # 设置一个最佳阈值，该值可能因图像而异。
# # 我们将Harris响应值大于最大响应值1%的点标记为角点。
# threshold = 0.2 * dst.max()
# original_image[dst > threshold] = [0, 0, 255]  # Mark corners in red [B, G, R]
# # 用红色 [B, G, R] 标记角点
#
#
# # --- 4. Display the Images ---
# # --- 4. 显示图像 ---
#
# # Display the image with detected corners
# # 显示带有检测到角点的图像
# cv2.imshow('Harris Corners', original_image)
#
# # Wait for a key press to exit
# # 等待按键后退出
# print("Press any key to close the window.")
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#################################################

# import numpy as np
# import cv2
# import os
#
# # --- English ---
# # Define the path to the image.
# # --- 中文 ---
# # 定义图像的路径。
# image_path = os.path.join('images', 'image.jpg')
#
# # --- English ---
# # Load the image from disk.
# # --- 中文 ---
# # 从磁盘加载图像。
# img = cv2.imread(image_path)
#
# # --- English ---
# # Check if the image was loaded successfully.
# # --- 中文 ---
# # 检查图像是否成功加载。
# if img is None:
#     print(f"Error: Could not open or find the image at '{image_path}'")
#     print("Please make sure the 'images' folder exists and contains 'image.jpg'.")
# else:
#     # --- English ---
#     # Create a copy of the image to draw the detected corners on.
#     # --- 中文 ---
#     # 创建一个图像副本，用于在其上绘制检测到的角点。
#     img_with_corners = img.copy()
#
#     # --- English ---
#     # Convert the image to grayscale, as the detector works on single-channel images.
#     # --- 中文 ---
#     # 将图像转换为灰度图，因为检测器在单通道图像上工作。
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # --- English ---
#     # Use cv2.goodFeaturesToTrack to detect corners.
#     # Parameters:
#     #   - gray: The input grayscale image.
#     #   - 100: maxCorners - The maximum number of corners to return.
#     #   - 0.01: qualityLevel - Minimal accepted quality of corners (0-1).
#     #   - 10: minDistance - Minimum possible Euclidean distance between corners.
#     # --- 中文 ---
#     # 使用 cv2.goodFeaturesToTrack 函数来检测角点。
#     # 参数:
#     #   - gray: 输入的灰度图像。
#     #   - 100: maxCorners - 返回的角点最大数量。
#     #   - 0.01: qualityLevel - 可接受的角点最低质量水平 (0-1之间)。
#     #   - 10: minDistance - 返回的角点之间的最小欧几里得距离。
#     corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
#
#     # --- English ---
#     # The returned corners are in float32 format. Convert them to integers.
#     # --- 中文 ---
#     # 返回的角点是 float32 格式，需要将它们转换为整数。
#     corners = np.intp(corners)
#
#     # --- English ---
#     # Loop over the detected corners and draw a circle at each one's location.
#     # --- 中文 ---
#     # 遍历所有检测到的角点，并在每个角点的位置上画一个圆。
#     for i in corners:
#         x, y = i.ravel() # Flatten the array to get x and y coordinates
#         cv2.circle(img_with_corners, (x, y), 3, (0, 0, 255), -1) # Draw a red circle
#
#     # --- English ---
#     # Display the image with the detected corners.
#     # --- 中文 ---
#     # 显示带有检测到角点的图像。
#     cv2.imshow('Shi-Tomasi Corners', img_with_corners)
#
#     # --- English ---
#     # Wait for a key press to close the image window. Press 'ESC' to exit.
#     # --- 中文 ---
#     # 等待用户按键以关闭图像窗口。按 'ESC' 键退出。
#     if cv2.waitKey(0) & 0xff == 27:
#         cv2.destroyAllWindows()

import cv2
import numpy as np
import os

# --- English ---
# Define the path to the image. Make sure you have an image file here.
# For example, you can use the same 'building.jpg' from the previous example.
# --- 中文 ---
# 定义图像的路径。请确保此处有一个图像文件。
# 例如，您可以使用前面例子中的 'building.jpg'。
image_path = 'images/boat2.png'

# --- English ---
# Load the image from disk.
# --- 中文 ---
# 从磁盘加载图像。
img = cv2.imread(image_path)

# --- English ---
# Check if the image was loaded successfully.
# --- 中文 ---
# 检查图像是否成功加载。
if img is None:
    print(f"Error: Could not open or find the image at '{image_path}'")
else:
    # --- English ---
    # Convert the image to grayscale. SIFT works on single-channel images.
    # --- 中文 ---
    # 将图像转换为灰度图，因为SIFT在单通道图像上工作。
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # --- English ---
    # Create a SIFT object. This object will be used to detect keypoints and compute descriptors.
    # --- 中文 ---
    # 创建一个SIFT对象。这个对象将用于检测关键点和计算描述符。
    sift = cv2.SIFT_create()

    # --- English ---
    # Detect keypoints and compute their descriptors.
    # The detectAndCompute() function does both steps at once.
    # It returns:
    #   - keypoints: A list of KeyPoint objects. Each object contains information like position, size, angle, etc.
    #   - descriptors: A NumPy array of size (Number of Keypoints, 128). Each row is a 128-dimensional descriptor vector for a keypoint.
    # --- 中文 ---
    # 检测关键点并计算它们的描述符。
    # detectAndCompute() 函数会一次性完成这两个步骤。
    # 它返回:
    #   - keypoints: 一个KeyPoint对象的列表。每个对象包含位置、大小、角度等信息。
    #   - descriptors: 一个 NumPy 数组，形状为 (关键点数量, 128)。每一行都是对应关键点的128维描述符向量。
    keypoints, descriptors = sift.detectAndCompute(gray_img, None)

    # --- English ---
    # Draw the detected keypoints on the original color image.
    # cv2.drawKeypoints() is a utility function to visualize keypoints.
    # The flags cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensure that the circle size corresponds to the keypoint scale
    # and the line direction corresponds to its orientation.
    # --- 中文 ---
    # 在原始彩色图像上绘制检测到的关键点。
    # cv2.drawKeypoints() 是一个用于可视化关键点的辅助函数。
    # 参数 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS 能确保绘制的圆圈大小代表关键点的尺度，
    # 而线段方向则代表其主方向。
    img_with_keypoints = cv2.drawKeypoints(
        img,
        keypoints,
        None, # Output image, None means it modifies the input image copy internally
        flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
    )

    # --- English ---
    # Print the number of keypoints detected and the shape of the descriptors array.
    # --- 中文 ---
    # 打印检测到的关键点数量以及描述符数组的形状。
    print(f"Number of keypoints detected: {len(keypoints)}")
    print(f"Shape of descriptors array: {descriptors.shape}") # Should be (Number of keypoints, 128)

    # --- English ---
    # Display the image with the keypoints.
    # --- 中文 ---
    # 显示带有关键点的图像。
    cv2.imshow('SIFT Keypoints', img_with_keypoints)

    # --- English ---
    # Wait for a key press to close the window.
    # --- 中文 ---
    # 等待按键以关闭窗口。
    cv2.waitKey(0)
    cv2.destroyAllWindows()
