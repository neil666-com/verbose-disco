#旋转矩阵转换为四元数形式
import numpy
import math
def unit_quaternions(matrix):
    r11=matrix[0][0]
    r22=matrix[1][1]
    r33=matrix[2][2]
    r32=matrix[2][1]
    r23=matrix[1][2]
    r13=matrix[0][2]
    r31=matrix[2][0]
    r21=matrix[1][0]
    r12=matrix[0][1]
    w=math.sqrt(1+r11+r22+r33)/2
    x=(r32-r23)/(4*w)
    y=(r13-r31)/(4*w)
    z=(r21-r12)/(4*w)
    w= format(w, '.8f')
    x = format(x, '.8f')
    y= format(y, '.8f')
    z = format(z, '.8f')
    unit_quaternions_1 = [w,x,y,z]
    print("单位四元数为",unit_quaternions_1)
    start=input("是否需要将四元数转换为旋转矩阵验证结果的准确性，是请输入1，否请输入2：")
    if start=="1":
        w=float(w)
        x= float(x)
        y= float(y)
        z=float(z)
        r11_after=1-2*y*y-2*z*z
        r12_after=2*y*x-2*w*z
        r13_after=2*x*z+2*w*y
        r21_after=2*x*y+2*w*z
        r22_after=1-2*x*x-2*z*z
        r23_after=2*y*z-2*w*x
        r31_after=2*x*z-2*w*y
        r32_after=2*y*z+2*w*x
        r33_after=1-2*x*x-2*y*y
        r11_after= format(r11_after, '.8f')
        r12_after= format(r12_after, '.8f')
        r13_after= format(r13_after, '.8f')
        r21_after= format(r21_after, '.8f')
        r22_after = format(r22_after, '.8f')
        r23_after = format(r23_after, '.8f')
        r31_after = format(r31_after, '.8f')
        r32_after = format(r32_after, '.8f')
        r33_after = format(r33_after, '.8f')
        r_rotate=[[r11_after,r12_after,r13_after],[r21_after,r22_after,r23_after],[r31_after,r32_after,r33_after]]
        print(r_rotate)





