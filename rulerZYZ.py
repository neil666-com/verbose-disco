#旋转矩阵转换为ZYZ形式
import numpy
import math
def ruler_zyz(matrix):
    r32=matrix[2][1]
    r31=matrix[2][0]
    r33=matrix[2][2]
    r23=matrix[1][2]
    r13=matrix[0][2]
    a=math.atan2(r32,-r31)
    b=math.acos(r33)
    c=math.atan2(r23,r13)
    if b==math.pi or b==0:
        print("万向锁问题会导致解不唯一")
    a = format(a, '.8f')
    b = format(b, '.8f')
    c = format(c, '.8f')
    zyz_ruler = [a, b, c]
    print("恢复的ZYZ欧拉角为：", zyz_ruler)
