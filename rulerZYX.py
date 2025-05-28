#旋转矩阵转换为ZXY形式
import numpy
import math
def ruler_xzy(matrix):
    r12=matrix[0][1]
    r11=matrix[0][0]
    r13=matrix[0][2]
    r23=matrix[1][2]
    r33=matrix[2][2]
    a=math.atan2(r12,r11)
    b=math.asin(-r13)
    c=math.atan2(r23,r33)
    a = format(a, '.8f')
    b = format(b, '.8f')
    c = format(c, '.8f')
    zxy_ruler = [a, b, c]
    print("恢复的zXY欧拉角为：", zxy_ruler)
