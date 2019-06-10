#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as Tk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
import display_ma as dm
import display_kmm as dkmm
import stockfund_upgrade_1 as su1
import os
import matplotlib.pyplot as plt
import coutminrate as cmr
#定义并绑定键盘事件处理函数
def on_key_event(event):
  print('you pressed %s'% event.key)
  key_press_handler(event, canvas, toolbar)
  canvas.mpl_connect('key_press_event', on_key_event)
  
#查询基金更新并显示ma图像
def _run():
    f.clf()
    fundnum=fundinput.get()
    exit_code=0
    if(upgrade):
        exit_code = os.system('ping baidu.com') 
  #结束事件主循环，并销毁应用程序窗口
    if exit_code or upgrade==0:
    #没网
        print("没有网或无需更新，采用本地数据")
        a=plt.subplot(211)
        dm.show_data(fundnum,rooturl,a)
        b=plt.subplot(212)
        dkmm.show_data_kmm(fundnum,rooturl,b)
    else:
    #有网
        a=plt.subplot(211)
        su1.reload(fundnum ,rooturl)
        dm.show_data(fundnum,rooturl,a)
        b=plt.subplot(212)
        dkmm.show_data_kmm(fundnum,rooturl,b)
        #把绘制的图形显示到tkinter窗口上
    lowrate.config(text='历史净值比较：比'+str(cmr.coutminrate_now(fundnum,rooturl)*100)+'%时候低')
    canvas.draw()
    toolbar.update()

#不知道用来干嘛
def _count():
    
    f.clf()
    fundnum=fundinput.get()
    exit_code=0
    if(upgrade):
        exit_code = os.system('ping baidu.com') 
  #结束事件主循环，并销毁应用程序窗口
    if exit_code or upgrade==0:
    #没网
        print("没有网或无需更新，采用本地数据")
        #f=plt.subplots(2,1)
       # plt.subplots(2,1)
        a=plt.subplot(211)
        dm.show_data(fundnum,rooturl,a)
        b=plt.subplot(212)
        dkmm.sho0w_data_kmm(fundnum,rooturl,b)
    else:
    #有网
        a=plt.subplot(221)
        su1.reload(fundnum ,rooturl)
        dm.show_data(fundnum,rooturl)
        
        b=plt.subplot(222)
        dkmm.show_data_kmm(fundnum,rooturl,b)
        #把绘制的图形显示到tkinter窗口上

    canvas.draw()
    # toolbar.update()
    
#点击是否进入
def _upgrade():
     global upgrade
     if upgrade==1:#判断是否被选中
            upgrade=0
            print(upgrade)
     else:
            upgrade=1
            print(upgrade)
#点击是否进入
def _sfund_lowfund():
     low10=cmr.findlowest10fund()
     lowfund.config(text='历史净值比较：比'+str(low10))
  #设置图形尺寸与质量  
rooturl='C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/'
#生成界面
matplotlib.use('TkAgg')#不知道有什么用
root =Tk.Tk()
root.title("基金查询系统")
root.geometry("800x600")
f=plt.figure()

f.subplots(2,1)
f.set_tight_layout(True)# fig.tight_layout()会出现警告
#生成画板
canvas =FigureCanvasTkAgg(f, master=root)
canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
canvas.draw()
#canvas.canvas.get_tk_widget().grid(row=0, columnspan=3)   
#生成放大缩小条
toolbar =NavigationToolbar2Tk(canvas, root)
#设置是否更新
upgrade=0#0表示不需要更新，1表示需要更新
upgradecheck = Tk.Checkbutton(master=root, text='更新数据', bg="yellow", selectcolor="red",bd =0.1,variable=0,command=_upgrade)
upgradecheck.pack(anchor=Tk.CENTER)
#显示输入框
fundinput = Tk.Entry(master=root, bd =0.5,fg='red',font='10',justify='center',width='10')
fundinput.pack(anchor=Tk.CENTER)
#显示运行按钮
button1 =Tk.Button(master=root, text='查询图像',bd =0.5,command=_run)
button1.pack(anchor=Tk.CENTER)
#显示运行按钮
button2 =Tk.Button(master=root, text='查询低点基金',bd =0.5,command=_sfund_lowfund)
button2.pack(anchor=Tk.CENTER)
#显示运行按钮
#button2 =Tk.Button(master=root, text='run',bd =0.5,command=_run)
#button2.pack(anchor=Tk.CENTER)
lowrate=Tk.Label(master=root, text='历史净值比较：')
lowrate.pack(anchor=Tk.CENTER)
lowfund=Tk.Label(master=root, text='基金历史净值最低：')
lowfund.pack(anchor=Tk.CENTER)
Tk.mainloop()
root.attributes("-topmost", 1)