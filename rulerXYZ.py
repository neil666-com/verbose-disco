#输入任意旋转矩阵:输出对应三种转角系统下的欧拉角以及单位四元数;
#旋转矩阵转换为XYZ形式
import numpy
import math
def ruler_xyz(matrix):
    r32=matrix[2][1]
    r33=matrix[2][2]
    r11=matrix[0][0]
    r21=matrix[1][0]
    r31=matrix[2][0]
    a=math.atan2(r32,r33)
    b=math.asin(-r31)
    c=math.atan2(r21,r11)
    a=format(a,'.8f')
    b= format(b, '.8f')
    c = format(c, '.8f')
    if b==math.pi/2 or b==-math.pi/2:
        print("万向锁问题会导致解不唯一")
    xyz_ruler=[a,b,c]
    print("恢复的XYZ欧拉角为：",xyz_ruler)

