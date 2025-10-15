import numpy as np
from sklearn.linear_model import LinearRegression

# 1. 创建一些示例数据
X = np.array([[1], [2], [3], [4], [5]]) # 特征 (例如，工作年限)
y = np.array([3, 5, 7, 9, 11])        # 目标 (例如，薪水，单位：万)

# 2. 实例化并拟合模型
model = LinearRegression()
model.fit(X, y)

# 3. 查看学习到的参数
print(f"系数 (w): {model.coef_}")
print(f"截距 (b): {model.intercept_}")
# 期望输出: 系数 (w): [2.], 截距 (b): 1.0
# 这意味着模型学习到了关系 y = 2x + 1

# 4. 对新数据点进行预测
new_X = np.array([[6]])
prediction = model.predict(new_X)
print(f"对X=6的预测: {prediction}")
# 期望输出: 对X=6的预测: [13.]

# 5. 评估模型
print(f"R-squared 分数: {model.score(X, y)}")
# 期望输出: R-squared 分数: 1.0 (对于这个简单数据是完美拟合)