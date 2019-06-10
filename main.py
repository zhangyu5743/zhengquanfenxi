# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
import window
from window import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
matplotlib.use("Qt5Agg")  # 声明使用QT5
from PyQt5.QtWidgets import *
import display_all
from display_all import st_show_data_kmm,st_show_data_ma,sf_show_data_kmm,sf_show_data_ma
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import stockfund_upgrade_1 as sfup1
def grapnew(ui):
    print(ui.F)
    ui.F.draw()
    ui.Q.draw()
    print(1)
#创建一个matplotlib图形绘制类
class MyFigure(FigureCanvas):
    def __init__(self):#调用的时候赋值给的是int
        #第一步：创建一个创建Figure
        self.fig = Figure(figsize=(0, 20), dpi=100)
        #第二步：在父类中激活Figure窗口
        super(MyFigure,self).__init__(self.fig) #调用FigureCanvas的__init__()
        #第三步：创建一个子图，用于绘制图形用，111表示子图编号
        self.axes = self.fig.add_subplot(111)
        self.fig.subplots_adjust(top=0.9, bottom=0.1, right=0.98, left=0.05, hspace=0, wspace=0)
############事件监听########################################
#鼠标移动
    # def mouseMoveEvent(self, event):
    #     # if event.buttons() == Qt.LeftButton:
    #     #     # print(type(event.pos().x()))    #<class 'int'>
    #     #     self.lab2.setText(str(event.pos().x())+","+str(event.pos().y()))
    #     self.pos = event.pos()
    #     print(self.pos)
    #     self.update()

#鼠标点击
    def mousePressEvent(self, event):
        if event.button() == 1:
            print("鼠标左键点击")
        elif event.button() == 2:
            print("鼠标右键点击")
        elif event.button() == 4:
            print("鼠标中键点击")
        # axtemp = event.axes
        self.update()
    # 滚轮事件
    def wheelEvent(self, event):
        if(event.angleDelta().y()>0):
            if(self.figure.axes[0].get_xlim()[0]>self.figure.axes[0].get_xlim()[1]-1000):
                 min=self.figure.axes[0].get_xlim()[0]-100
                 ui.F.figure.axes[0].set_xlim(min,self.figure.axes[0].get_xlim()[1])
                 ui.Q.figure.axes[0].set_xlim(min, self.figure.axes[0].get_xlim()[1])

        if(event.angleDelta().y()<0):
            if(self.figure.axes[0].get_xlim()[0]<self.figure.axes[0].get_xlim()[1]-200):
                 min=self.figure.axes[0].get_xlim()[0]+100
                 ui.F.figure.axes[0].set_xlim(min,self.figure.axes[0].get_xlim()[1])
                 ui.Q.figure.axes[0].set_xlim(min, self.figure.axes[0].get_xlim()[1])
        # 通过外部函数调用ui里面的F和Q更新
        grapnew(ui)

class win(Ui_MainWindow):
    # ---------------这个是建立新的figure的操作-----------------------
    # 第五步：定义MyFigure类的一个实例

    def initializtion(self,MainWindow):#调用的时候赋值给的是int
        self.fundcheckBox.toggled.connect(self.fcstate)
        # self.upgradecheckBox.toggled.connect(self.btnState)
        self.stockcheckBox.toggled.connect(self.ststate)
        self.fundcheckBox.setChecked(True)

    def createfigure(self, MainWindow):
        self.F = MyFigure()
        self.gridlayout = QGridLayout(self.frame)  # 继承容器groupBox
        self.gridlayout.addWidget(self.F, 0, 1)

        self.Q = MyFigure()
        self.gridlayout = QGridLayout(self.frame_2)  # 继承容器groupBox
        self.gridlayout.addWidget(self.Q, 0, 1)
        # toolbar = NavigationToolbar2Tk(self.F, MainWindow)

    def proUi_ma(self,code):#股票是1 基金是0
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，
        if(self.stockcheckBox.isChecked()==True):
            self.F.axes.cla()
            rooturl = 'C:/Users/章鱼哥/Desktop/证券分析/gpdata/data/'
            st_show_data_ma(code, rooturl, self.F.axes)
        if(self.fundcheckBox.isChecked()==True):
            self.F.axes.cla()
            rooturl = "C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/"
            sf_show_data_ma(code, rooturl, self.F.axes)
        self.F.draw()
        # FigureCanvas.updateGeometry(self)
        # ------------------------------------------------------------------------
    def proUi_kmm(self,  code):  # 股票是1 基金是0
        # 第三步：创建一个子图，用于绘制图形用，111表示子图编号，
        # self.Q = MyFigure()
        if (self.stockcheckBox.isChecked()==True):
            self.Q.axes.cla()
            rooturl = 'C:/Users/章鱼哥/Desktop/证券分析/gpdata/data/'
            st_show_data_kmm(code, rooturl, self.Q.axes)
        if (self.fundcheckBox.isChecked()==True):
            self.Q.axes.cla()
            rooturl = "C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/"
            sf_show_data_kmm(code, rooturl, self.Q.axes)
        self.Q.draw()
        # ------------------------------------------------------------------------
    def buttoncontrol(self, MainWindow):
        a=self.codetext.text()
        a=self.codetext.text()
        self.showdatabtn.clicked.connect(self.showdata)
        MainWindow.show()
    def showdata(self):
        if (self.upgradecheckBox.isChecked() == True and self.fundcheckBox.isChecked()==True):
            sfrooturl = 'C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/'
            sfup1.reload(self.codetext.text(), sfrooturl)
        self.proUi_kmm(self.codetext.text())
        self.proUi_ma(self.codetext.text())

    def ststate(self):
             if self.stockcheckBox.isChecked()==True:
                 self.fundcheckBox.setChecked(False)
             else:
                 self.fundcheckBox.setChecked(True)

    def fcstate(self):
             if self.fundcheckBox.isChecked()==True:
                 self.stockcheckBox.setChecked(False)
             else:
                 self.stockcheckBox.setChecked(True)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建一个QApplication，也就是你要开发的软件app
    MainWindow = QtWidgets.QMainWindow()  # 创建一个QMainWindow，用来装载你需要的各种组件、控件
    ui =win()  # ui是你创建的ui类的实例化对象
    ui.setupUi(MainWindow)  # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow
    ui.createfigure(MainWindow)

    ui.initializtion(MainWindow)
    ui.buttoncontrol(MainWindow)
    # ui.proUi_ma(1,'000001')
    # ui.proUi_kmm(1,'000001')
    # ui.proUi_ma(MainWindow,0,'001986')
    # ui.proUi_kmm(MainWindow,0,'001986')
    MainWindow.show()  # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_())


