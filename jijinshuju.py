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
browser = webdriver.Chrome(r'C:\Users\章鱼哥\AppData\Local\Google\Chrome\Application\chromedriver.exe')
browser.maximize_window() 
#获取基金代码
f = open(r"C:\Users\章鱼哥\Desktop\证券分析\基金\jijindaima.txt")
line = f.readline()
data_list = []
#大循环基金代码
while line:
    if line>='0':
        print (line),                 # 后面跟 ',' 将忽略换行符
        data_list.append(line[:-1])
        browser.get('http://fund.eastmoney.com/f10/jjjz_'+line+'.html')
        #先试试能不能打开网页
        try:
            #输出标题
            a=browser.find_element_by_xpath('//*[@id="jztable"]/table/thead/tr').text
        #无法打开网页就跳出，然后显示不行的基金代码
        except  NoSuchElementException as msg:
                 print('wrong:'+line)
        else:
            #输出抬头
            data =  open('C:/Users/章鱼哥/Desktop/证券分析/基金/data/'+line[:-1]+'.txt',"w+")
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
    line = f.readline()
f.close()


