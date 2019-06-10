# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:57:54 2019

@author: 章鱼哥
"""
import os
import copy
import re
def is_number(s):
  try:
    complex(s) # for int, long, float and complex
  except ValueError:
    return False
  return True
#数据规整
rooturl='C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/'
for root, dirs, files in os.walk(rooturl):  
    print(root) #当前目录路径  
    print(dirs) #当前路径下所有子目录  
    print(files) #当前路径下所有非目录子文件
    srcfile_name=files
    
#按照基金代码循环
for part in srcfile_name:  
    temp=[]
   # print(part) #当前处理文件号  
                #输出标题
    res=open(rooturl+part[:-4]+'.txt',"r",errors='ignore')
    reslines=res.readlines()     #读取文件中的内容所有内容
    res.close()
    if(len(reslines)<=3):  
        os.remove(rooturl+part[:-4]+'.txt')    #删除文件
        continue
    
    out=0
    b=[]
    copy1=1
    c=[]
    #读取就文件
    for a in reslines:
        if(out==0):
            temp.append(a)
            out=out+1
            continue
        else:
            if(out==1):
                b=re.split(" |%", a)
                try:
                    if(not is_number(b[3])):
                        templine=str(b[0])+' '+str(b[1])+' '+str(b[2])+' 0'+' \n'
                        c = copy.deepcopy(re.split(" |%", templine))
                        temp.append(templine)
                except IndexError:
                    out=out+1                    
                    continue
                else:
                    out=out+1
                    continue
            else:
                b=re.split(" |%", a)
                try:
                    if(  is_number(b[1]) and  is_number(b[2]) and is_number(b[3])):
                         temp.append(a)  
                         c = copy.deepcopy(b)
                    else:
                         templine=str(b[0])+' '+str(c[1])+' '+str(c[2])+' 0'+' \n'
                         print('有问题已被修改：'+part[:-4])
                         temp.append(templine)
                except IndexError:
                    continue
                else:
                    continue
        

    data =open(rooturl+part[:-4]+'.txt',"w+")
    for l in temp:
        data.write(l)
    data.close()