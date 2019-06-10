# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:11:02 2019

@author: 章鱼哥
"""
import copyfile
import os  
rooturl=r"C:\Users\章鱼哥\Desktop\证券分析\基金\data"
for root, dirs, files in os.walk(rooturl):  
    print(root) #当前目录路径  
    print(dirs) #当前路径下所有子目录  
    print(files) #当前路径下所有非目录子文件
    srcfile_name=files
#识别是不是理财产品还是股票基金
for name in srcfile_name:
    srcfile=rooturl+"\\"+name
    f = open(srcfile)
    line = f.readline()
    if(line=='净值日期 单位净值 累计净值 日增长率 申购状态 赎回状态 分红送配\n'):
        dstfile=rooturl+"\\"+'stock_fund'+"\\"+name
        copyfile.copyfile(srcfile,dstfile)
    f.close()

for name in srcfile_name:
    srcfile=r"C:\Users\章鱼哥\Desktop\证券分析\基金\data\\"+name
    f = open(srcfile)
    line = f.readline()
    if(line=='净值日期 每万份收益 7日年化收益率（%） 申购状态 赎回状态 分红送配\n'):
        dstfile=rooturl+"\\"+'bond_fund'+"\\"+name
        copyfile.copyfile(srcfile,dstfile)
    f.close()

#i=0
#graph= []
#while line:
#    line=line.split()
#    graph.append(line)
#    i=i+1
#    line = f.readline()
#print(graph[1][:])

#copyfile.copyfile(srcfile,dstfile)