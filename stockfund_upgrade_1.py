# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 17:11:02 2019

@author: 章鱼哥
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import InvalidSelectorException
#from bs4 import BeautifulSoup
import time 
from selenium.webdriver.chrome.options import Options
def reload( fundnum ,rooturl,Chromeurl=r'C:\Users\章鱼哥\AppData\Local\Google\Chrome\Application\chromedriver.exe'):
    chrome_options=Options()
    #chrome_options.add_argument('--headless')
    chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
    browser = webdriver.Chrome(Chromeurl,chrome_options=chrome_options)
#获取现有基金代码
    browser.get('http://fund.eastmoney.com/f10/jjjz_'+fundnum+'.html')
        #先试试能不能打开网页
    try:
        #检验能否打开网站，不能的话就是没有该基金，可以的话就读取本地我呢见
        a=browser.find_element_by_xpath('//*[@id="jztable"]/table/thead/tr').text
    #无法打开网页就跳出，然后显示不行的基金代码
    except  NoSuchElementException as msg:
             print('网页打开有问题:'+fundnum+',应该是不存在该基金')
    else:
        #读取本地文件
        try:
            with open(rooturl+fundnum+'.txt',"r",errors='ignore') as res:
                reslines = res.readlines() 
                res.close()
        #如果没有的话就从头开始爬，可以的话就进行更新
        except IOError:
            print('没有原始文件有问题，现在重新下载ing，需要等待一分钟')
            #如果为空调用爬取整个的程序
            browser.get('http://fund.eastmoney.com/f10/jjjz_'+fundnum+'.html')
            #先试试能不能打开网页
            try:
                #输出标题
                a=browser.find_element_by_xpath('//*[@id="jztable"]/table/thead/tr').text
            #无法打开网页就跳出，然后显示不行的基金代码
            except  NoSuchElementException as msg:
                print('网页打开有问题，没有该基金数据:'+fundnum)
            else:
                #输出抬头
                data =  open(rooturl+fundnum+'.txt',"w+")
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
                print('已重新下载数据数据')
        else:#更新
            out=0
            #如果本地有文件但是是空的，那么就重新开始爬，如果数据草果两行那么就开始更新
            if(len(reslines)>2):
                   #输出抬头
                data =open(rooturl+fundnum+'.txt',"w+")
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
                print('已更新到最新数据')
                
            else:
                print('原始文件有问题，现在重新下载ing，需要等待一分钟')
                #如果为空调用爬取整个的程序
                browser.get('http://fund.eastmoney.com/f10/jjjz_'+fundnum+'.html')
                #先试试能不能打开网页
                try:
                    #输出标题
                    a=browser.find_element_by_xpath('//*[@id="jztable"]/table/thead/tr').text
                #无法打开网页就跳出，然后显示不行的基金代码
                except  NoSuchElementException as msg:
                         print('网页打开有问题:'+fundnum)
                else:
                    #输出抬头
                    data =  open(rooturl+fundnum+'.txt',"w+")
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
                    print('已重新下载数据数据')
    return


