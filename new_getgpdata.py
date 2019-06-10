

#
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 15:18:46 2019

@author: 章鱼哥
"""
import urllib.request
import re
from selenium import webdriver
import time
import os
import copyfile

time.strftime('%Y-%m-%d',time.localtime(time.time()))
stock_CodeUrl = 'http://quote.eastmoney.com/stocklist.html'

#获取股票代码列表
def urlTolist(url):
    allCodeList = []
    html = urllib.request.urlopen(url).read()
    html = html.decode('gbk')
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    for item in code:
        if item[0]=='6' or item[0]=='3' or item[0]=='0':
            allCodeList.append(item)
    return allCodeList
#查看有个多少个股票
#a=urlTolist(stock_CodeUrl);
#b=len(a)
#print(b)    

#将temp下载好的数据移动到data目标文件中
def tempmovedata():
    rooturl=r"C:\Users\章鱼哥\Desktop\证券分析\gpdata"
    temp_url=rooturl+"\\"+'temp'+"\\"
        #temp\
    for root, dirs, files in os.walk(temp_url):  
        print(root) #当前目录路径  
        print(dirs) #当前路径下所有子目录  
        print(files) #当前路径下所有非目录子文件
        srcfile_name=files
    #识别是不是理财产品还是股票基金
    for name in srcfile_name:
        srcfile=temp_url+"\\"+name
        dstfile=rooturl+"\\"+'data'+"\\"+name[:6]+".csv"
        copyfile.movefile(srcfile,dstfile)
        
#tempmovedata()
#如果要跟新运行下面这一个
def upgrade():
    options = webdriver.ChromeOptions()
    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'C:\\Users\\章鱼哥\\Desktop\\证券分析\\gpdata\\temp\\'}
    options.add_experimental_option('prefs', prefs)
   # options.add_argument('--headless')
    browser = webdriver.Chrome(r'C:\Users\章鱼哥\AppData\Local\Google\Chrome\Application\chromedriver.exe',chrome_options=options) 
    browser.maximize_window()
    time.sleep(1) 
    allCodelist = urlTolist(stock_CodeUrl)
    today=time.strftime('%Y%m%d',time.localtime(time.time()))
    #6开头的加0 其他的加1
    for part in allCodelist: 
        print(part)
        if(part[0]=='6'):
            browser.get('http://quotes.money.163.com/service/chddata.html?code=0'+part+'&start=19501105&end='+today+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP')
            print('+1')
        else :
            browser.get('http://quotes.money.163.com/service/chddata.html?code=1'+part+'&start=19501105&end='+today+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP')
            print('+0')
    tempmovedata()
#upgrade()

    

