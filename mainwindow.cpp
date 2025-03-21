#include "mainwindow.h"
#include "ui_mainwindow.h"
#include"math.h"
MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->label_pic->setPixmap(QPixmap(":/new/prefix1/图片1.png"));
    ui->label_pic->setScaledContents(true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_2_clicked()
{
    //清空lineedit中的数据
    ui->lineEdit_XA->clear();
    ui->lineEdit_YA->clear();
    ui->lineEdit_XB->clear();
    ui->lineEdit_YB->clear();
    ui->lineEdit_XC->clear();
    ui->lineEdit_YC->clear();
    ui->lineEdit_XD->clear();
    ui->lineEdit_YD->clear();
    ui->lineEdit_a1->clear();
    ui->lineEdit_a2->clear();
    ui->lineEdit_a3->clear();
    ui->lineEdit_a4->clear();
    ui->lineEdit_a5->clear();
    ui->lineEdit_a6->clear();
    ui->lineEdit_a7->clear();
    ui->lineEdit_a8->clear();
    ui->lineEdit_condition->clear();
    ui->lineEdit_triangle1->clear();
    ui->lineEdit_triangle2->clear();
    ui->lineEdit_triangle3->clear();
}


void MainWindow::on_pushButton_3_clicked()
{
    //关闭窗口
    QApplication::quit();
}


void MainWindow::on_pushButton_clicked()
{
    //定义变量以及圆周率和p的参数
     double pai=3.141592653589;
    double p = 206265;double w1,w2,w3;
     double xa,ya,xb,yb,xc,yc,xd,yd,a1,a2,a3,a4,a5,a6,a7,a8,condition;
    xa=ui->lineEdit_XA->text().toDouble();
    ya=ui->lineEdit_YA->text().toDouble();
    xb=ui->lineEdit_XB->text().toDouble();
    yb=ui->lineEdit_YB->text().toDouble();
    a1=ui->lineEdit_a1->text().toDouble();
    a2=ui->lineEdit_a2->text().toDouble();
    a3=ui->lineEdit_a3->text().toDouble();
    a4=ui->lineEdit_a4->text().toDouble();
    a5=ui->lineEdit_a5->text().toDouble();
    a6=ui->lineEdit_a6->text().toDouble();
    a7=ui->lineEdit_a7->text().toDouble();
    a8=ui->lineEdit_a8->text().toDouble();
//将度分秒形式转换为度的形式
    double temper,temper1,temper2;
    temper=floor(a1);
    a1=a1-temper;
    a1=a1*100;
    temper1=floor(a1);
    a1=a1-temper1;
    a1=a1*100;
    temper2=a1;
    a1=temper+temper1/60+temper2/3600;

    temper=floor(a2);
    a2=a2-temper;
    a2=a2*100;
    temper1=floor(a2);
    a2=a2-temper1;
    a2=a2*100;
    temper2=a2;
    a2=temper+temper1/60+temper2/3600;

    temper=floor(a3);
    a3=a3-temper;
    a3=a3*100;
    temper1=floor(a3);
    a3=a3-temper1;
    a3=a3*100;
    temper2=a3;
    a3=temper+temper1/60+temper2/3600;

    temper=floor(a4);
    a4=a4-temper;
    a4=a4*100;
    temper1=floor(a4);
    a4=a4-temper1;
    a4=a4*100;
    temper2=a4;
    a4=temper+temper1/60+temper2/3600;

    temper=floor(a5);
    a5=a5-temper;
    a5=a5*100;
    temper1=floor(a5);
    a5=a5-temper1;
    a5=a5*100;
    temper2=a5;
    a5=temper+temper1/60+temper2/3600;

    temper=floor(a6);
    a6=a6-temper;
    a6=a6*100;
    temper1=floor(a6);
    a6=a6-temper1;
    a6=a6*100;
    temper2=a6;
    a6=temper+temper1/60+temper2/3600;

    temper=floor(a7);
    a7=a7-temper;
    a7=a7*100;
    temper1=floor(a7);
    a7=a7-temper1;
    a7=a7*100;
    temper2=a7;
    a7=temper+temper1/60+temper2/3600;

    temper=floor(a8);
    a8=a8-temper;
    a8=a8*100;
    temper1=floor(a8);
    a8=a8-temper1;
    a8=a8*100;
    temper2=a8;
    a8=temper+temper1/60+temper2/3600;


//计算大地四边形的角度闭合差（4个中有三个是相互独立的）
    w1=a5+a6+a7+a8-180;
    w2=a1+a2+a3+a4-180;
    w3=a1+a2+a7+a8-180;
    w1=w1*3600/10000;
    w2=w2*3600/10000;
    w3=w3*3600/10000;
    ui->lineEdit_triangle1->setText(QString::number(w1,'f',6));
    ui->lineEdit_triangle2->setText(QString::number(w2,'f',6));
    ui->lineEdit_triangle3->setText(QString::number(w3,'f',6));
    a1=a1*pai/180; a2=a2*pai/180; a3=a3*pai/180; a4=a4*pai/180; a5=a5*pai/180; a6=a6*pai/180; a7=a7*pai/180;
     a8=a8*pai/180;
    //利用前方交会算法计算C和D点的坐标
    double D0,D1;
    D0=sqrt((xa-xb)*(xa-xb)+(ya-yb)*(ya-yb));
    D1=D0*sin(a1)/sin(a1+a2+a3);
   // D2=D0*sin(a2+a3)/sin(a1+a2+a3);
    double A,a;
    a=atan2((yb-ya),(xb-xa));
    A=a-(a2+a3);
   // B=a+a1;
    xc=xa+D1*cos(A);
    yc=ya+D1*sin(A);
    ui->lineEdit_XC->setText(QString::number(xc,'f',6));
    ui->lineEdit_YC->setText(QString::number(yc,'f',6));
    D1=D0*sin(a1+a8)/sin(a1+a2+a8);
    //D2=D0*sin(a2)/sin(a1+a2+a8);
    double A1;
    A1=a-a2;
    //B1=a+a1+a8;
    xd=xa+D1*cos(A1);
    yd=ya+D1*sin(A1);
    ui->lineEdit_XD->setText(QString::number(xd,'f',6));
    ui->lineEdit_YD->setText(QString::number(yd,'f',6));
    //计算极条件闭合差
    condition=(1-(sin(a1)*sin(a7)*sin(a4+a5))/(sin(a4)*sin(a1+a8)*sin(a6)))*p;
     ui->lineEdit_condition->setText(QString::number(condition,'f',6));

}

