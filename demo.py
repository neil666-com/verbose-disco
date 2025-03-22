import numpy as np
import matplotlib.pyplot as plt
# 设置字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 更换为支持中文等字符的字体，如黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

class KalmanFilter:
    def __init__(self, Q=0.01, R=0.1):
        # 过程噪声协方差
        self.Q = Q
        # 测量噪声协方差
        self.R = R
        # 状态估计值
        self.x = 0
        # 估计误差协方差
        self.P = 1

    def update(self, measurement):
        # 预测步骤
        # 预测状态估计值（这里假设状态转移矩阵为 1，即状态不变）
        self.x = self.x
        # 预测估计误差协方差
        self.P = self.P + self.Q

        # 更新步骤
        # 计算卡尔曼增益
        K = self.P / (self.P + self.R)
        # 更新状态估计值
        self.x = self.x + K * (measurement - self.x)
        # 更新估计误差协方差
        self.P = (1 - K) * self.P

        return self.x


# 生成模拟数据
np.random.seed(0)
true_values = np.linspace(0, 10, 100)
measurements = true_values + np.random.normal(0, 1, 100)

# 创建卡尔曼滤波器实例
kf = KalmanFilter()

# 进行滤波
filtered_values = []
for measurement in measurements:
    filtered_value = kf.update(measurement)
    filtered_values.append(filtered_value)

# 绘制结果
plt.figure(figsize=(10, 6))
plt.plot(true_values, label='真实值')
plt.plot(measurements, label='测量值', alpha=0.5)
plt.plot(filtered_values, label='滤波后的值', color='r')
plt.legend()
plt.xlabel('时间步')
plt.ylabel('值')
plt.title('卡尔曼滤波示例')
plt.show()
