# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 11:14:16 2019
@author: 章鱼哥
"""
import os  
import numpy as np

#计算到今天比百分之多少要低
def coutminrate_now(fundnum,rooturl):
    low=0
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
#            if(net_asset_value[i]=='--'):
#                net_asset_value[i]=float(net_asset_value[i-1])
#            else:
                net_asset_value[i]=float(net_asset_value[i])
        for i in range(0,len(net_asset_value)):
            if (net_asset_value[len(net_asset_value)-1]<net_asset_value[i]):
                low=low+1
        print(fundnum)
       
    return low/len(net_asset_value)

#计算到制定日期比百分之多少要低
def coutminrate_someday(fundnum,rooturl,targetdata):
    low=0
    res=open(rooturl+fundnum+'.txt',"r",errors='ignore')
    reslines=res.readlines()     #读取文件中的内容所有内容
    res.close()
    #去除第一行
    if(reslines):    
        reslines=reslines[1:]
        #数组颠倒
        reslines=reslines[::-1]
        #分割成二维数组
        for i in range(len(reslines)):
            reslines[i]=reslines[i].split(' ')
        #获取单位净值
        net_asset_value = [i[1] for i in reslines] 
      #  data = [i[0] for i in reslines]
        for i in range(len(net_asset_value)):
            net_asset_value[i]=float(net_asset_value[i])
        for i in range(0,targetdata):
            if (net_asset_value[len(net_asset_value)-1]<net_asset_value[i]):
                low=low+1
        print(fundnum)
    return low/targetdata

def findlowest10fund():
    rooturl="C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/"
    for root, dirs, files in os.walk(rooturl):  
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件
        srcfile_name=files
    data_list=[]
    for part in srcfile_name: 
#    data_list =  [([0] * 2) for i in range(len(srcfile_name))] 
        res=open(rooturl+part[:-4]+'.txt',"r",errors='ignore')
        reslines=res.readlines()     #读取文件中的内容所有内容
        res.close()
        
        if(reslines):    
            reslines=reslines[1:]
            #数组颠倒
            reslines=reslines[::-1]
            #分割成二维数组
            for i in range(len(reslines)):
                reslines[i]=reslines[i].split(' ')
            #获取单位净值
            net_asset_value = [i[1] for i in reslines]
            if(float(max(net_asset_value))-float(min(net_asset_value))>0.2):
                data_list.append([part[:-4],coutminrate_now(str(part[:-4]),rooturl)])
                
                
    rate = [i[1] for i in data_list] 
    a = np.array(rate)
    b = np.argsort(a)
    b=b[::-1]
    maxnum=[]
    for i in range(30,40):
        print(data_list[b[i]][0])
        maxnum.append(data_list[b[i]][0])
    return maxnum
    #rooturl='C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/'
#b=findlowest10fund()
#fundnum='001986'
#print(coutminrate_now(fundnum,rooturl))
#print(coutminrate_someday(fundnum,rooturl,600))