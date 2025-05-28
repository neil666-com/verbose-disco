import numpy as np
import collinearity_equation
import math
from collinearity_equation import calculate_space_forward_intersection
from rotate_matrix import rotate_matrix
from collinearity_equation import calculate_collinearity_equation
from eight_point_algorithm import calculate_eight_point_algorithm
from eight_point_algorithm import check_epistolary_constraint
##输入已知像点坐标
[[x1_left,y1_left],[x2_left,y2_left],[x3_left,y3_left],[x4_left,y4_left]]=[[16.012,79.963],[88.56,81.134],[13.362,-79.37],[82.24,-80.027]]
[[x1_right, y1_right], [x2_right, y2_right], [x3_right, y3_right], [x4_right, y4_right]] = [[-73.93, 78.706],[-5.252,78.184], [-79.122,-78.879], [-9.887,-80.089]]
matrix_left =np.array( [[x1_left, y1_left], [x2_left, y2_left], [x3_left, y3_left], [x4_left, y4_left]])
matrix_right=np.array([[x1_right, y1_right], [x2_right, y2_right], [x3_right, y3_right], [x4_right, y4_right]])
matrix_left=matrix_left.astype(np.float32)
matrix_right=matrix_right.astype(np.float32)
##输入内方位元素的值

x0=0
y0=0
#输入内方位元素的初值（相机的姿态）
fai_beg,w_beg,k_beg=float(0),float(0),float(0)##一般相片倾角小于3°所以外方位元素近似取φ，ω，κ=0
##输入左片和右片的外方位元素(xs_beg,ys_beg,zs_beg)
[[x1_ground,y1_ground,z1_ground],[x2_ground,y2_ground,z2_ground],[x3_ground,y3_ground,z3_ground],[x4_ground,y4_ground,z4_ground]]=[[5083.205,5852.099,527.925],[5780.02,5906.365,571.549],[5210.879,4258.446,461.81],[5909.264,4314.283,455.484]]
matrix_ground=np.array([[x1_ground,y1_ground,z1_ground],[x2_ground,y2_ground,z2_ground],[x3_ground,y3_ground,z3_ground],[x4_ground,y4_ground,z4_ground]])
matrix_ground=matrix_ground.astype(np.float32)

#xs_beg=(matrix_ground[0][0]+matrix_ground[1][0]+matrix_ground[2][0]+matrix_ground[3][0])/4.0##xs近似值取平均值
#ys_beg =(matrix_ground[0][1]+matrix_ground[1][1]+matrix_ground[2][1]+matrix_ground[3][1])/4.0##ys近似值取平均值
xs_beg=float(5000)
ys_beg=float(5000)
zs_begin=float(2000)##相机焦距乘以航摄比例尺
print("打印初始的xs，ys，zs")
print(xs_beg,ys_beg,zs_begin)
##八点法求解基础矩阵
array_left=np.array([[106,136],[180,163],[192,107],[192,107],[329,176],[330,179],[334,588],[374,466],[378,257],[378,496],[413,468],[424,492],[454,258],[468,208],[495,214],[560,164],[631,550],[650,530],[670,600],[677,600],[685,518],[692,527]])
array_right=np.array([[152,205],[190,213],[237,159],[237,159],[349,191],[349,193],[380,570],[335,461],[457,254],[295,488],[375,462],[341,485],[543,239],[462,194],[496,194],[612,115],[588,552],[614,531],[640,614],[650,615],[658,518],[666,530]])
array_left=array_left.astype(np.float64)
array_right=array_right.astype(np.float64)

def main():



##########空间后方交会###########
     xs_left,ys_left,zs_left,fai_left,w_left,k_left=calculate_collinearity_equation(xs_beg,ys_beg,zs_begin,fai_beg,w_beg,k_beg,0)
     xs_right,ys_right,zs_right,fai_right,w_right,k_right=calculate_collinearity_equation(xs_beg, ys_beg, zs_begin, fai_beg, w_beg, k_beg, 1)
#########################空间前方交会###############
     calculate_space_forward_intersection(xs_left,ys_left,zs_left,fai_left,w_left,k_left,xs_right,ys_right,zs_right,fai_right,w_right,k_right)
#####################八点法求解基本矩阵###################
     F=calculate_eight_point_algorithm(array_left,array_right)
     check_epistolary_constraint(F,array_left,array_right)
















if __name__ == "__main__":
    main()

