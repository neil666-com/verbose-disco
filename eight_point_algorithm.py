import math

import numpy as np

def calculate_eight_point_algorithm(array_left,array_right):
    print("下面为八点法求解基础矩阵的结果")
    ###坐标归一化
    rows_left,cols_left=array_left.shape
    print(rows_left,cols_left)
    rows_right,cols_right=array_right.shape
    print(rows_right,cols_right)
    sum_x_left=0
    sum_y_left=0
    sum_x_right=0
    sum_y_right=0
    mean_left=0
    mean_right=0
    for i in range(0,rows_left,1):
        sum_x_left+=array_left[i][0]
        sum_y_left+=array_left[i][1]
    x_bar_left=sum_x_left/rows_left
    y_bar_left=sum_y_left/rows_left
    print(f"左图像质心: ({x_bar_left}, {y_bar_left})")
    for i in range(0,rows_right,1):
        sum_x_right+=array_right[i][0]
        sum_y_right+=array_right[i][1]
    x_bar_right=sum_x_right/rows_right
    y_bar_right=sum_y_right/rows_right
    print(f"右图像质心: ({x_bar_right}, {y_bar_right})")
    squared_norms_left=0
    squared_norms_right=0

    # 计算平移后的坐标（不修改原始数组）
    translated_left = array_left - [x_bar_left, y_bar_left]
    translated_right = array_right - [x_bar_right, y_bar_right]

    # 修正缩放因子计算：计算每个点的平方和再取均值
    for i in range (0,rows_left,1):
        squared_norms_left+=translated_left[i][0]**2+translated_left[i][1]**2
    squared_norms_left=math.sqrt(squared_norms_left/rows_left)
    s_left=math.sqrt(2)/squared_norms_left
    for i in range (0,rows_right,1):
        squared_norms_right+=translated_right[i][0]**2+translated_right[i][1]**2
    squared_norms_right=math.sqrt(squared_norms_right/rows_right)
    s_right=math.sqrt(2)/squared_norms_right




    # print("左边图像点中心化后的坐标",array_left)
    # print("右边图像点中心化后的坐标", array_right)


    # 构造归一化矩阵（左边）
    T_left = np.array([
        [s_left, 0, -s_left * x_bar_left],
        [0, s_left, -s_left * y_bar_left],
        [0, 0, 1]
    ])
    T_right = np.array([
        [s_right, 0, -s_right * x_bar_right],
        [0, s_right, -s_right * y_bar_right],
        [0, 0, 1]
    ])
    # 归一化坐标
    normalized_left = np.dot(T_left, np.vstack((array_left.T, np.ones(rows_left)))).T[:, :2]
    normalized_right = np.dot(T_right, np.vstack((array_right.T, np.ones(rows_right)))).T[:, :2]
    # 构建约束方程矩阵 A
    A = np.zeros((rows_left, 9))
    for i in range(rows_left):
        x1, y1 = normalized_left[i]
        x2, y2 = normalized_right[i]
        A[i] = [x2 * x1, x2 * y1, x2, y2 * x1, y2 * y1, y2, x1, y1, 1]
        # 使用 SVD 求解基础矩阵
    U, S, Vt = np.linalg.svd(A)
    F = Vt[-1].reshape(3, 3)

    # 强制基础矩阵的秩为 2
    U, S, Vt = np.linalg.svd(F)
    S[2] = 0
    F = np.dot(U, np.dot(np.diag(S), Vt))

    # 反归一化基础矩阵
    F = np.dot(T_right.T, np.dot(F, T_left))
    det_F=np.linalg.det(F)
    print(f"基础矩阵的行列式为det={det_F}")


    print("基础矩阵 F:")
    print(F)
    return F


def check_epistolary_constraint(F, points_left, points_right):
    errors = []
    for x1, x2 in zip(points_left, points_right):
        x1_homo = np.append(x1, 1)  # Convert to homogeneous coordinates
        x2_homo = np.append(x2, 1)
        error = np.abs(x2_homo.T @ F @ x1_homo)
        errors.append(error)
    print("计算所有匹配点通过基础矩阵重投影后的误差")
    print(errors)


















