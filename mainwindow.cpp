#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}
//清除文本框中的数据函数
void MainWindow::on_pushButton_clear_clicked()
{
    ui->textEdit_input->clear();
    ui->textEdit_outtput->clear();
}
//退出程序
void MainWindow::on_pushButton_clicked()
{
    QApplication::quit();
}

//读取文件函数
void MainWindow::on_pushButton_2_clicked()
{
    QString inputs = "D:/遥感程序设计文件/无定向导线计算.txt";
    QFile qinput(inputs);
    bool bopen = qinput.open(QIODevice::ReadOnly | QIODevice::Text);
    qDebug() << bopen;
    if (bopen) {
        ui->textEdit_input->clear(); // 清空之前的文本
        while (!qinput.atEnd()) {
            QString strline = qinput.readLine();
            // 去除行末尾的换行符，并检查是否为空行
            strline = strline.trimmed();
            if (!strline.isEmpty()) {
                ui->textEdit_input->append(strline);
            }
        }
        qinput.close(); // 关闭文件
    }
}


void MainWindow::on_pushButton_cal_clicked()
{
    double pai=3.1415926535697;
    QString strInput = ui->textEdit_input->toPlainText();
    QStringList strListInput = strInput.split('\n');
    //获取导线类型
    traverse_type=strListInput[0].toInt();
    //如果不是无定向导线则退出程序
    if(traverse_type!=3)
    {
        QApplication::quit();
    }
    knowpoints_number=strListInput[1].toInt();//读取已知点个数
  //  qDebug() <<knowpoints_number;
    //存储已知点信息
    point*points=new point[knowpoints_number];
   //  point* points = (point*)malloc(knowpoints_number * sizeof(point));
    for(int i=1;i<=knowpoints_number;i++)
    {
        QStringList data=strListInput[1+i].split(',');
        points[i-1].x=data[1].toDouble();
         points[i-1].y=data[2].toDouble();
      //  qDebug()<<points[i-1].x;
      //   qDebug()<<points[i-1].y;
    }
    //存储未知点点号以及未知点数目
    unknowpoints_number=strListInput[4].toInt();
   //  qDebug() <<unknowpoints_number;
    QStringList data=strListInput[5].split(',');
    QString* name = new QString[unknowpoints_number];
     for(int i=0;i<unknowpoints_number;i++)
     {

         name[i]=data[i];
     //    qDebug()<<name[i];
     }
     //存储观测到的角度值
     anglesee_number=strListInput[7].toInt();
     double*angle=new double[anglesee_number];
     for(int i=0;i<anglesee_number;i++)
     {
         QStringList data=strListInput[8+i].split(',');
         angle[i]=data[3].toDouble();
      //   qDebug()<<angle[i];
     }
     distsee_number=strListInput[12].toInt();
     //存储观测到的距离值
     double*dist=new double[distsee_number];
     dist_sum=0;
     for(int i=0;i<distsee_number;i++)
     {
         QStringList data=strListInput[13+i].split(',');
         dist[i]=data[2].toDouble();
         dist_sum+=dist[i];
       //  qDebug()<<dist[i];
     }
     //计算各个待定点坐标
     //假定A1边的方位角
     double angle_assume=60;
     //按单定向导线推算出B点的假定坐标
     //先转变angle的角度为弧度
     for(int i=0;i<anglesee_number;i++)
     {
         double temper=angle[i];
         double temper_ra;
         double temper1=qFloor(temper);
         double temper2=qFloor((temper-temper1)*100);
         double temper3=((temper-temper1)*100-temper2)*100;
         temper_ra=(temper1+temper2/60+temper3/3600)*pai/180;
         angle[i]=temper_ra;
    //     qDebug()<<angle[i];
     }
     //计算单定向导线的方位角
     double*angle_turning=new double[anglesee_number];
     angle_turning[0]=angle_assume*pai/180;
     for(int i=1;i<anglesee_number+1;i++)
     {
         angle_turning[i]=angle_turning[i-1]+pai-angle[i-1];//右角
     }
     //计算x和y
     point*points_assume=new point[unknowpoints_number+knowpoints_number];
     points_assume[0]=points[0];
     for(int i=1;i<knowpoints_number+unknowpoints_number;i++)
     {
         points_assume[i].x=points_assume[i-1].x+dist[i-1]*cos(angle_turning[i-1]);
         points_assume[i].y=points_assume[i-1].y+dist[i-1]*sin(angle_turning[i-1]);
     }
     //反算出AB假定方位角及AB假定边长
     angle_bc_assume=qAtan((points_assume[knowpoints_number+unknowpoints_number-1].y-points_assume[0].y)/(points_assume[knowpoints_number+unknowpoints_number-1].x-points_assume[0].x));
     dist_bc_assume=sqrt((points_assume[knowpoints_number+unknowpoints_number-1].y-points_assume[0].y)*(points_assume[knowpoints_number+unknowpoints_number-1].y-points_assume[0].y)+(points_assume[knowpoints_number+unknowpoints_number-1].x-points_assume[0].x)*(points_assume[knowpoints_number+unknowpoints_number-1].x-points_assume[0].x));
     // 以A为基点对该导线进行缩放，缩放比=AB边真长/AB边假定边长
     dist_bc_true=sqrt((points[0].y-points[1].y)*(points[0].y-points[1].y)+(points[0].x-points[1].x)*(points[0].x-points[1].x));
     //以A为基点旋转该导线，旋角=AB真方位角-AB假定方位角
     angle_bc_true=qAtan((points[1].y-points[0].y)/(points[1].x-points[0].x));
     angle_rotate=angle_bc_true- angle_bc_assume;
     dist_proportion=dist_bc_true/dist_bc_assume;
     for(int i=0;i<distsee_number;i++)
     {
         dist[i]=dist_proportion*dist[i];
     }
     for(int i=0;i<=anglesee_number;i++)
     {
         angle_turning[i]=angle_turning[i]+angle_rotate;
     }
     //根据旋转后的A1 方位角和缩放后的各边长数据，重新推算各点的坐标即可
      point*points_true=new point[knowpoints_number+unknowpoints_number];
     points_true[0]=points[0];
     for(int i=1;i<knowpoints_number+unknowpoints_number;i++)
     {
         points_true[i].x=points_true[i-1].x+dist[i-1]*cos(angle_turning[i-1]);
         points_true[i].y=points_true[i-1].y+dist[i-1]*sin(angle_turning[i-1]);
         if(i==5)
         {qDebug()<<points_true[i].x;}
         if(i==knowpoints_number+unknowpoints_number-1)
         {
             fx=points_true[i].x-points[1].x;
             fy=points_true[i].y-points[1].y;
         //    qDebug()<<fx;
         //    qDebug()<<fy;
         }
     }

    //计算相对闭合差和边长比例
     closing_error=1-1/dist_proportion;
     R=dist_proportion;
     qDebug()<<R;

 for(int i=0;i<distsee_number;i++)
    {
    dist[i]=dist[i]*R;
     }
 for(int i=1;i<knowpoints_number+unknowpoints_number;i++)
 {
     points_true[i].x=points_true[i-1].x+dist[i-1]*cos(angle_turning[i-1]);
     points_true[i].y=points_true[i-1].y+dist[i-1]*sin(angle_turning[i-1]);
 }
     //输出计算结果
     ui->textEdit_outtput->append("待定点坐标：");
     QString str1="B:(";
     QString str2=QString::number(points[0].x,'f',3);
     QString str3=",";
     QString str4=QString::number(points[0].y,'f',3);
     QString str5=")";
     QString str6=str1+str2+str3+str4+str5;
     ui->textEdit_outtput->append(str6);
     QString str7="T1:(";
     QString str8=QString::number(points_true[1].x,'f',3);
     QString str9=",";
     QString str10=QString::number(points_true[1].y,'f',3);
     QString str11=")";
     QString str12=str7+str8+str9+str10+str11;
 ui->textEdit_outtput->append(str12);
     QString str13="T2:(";
     QString str14=QString::number(points_true[2].x,'f',3);
     QString str15=",";
     QString str16=QString::number(points_true[2].y,'f',3);
     QString str17=")";
     QString str18=str13+str14+str15+str16+str17;
     ui->textEdit_outtput->append(str18);
     QString str19="T3:(";
     QString str20=QString::number(points_true[3].x,'f',3);
     QString str21=",";
     QString str22=QString::number(points_true[3].y,'f',3);
     QString str23=")";
     QString str24=str19+str20+str21+str22+str23;
     ui->textEdit_outtput->append(str24);
     QString str25="T4:(";
     QString str26=QString::number(points_true[4].x,'f',3);
     QString str27=",";
     QString str28=QString::number(points_true[4].y,'f',3);
     QString str29=")";
     QString str30=str25+str26+str27+str28+str29;
     ui->textEdit_outtput->append(str30);
     QString str31="C:(";
     QString str32=QString::number(points[1].x,'f',3);
     QString str33=",";
     QString str34=QString::number(points[1].y,'f',3);
     QString str35=")";
     QString str36=str31+str32+str33+str34+str35;
     ui->textEdit_outtput->append(str36);
    QString str37="相对闭合差大小：";
    QString str38=QString::number(closing_error);
    QString str39=str37+str38;
    ui->textEdit_outtput->append(str39);
}


void MainWindow::on_pushButton_3_clicked()
{
    // 检查textEdit是否为nullptr
    if (!ui->textEdit_outtput)
    {
        QMessageBox::critical(nullptr, "错误", "QTextEdit对象为空！");
        return;
    }

    // 创建一个QFile对象
    QFile file("D:/遥感程序设计文件/无定向导线计算结果文件.txt");

    // 尝试打开文件
    if (!file.open(QIODevice::WriteOnly | QIODevice::Text)) {
        QMessageBox::critical(nullptr, "错误", "无法打开文件进行写入！");
        return;
    }

    // 创建一个QTextStream对象，用于写入文件
    QTextStream out(&file);
    // 将QTextEdit中的文本写入文件
    out << ui->textEdit_outtput->toPlainText();

    // 关闭文件
    file.close();
}

