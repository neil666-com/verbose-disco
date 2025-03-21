#include "dialog.h"
#include "ui_dialog.h"

Dialog::Dialog(QWidget *parent)
    : QDialog(parent)
    , ui(new Ui::Dialog)
{
    ui->setupUi(this);
    ui->label_pic->setPixmap(QPixmap(":/new/prefix1/图片1.png"));
    ui->label_pic->setScaledContents(true);
}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_pushButton_2_clicked()
{
    QApplication::quit();
}


void Dialog::on_pushButton_clicked()
{
    //设置为模态
    MainWindow*w=new MainWindow();
    w->setWindowModality(Qt::WindowModal);
    w->show();



}

