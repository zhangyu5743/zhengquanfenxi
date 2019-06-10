
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:14:16 2019

@author: 章鱼哥
"""
#数组复制是a=b[:]而不是a=b
#可以尝试用turtle画图
# 导入 matplotlib 的所有内容（nympy 可以用 np 这个名字来使用）
import matplotlib.pyplot as plt
from datetime import datetime 
#该函数在计算日常K线减去ma20



def show_data_kmm( fundnum ,rooturl,a):

    res=open(rooturl+fundnum+'.csv',"r",errors='ignore')
    reslines=res.readlines()     #读取文件中的内容所有内容
    res.close()
    #去除第一行
    if(reslines):    
        reslines=reslines[1:]
        #数组颠倒
        reslines=reslines[::-1]
        #分割成二维数组
        for i in range(len(reslines)):
            reslines[i]=reslines[i].split(',')
        #获取单位净值
        net_asset_value = [i[7] for i in reslines] 
        for i in range(len(net_asset_value)):
            net_asset_value[i]=float(net_asset_value[i])
       # print(net_asset_value)
        #获取日期
        date = [i[0] for i in reslines] 
        print(date[0])
        print(date[-1])
        #计算ma
        ma5=net_asset_value[:];
        ma20=net_asset_value[:];
        ma120=net_asset_value[:];
        for i in range(5,len(net_asset_value)):
            ma5[i]=sum(net_asset_value[i-4:i+1])/5;
        for i in range(0,5):
            ma5[i]=sum(net_asset_value[:(i+1)])/(i+1);
        
        for i in range(20,len(net_asset_value)):
            ma20[i]=sum(net_asset_value[i-19:i+1])/20;
        for i in range(0,20):
            ma20[i]=sum(net_asset_value[:(i+1)])/(i+1);
        
        for i in range(120,len(net_asset_value)):
            ma120[i]=sum(net_asset_value[i-119:i+1])/120;
        for i in range(0,120):
            ma120[i]=sum(net_asset_value[:(i+1)])/(i+1);
            
        kmm_value20=net_asset_value[:];
        for i in range(0,len(net_asset_value)):
            kmm_value20[i]=net_asset_value[i]-ma20[i];
        
        kmm_value5=net_asset_value[:];
        for i in range(0,len(net_asset_value)):
            kmm_value5[i]=net_asset_value[i]-ma5[i];
        
        y0=[0 for i in range(len(net_asset_value))]
# 创建一个 8 * 6 点（point）的图，并设置分辨率为 80
        xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in date]
        a.set_title(fundnum)
        wide='2'
        a.plot(xs, y0, '-', linewidth = wide)
        a.plot(xs, kmm_value20, '-', linewidth = wide, label = "kmm20")
        a.plot(xs, kmm_value5, '-', linewidth = wide, label = "kmm5")
        a.legend(loc='upper left')
        a.set_xlabel('Date')
        a.set_ylabel('value')
        a.text(xs[-1],net_asset_value[-1], net_asset_value[-1], ha='right', va='bottom', fontsize=10)
        print(fundnum)

        return