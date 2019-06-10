# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:11:02 2019

@author: 章鱼哥
"""
import numpy as np
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSelectorException
#from bs4 import BeautifulSoup
import time
import os  

from selenium.webdriver.chrome.options import Options

chrome_options=Options()

#设置chrome浏览器无界面模式
#浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
chrome_options.add_argument('--headless')
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度

 #实例化一个浏览器
#driver = webdriver.Chrome(chrome_options=chrome_options)
# 设设设设设设设设设chrome_opt设设设设
browser = webdriver.Chrome(r'C:\Users\章鱼哥\AppData\Local\Google\Chrome\Application\chromedriver.exe',chrome_options=chrome_options)
#browser.maximize_window() 
#获取现有基金代码
rooturl=r"C:\Users\章鱼哥\Desktop\证券分析\基金\data\stock_fund"
for root, dirs, files in os.walk(rooturl):  
    print(root) #当前目录路径  
    print(dirs) #当前路径下所有子目录  
    print(files) #当前路径下所有非目录子文件
    srcfile_name=files
    
#按照基金代码循环
for part in srcfile_name:  
    print(part) #当前处理文件号  
    browser.get('http://fund.eastmoney.com/f10/jjjz_'+part[:-4]+'.html')
        #先试试能不能打开网页
    try:
        #输出标题
        a=browser.find_element_by_xpath('//*[@id="jztable"]/table/thead/tr').text
    #无法打开网页就跳出，然后显示不行的基金代码
    except  NoSuchElementException as msg:
             print('wrong:'+part[:-4])
    else:
        #读取就文件
        res=open('C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/'+part[:-4]+'.txt',"r",errors='ignore')
        reslines=res.readlines()     #读取文件中的内容所有内容
        res.close()
        out=0
        
        if(len(reslines)>2):
               #输出抬头
            data =open('C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/'+part[:-4]+'.txt',"w+")
            data.write(a+'\n')            
            #输出内容（数据）
            while browser.find_element_by_xpath("//label[text()='下一页']").value_of_css_property('color')=='rgba(3, 42, 143, 1)':
                rowCount = len(browser.find_elements_by_xpath('//*[@id="jztable"]/table/tbody/tr'))
                for i in range(1,rowCount+1):
                    a=browser.find_element_by_xpath('//*[@id="jztable"]/table/tbody/tr['+str(i)+']').text
                    b=reslines[1]
                    if(a[:10]==b[:10]):
                            out=1
                            break
                    else:
                            data.write(a+'\n')
                if(out==1):
                    break
                #点击下一页
                nextpage=browser.find_element_by_xpath("//label[text()='下一页']")
                nextpage.click()
                #看看加载完了吗，没有的话就继续等待
                i=1
                while i:
                        try:
                            a=browser.find_element_by_xpath('//*[@id="jztable"]/table/tbody/tr[1]').text
                            i=0;
                        except (StaleElementReferenceException,NoSuchElementException) as msg:
                            #print('stop')
                            time.sleep(0.001)        
            for var in reslines[1:]:
                data.writelines(var)
            data.close()
            
            
        else:
            #如果为空调用爬取整个的程序
            browser.get('http://fund.eastmoney.com/f10/jjjz_'+part[:-4]+'.html')
            #先试试能不能打开网页
            try:
                #输出标题
                a=browser.find_element_by_xpath('//*[@id="jztable"]/table/thead/tr').text
            #无法打开网页就跳出，然后显示不行的基金代码
            except  NoSuchElementException as msg:
                     print('wrong:'+part[:-4])
            else:
                #输出抬头
                data =  open('C:/Users/章鱼哥/Desktop/证券分析/基金/data/stock_fund/'+part[:-4]+'.txt',"w+")
                data.write(a+'\n')
                #输出内容（数据）
                while browser.find_element_by_xpath("//label[text()='下一页']").value_of_css_property('color')=='rgba(3, 42, 143, 1)':
                    rowCount = len(browser.find_elements_by_xpath('//*[@id="jztable"]/table/tbody/tr'))
                    for i in range(1,rowCount+1):
                        a=browser.find_element_by_xpath('//*[@id="jztable"]/table/tbody/tr['+str(i)+']').text
                        data.write(a+'\n')
                    #点击下一页
                    nextpage=browser.find_element_by_xpath("//label[text()='下一页']")
                    nextpage.click()
                    #看看加载完了吗，没有的话就继续等待
                    i=1
                    while i:
                            try:
                                a=browser.find_element_by_xpath('//*[@id="jztable"]/table/tbody/tr[1]').text
                                i=0;
                            except (StaleElementReferenceException,NoSuchElementException) as msg:
                                #print('stop')
                                time.sleep(0.001)
                data.close()
                    



