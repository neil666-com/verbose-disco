#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include<QFile>
#include<cmath>
#include <QtMath>
#include<QMessageBox>
QT_BEGIN_NAMESPACE
namespace Ui {
class MainWindow;
}
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    struct point{
        double x;
        double y;
    };//定义结构体
    point* points;//存储控制点的坐标
    double*angle;//存储角度观测值
    double*dist;//存储距离观测值
    QString*name;//待定点点号
    point*points_assume;//按照假设的方位角推算出来的点位坐标
    point*points_true;//改正后的点位坐标
    double*angle_turning;//假设方位角推算出的转折角
    double*vx;//x方向加的坐标闭合差
    double*vy;//x方向加的坐标闭合差



private slots:
    void on_pushButton_clear_clicked();

    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_pushButton_cal_clicked();

    void on_pushButton_3_clicked();

private:
    Ui::MainWindow *ui;
 int knowpoints_number;//控制点数目
    int unknowpoints_number;//待定点数目
    int anglesee_number;//角度观测值数目
    int distsee_number;//距离观测值数目
    int traverse_type;//导线类型
    double angle_bc_assume;//AB假定方位角
    double dist_bc_assume;//AB假定距离
    double dist_bc_true;//AB真实距离
    double angle_bc_true;//AB真实方位角
    double angle_rotate;//角度旋转值
    double dist_proportion;//长度比例
    double closing_error;//相对闭合差
    double fx;//x坐标误差
    double fy;//y坐标误差
    double dist_sum;//路线总长度
    double R;//边长缩放比例
};
#endif // MAINWINDOW_H
