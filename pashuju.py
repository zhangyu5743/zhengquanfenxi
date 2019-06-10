# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:11:02 2019

@author: 章鱼哥
"""
import numpy as np
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
browser = webdriver.Chrome(r'C:\Users\章鱼哥\AppData\Local\Google\Chrome\Application\chromedriver.exe')
browser.maximize_window() 
f = open(r"C:\Users\章鱼哥\Desktop\证券分析\gpdaima.txt")
line = f.readline()
data_list = []
while line:
    if line>='0':
        print (line),                 # 后面跟 ',' 将忽略换行符
        data_list.append(line[:-1])
        browser.get('http://quotes.money.163.com/trade/lsjysj_'+line[:-1]+'.html#06f01')
        # =============================================================================
        # input = browser.find_element_by_id('downloadData')#找到搜索框
        # input.send_keys('001986')#传送入关键词
        # =============================================================================
        try:
            button = browser.find_element_by_class_name('download_link')
        
        except  NoSuchElementException as msg:
                 print('wrong:'+line)
        else:
                button.click()
                begin = browser.find_element_by_xpath('//*[@id="dropBox1"]/div[2]/form/table[2]/tbody/tr[1]/td[2]/input[3]')
                begin.click()
                begin = browser.find_element_by_xpath('//*[@id="dropBox1"]/div[2]/form/table[2]/tbody/tr[2]/td[2]/input[3]')
                begin.click()
                begin = browser.find_element_by_xpath('//*[@id="dropBox1"]/div[2]/form/div[3]/a[1]')
                begin.click()
        #print(browser.page_source)#browser.page_source是获取网页的全部html
        #browser.close()
    line = f.readline()
f.close()


