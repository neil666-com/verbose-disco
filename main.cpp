#include "mainwindow.h"
#include<QDialog>
#include"dialog.h";
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Dialog w;
    w.show();
    //MainWindow w;
   // w.show();
    return a.exec();
}
