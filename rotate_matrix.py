import numpy as np
import math
def rotate_matrix(fai,w,k):
    ##计算旋转矩阵
    #fai = fai * math.pi / 180.0
   # w = w * math.pi / 180.0
   # k = k * math.pi / 180.0
    a1=math.cos(fai)*math.cos(k)-math.sin(fai)*math.sin(w)*math.sin(k)
    a2=-math.cos(fai)*math.sin(k)-math.sin(fai)*math.sin(w)*math.cos(k)
    a3=-math.sin(fai)*math.cos(w)
    b1=math.cos(w)*math.sin(k)
    b2=math.cos(w)*math.cos(k)
    b3=-math.sin(w)
    c1=math.sin(fai)*math.cos(k)+math.cos(fai)*math.sin(w)*math.sin(k)
    c2=-math.sin(fai)*math.sin(k)+math.cos(fai)*math.sin(w)*math.cos(k)
    c3=math.cos(fai)*math.cos(w)
    rotate_matrix_1=np.array([[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]])
    rotate_matrix_1=rotate_matrix_1.astype(np.float32)
    return rotate_matrix_1
