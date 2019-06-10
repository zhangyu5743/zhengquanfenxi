# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 22:37:11 2019

@author: 章鱼哥
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as Tk
from tkinter import ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.backend_bases import key_press_handler
import st_display_ma as dm
import st_display_kmm as dkmm
import stockfund_upgrade_1 as su1
import os
import matplotlib.pyplot as plt
import st_coutminrate as cmr

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
    if(upgrade.get()):
        exit_code = os.system('ping baidu.com') 
  #结束事件主循环，并销毁应用程序窗口
    if exit_code or upgrade.get()==0:
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
    canvas.show()
    toolbar.update()

    
#点击是否进入
def _lowfund():
     low10=cmr.findlowest10fund()
     lowfund.config(text='历史净值比较：比'+str(low10))
     
#生成图片
  #设置图形尺寸与质量  
rooturl='C:/Users/章鱼哥/Desktop/证券分析/gpdata/data/'
#生成界面
matplotlib.use('TkAgg')#不知道有什么用
root =Tk.Tk()
root.title("股票基金查询系统")
root.geometry("8000x4000")


fup=Tk.Frame(width=500,height=420,bg='red')
fup.grid(row=0,padx=1,pady=3,columnspan=20,sticky='e')

fup.grid_propagate(0)
f=plt.figure()
f.subplots(2,1)
f.set_tight_layout(True)# fig.tight_layout()会出现警告
#生成画板
canvas =FigureCanvasTkAgg(f, master=fup)
canvas.show()
#canvas.get_tk_widget().grid(row=0, columnspan=3)
#canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
#canvas.canvas.get_tk_widget().grid(row=0, columnspan=3)   
#生成放大缩小条
#toolbar =NavigationToolbar2TkAgg(canvas, root)
#设置是否更新
upgrade=Tk.IntVar()
upgradecheck = Tk.Checkbutton(master=fup, text='更新数据', bg="yellow",\
   variable=upgrade,onvalue=1,offvalue=0, selectcolor="red",bd =0.1)
upgradecheck.grid(column=0, row=1, sticky=Tk.W)  
upgradecheck.deselect()

#设置是基金还是股票
stock=Tk.IntVar()#0表示不需要更新，1表示需要更新
stockcheck = Tk.Checkbutton(master=root, text='股票', bg="yellow", \
variable=stock,onvalue=1,offvalue=0, selectcolor="red",bd =0.1,command=_lowfund)
stockcheck.grid(column=2, row=1, sticky=Tk.W)  
stockcheck.deselect()
##设置是基金还是股票
fund=Tk.IntVar()#0表示不需要更新，1表示需要更新
fundcheck = Tk.Checkbutton(master=root, text='基金', bg="yellow", \
variable=fund,onvalue=1,offvalue=0, selectcolor="red",bd =0.1)
fundcheck.select()
fundcheck.grid(column=0, row=4, sticky=Tk.W)    
print(fund.get())
#显示输入框
fundinput = Tk.Entry(master=root, bd =0.5,fg='red',font='10',justify='center',width='10')
fundinput.grid(column=2, row=4, sticky=Tk.W)   
##显示运行按钮
button1 =Tk.Button(master=root, text='查询图像',bd =0.5,command=_run)
button1.grid(column=3, row=4, sticky=Tk.W)   
##显示运行按钮
button2 =Tk.Button(master=root, text='查询低点基金',bd =0.5,command=_lowfund)
utton2.grid(column=4, row=5, sticky=Tk.W)   

lowrate=Tk.Label(master=root, text='历史净值比较：')
lowrate.grid(column=3, row=5, sticky=Tk.W)   

lowfund=Tk.Label(master=root, text='基金历史净值最低：')
lowfund.grid(column=6, row=5, sticky=Tk.W)   
Tk.mainloop()
root.attributes("-topmost", 1)