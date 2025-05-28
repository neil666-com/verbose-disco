import numpy as np
import math
from rotate_matrix import rotate_matrix
##输入内方位元素的值
f=150
x0=0
y0=0
##输入已知像点坐标
[[x1_left,y1_left],[x2_left,y2_left],[x3_left,y3_left],[x4_left,y4_left]]=[[16.012,79.963],[88.56,81.134],[13.362,-79.37],[82.24,-80.027]]
[[x1_right, y1_right], [x2_right, y2_right], [x3_right, y3_right], [x4_right, y4_right]] = [[-73.93, 78.706],[-5.252,78.184], [-79.122,-78.879], [-9.887,-80.089]]
matrix_left =np.array( [[x1_left, y1_left], [x2_left, y2_left], [x3_left, y3_left], [x4_left, y4_left]])
matrix_right=np.array([[x1_right, y1_right], [x2_right, y2_right], [x3_right, y3_right], [x4_right, y4_right]])
matrix_left=matrix_left.astype(np.float64)

print("###################")
print(matrix_left)
print(matrix_right)
matrix_right=matrix_right.astype(np.float64)

##输入左片和右片的外方位元素(xs_beg,ys_beg,zs_beg)
[[x1_ground,y1_ground,z1_ground],[x2_ground,y2_ground,z2_ground],[x3_ground,y3_ground,z3_ground],[x4_ground,y4_ground,z4_ground]]=[[5083.205,5852.099,527.925],[5780.02,5906.365,571.549],[5210.879,4258.446,461.81],[5909.264,4314.283,455.484]]
matrix_ground=np.array([[x1_ground,y1_ground,z1_ground],[x2_ground,y2_ground,z2_ground],[x3_ground,y3_ground,z3_ground],[x4_ground,y4_ground,z4_ground]])
matrix_ground=matrix_ground.astype(np.float64)
print(matrix_ground)
deta=float(10*math.pi/(3600*180))
number = 0
number1=0
deta=float(10/3600)*float(np.pi/180)
##############前方交会实验数据####################
[[forward_left_x1,forward_left_y1],[forward_left_x2,forward_left_y2],[forward_left_x3,forward_left_y3],[forward_left_x4,forward_left_y4],[forward_left_x5,forward_left_y5]]=[[51.758,80.555],[14.618,-0.231],[49.88,-0.782],[86.14,-1.346],[48.035,-79.962]]
[[forward_right_x1,forward_right_y1],[forward_right_x2,forward_right_y2],[forward_right_x3,forward_right_y3],[forward_right_x4,forward_right_y4],[forward_right_x5,forward_right_y5]]=[[-39.953,78.463],[-70.006,0.036],[-42.201,-1.022],[-7.706,-2.112],[-44.438,-79.736]]
matrix_forward_left=np.array([[forward_left_x1,forward_left_y1],[forward_left_x2,forward_left_y2],[forward_left_x3,forward_left_y3],[forward_left_x4,forward_left_y4],[forward_left_x5,forward_left_y5]])
matrix_forward_left=matrix_forward_left.astype(np.float64)
matrix_forward_right=np.array([[forward_right_x1,forward_right_y1],[forward_right_x2,forward_right_y2],[forward_right_x3,forward_right_y3],[forward_right_x4,forward_right_y4],[forward_right_x5,forward_right_y5]])
matrix_forward_right=matrix_forward_right.astype(np.float64)
def calculate_collinearity_equation(xs, ys, zs, fai, w, k, j):
    if j == 0:
        print("#####################空间后方交会###############################")
        global number
        max_iter = 4000
        for _ in range(max_iter):
            r_matrix = rotate_matrix(fai, w, k)
            # print(r_matrix)
            a1 = r_matrix[0][0]
            a2 = r_matrix[0][1]
            a3 = r_matrix[0][2]
            b1 = r_matrix[1][0]
            b2 = r_matrix[1][1]
            b3 = r_matrix[1][2]
            c1 = r_matrix[2][0]
            c2 = r_matrix[2][1]
            c3 = r_matrix[2][2]
            # print(a1, a2, a3, b1, b2, b3, c1, c2, c3)
            matrix_xy_calc = np.zeros((4, 2), dtype=float)
            matrix_a = np.zeros((8, 6))
            matrix_lxy_calc = np.zeros(8, dtype=float)
            for i in range(0, 4, 1):
                X = matrix_ground[i][0]
                Y = matrix_ground[i][1]
                Z = matrix_ground[i][2]
                ## 计算偏导矩阵
                x_ba = a1 * (X - xs) + b1 * (Y - ys) + c1 * (Z - zs)
                y_ba = a2 * (X - xs) + b2 * (Y - ys) + c2 * (Z - zs)
                z_ba = a3 * (X - xs) + b3 * (Y - ys) + c3 * (Z - zs)
                x_img = -f * (x_ba / z_ba)
                y_img = -f * (y_ba / z_ba)
                # print(x_img, y_img)
                a11 = (a1 * f + a3 * x_img) / z_ba
                a12 = (b1 * f + b3 * x_img) / z_ba
                a13 = (c1 * f + c3 * x_img) / z_ba
                a14 = y_img * math.sin(w) - ((x_img / f) * (x_img * math.cos(k) - y_img * math.sin(k)) + f * math.cos(k)) * math.cos(w)
                a15 = -f * math.sin(k) - (x_img / f) * (x_img * math.sin(k) + y_img * math.cos(k))
                a16 = y_img
                a21 = (a2 * f + a3 * y_img) / z_ba
                a22 = (b2 * f + b3 * y_img) / z_ba
                a23 = (c2 * f + c3 * y_img) / z_ba
                a24 = -x_img * math.sin(w) - ((y_img / f) * (x_img * math.cos(k) - y_img * math.sin(k)) - f * math.sin(k)) * math.cos(w)
                a25 = -f * math.cos(k) - (y_img / f) * (x_img * math.sin(k) + y_img * math.cos(k))
                a26 = -x_img
                # 得到偏导数矩阵
                matrix_a[2 * i][0] = a11
                matrix_a[2 * i][1] = a12
                matrix_a[2 * i][2] = a13
                matrix_a[2 * i][3] = a14
                matrix_a[2 * i][4] = a15
                matrix_a[2 * i][5] = a16
                matrix_a[2 * i + 1][0] = a21
                matrix_a[2 * i + 1][1] = a22
                matrix_a[2 * i + 1][2] = a23
                matrix_a[2 * i + 1][3] = a24
                matrix_a[2 * i + 1][4] = a25
                matrix_a[2 * i + 1][5] = a26
                ## 计算常数项矩阵
                [x_left, y_left] = matrix_left[i]
                matrix_lxy_calc[2 * i] = x_left - x_img
                matrix_lxy_calc[2 * i + 1] = y_left - y_img
            matrix_b = np.dot(matrix_a.T, matrix_a)
            matrix_f = np.dot(matrix_a.T, matrix_lxy_calc)
            matrix_b_ni = np.linalg.inv(matrix_b)
            x = np.dot(matrix_b_ni, matrix_f)
            # 更新外方位元素的值
            xs = xs + x[0]
            ys = ys + x[1]
            zs = zs + x[2]
            fai = fai + x[3]
            w = w + x[4]
            k = k + x[5]
            # print(matrix_a)
            # print("###################")
            # print(matrix_lxy_calc)
            # print("##########################")
            # print(x)
            number += 1
            if abs(x[0] * 0.001) < 1e-6 and abs(x[1] * 0.001) < 1e-6 and abs(x[2] * 0.001) < 1e-6 and (x[3]) < deta and (x[4]) < deta and (x[5]) < deta:
                break
        print("##############左片最终结果#################")
        print("##############迭代次数#######################")
        print(number)
        print("##############外方位元素######################")
        print(xs, ys, zs, fai, w, k)
        v=np.dot(matrix_a,x)+matrix_lxy_calc
        error=math.sqrt(np.dot(v.T,v)/2)
        d=error*error*matrix_b_ni
        print("################方差协方差矩阵##############################")
        #print(d)
        print("#################左片外方位元素的精度######################################")
        for q in range(0, 6, 1):
            error_every = d[q][q]
            error_every_real = math.sqrt(error_every)
            if q==3 or q==4 or q==5:
                error_every_real=error_every_real*(180/np.pi)*3600
            print(error_every_real)

    if j==1:
        global number1
        max_iter = 4000
        for _ in range(max_iter):
            r_matrix = rotate_matrix(fai, w, k)
            # print(r_matrix)
            a1 = r_matrix[0][0]
            a2 = r_matrix[0][1]
            a3 = r_matrix[0][2]
            b1 = r_matrix[1][0]
            b2 = r_matrix[1][1]
            b3 = r_matrix[1][2]
            c1 = r_matrix[2][0]
            c2 = r_matrix[2][1]
            c3 = r_matrix[2][2]
            # print(a1, a2, a3, b1, b2, b3, c1, c2, c3)
            matrix_xy_calc = np.zeros((4, 2), dtype=float)
            matrix_a = np.zeros((8, 6))
            matrix_lxy_calc = np.zeros(8, dtype=float)
            for i in range(0, 4, 1):
                X = matrix_ground[i][0]
                Y = matrix_ground[i][1]
                Z = matrix_ground[i][2]
                ## 计算偏导矩阵
                x_ba = a1 * (X - xs) + b1 * (Y - ys) + c1 * (Z - zs)
                y_ba = a2 * (X - xs) + b2 * (Y - ys) + c2 * (Z - zs)
                z_ba = a3 * (X - xs) + b3 * (Y - ys) + c3 * (Z - zs)
                x_img = -f * (x_ba / z_ba)
                y_img = -f * (y_ba / z_ba)
                # print(x_img, y_img)
                a11 = (a1 * f + a3 * x_img) / z_ba
                a12 = (b1 * f + b3 * x_img) / z_ba
                a13 = (c1 * f + c3 * x_img) / z_ba
                a14 = y_img * math.sin(w) - (
                            (x_img / f) * (x_img * math.cos(k) - y_img * math.sin(k)) + f * math.cos(k)) * math.cos(w)
                a15 = -f * math.sin(k) - (x_img / f) * (x_img * math.sin(k) + y_img * math.cos(k))
                a16 = y_img
                a21 = (a2 * f + a3 * y_img) / z_ba
                a22 = (b2 * f + b3 * y_img) / z_ba
                a23 = (c2 * f + c3 * y_img) / z_ba
                a24 = -x_img * math.sin(w) - (
                            (y_img / f) * (x_img * math.cos(k) - y_img * math.sin(k)) - f * math.sin(k)) * math.cos(w)
                a25 = -f * math.cos(k) - (y_img / f) * (x_img * math.sin(k) + y_img * math.cos(k))
                a26 = -x_img
                # 得到偏导数矩阵
                matrix_a[2 * i][0] = a11
                matrix_a[2 * i][1] = a12
                matrix_a[2 * i][2] = a13
                matrix_a[2 * i][3] = a14
                matrix_a[2 * i][4] = a15
                matrix_a[2 * i][5] = a16
                matrix_a[2 * i + 1][0] = a21
                matrix_a[2 * i + 1][1] = a22
                matrix_a[2 * i + 1][2] = a23
                matrix_a[2 * i + 1][3] = a24
                matrix_a[2 * i + 1][4] = a25
                matrix_a[2 * i + 1][5] = a26
                ## 计算常数项矩阵
                [x_right, y_right] = matrix_right[i]
                matrix_lxy_calc[2 * i] = x_right - x_img
                matrix_lxy_calc[2 * i + 1] = y_right - y_img
            matrix_b = np.dot(matrix_a.T, matrix_a)
            matrix_f = np.dot(matrix_a.T, matrix_lxy_calc)
            matrix_b_ni = np.linalg.inv(matrix_b)
            x = np.dot(matrix_b_ni, matrix_f)
            # 更新外方位元素的值
            xs = xs + x[0]
            ys = ys + x[1]
            zs = zs + x[2]
            fai = fai + x[3]
            w = w + x[4]
            k = k + x[5]
            # print(matrix_a)
            # print("###################")
            # print(matrix_lxy_calc)
            # print("##########################")
            # print(x)
            number1 += 1
            if abs(x[0] * 0.001) < 1e-6 and abs(x[1] * 0.001) < 1e-6 and abs(x[2] * 0.001) < 1e-6 and (
            x[3]) < deta and (x[4]) < deta and (x[5]) < deta:
                break
        print("##############右片最终结果#################")
        print("##############迭代次数：#######################")
        print(number1)
        print("##############外方位元素：######################")
        print(xs, ys, zs, fai, w, k)
        v = np.dot(matrix_a, x) + matrix_lxy_calc
        error = math.sqrt(np.dot(v.T, v) / 2)
        d = error * error * matrix_b_ni
        print("################方差协方差矩阵##############################")
        #print(d)
        print("#################右片外方位元素的精度######################################")
        for q in range(0,6,1):
            error_every=d[q][q]
            error_every_real=math.sqrt(error_every)
            if q==3 or q==4 or q==5:
                error_every_real=error_every_real*(180/np.pi)*3600
            print(error_every_real)
    return xs,ys,zs,fai,w,k




def calculate_space_forward_intersection(xs_left,ys_left,zs_left,fai_left,w_left,k_left,xs_right,ys_right,zs_right,fai_right,w_right,k_right):
    ##############空间前方交会################
    print("############################空间前方交会#######################################")
    print("下面是前方交会输出的结果")
    matrix_r1 = rotate_matrix(fai_left, w_left, k_left)
    matrix_r2 = rotate_matrix(fai_right, w_right, k_right)
    ###计算摄影基线
    bu=xs_right-xs_left
    bv=ys_right-ys_left
    bw=zs_right-zs_left
    for i in range(0, 5, 1):
        ###将像点从像空间坐标系转换为像空间辅助坐标系
        x1 = matrix_forward_left[i][0]
        y1 = matrix_forward_left[i][1]
        x2 = matrix_forward_right[i][0]
        y2 = matrix_forward_right[i][1]
        matrix_image_space_left = np.array([[x1], [y1], [-f]])
        matrix_image_space_left = matrix_image_space_left.astype(np.float64)
        matrix_image_space_right = np.array([[x2], [y2], [-f]])
        matrix_image_space_right = matrix_image_space_right.astype(np.float64)

        matrix_image_assist_left=np.dot(matrix_r1,matrix_image_space_left)
        matrix_image_assist_left=matrix_image_assist_left * 0.001
        [[u1],[v1],[w1]]=matrix_image_assist_left

        matrix_image_assist_right=np.dot(matrix_r2,matrix_image_space_right)
        matrix_image_assist_right=matrix_image_assist_right*0.001
        [[u2],[v2],[w2]]=matrix_image_assist_right

        #####计算投影系数和地面点坐标
        N1=(bu*w2-bw*u2)/(u1*w2-u2*w1)
        N2=(bu*w1-bw*u1)/(u1*w2-u2*w1)
        [[U1],[V1],[W1]]=N1*matrix_image_assist_left
        [[U2],[V2],[W2]]=N2*matrix_image_assist_right
        ##########计算地面点坐标
        X=xs_left+U1
        Y=(ys_left+V1+ys_right+V2)/2
        Z=zs_left+W1
        q=str(i+1)
        print("第"+q+"个地面点的坐标为")
        print(X,Y,Z)












































