# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 09:29:24 2017

@author: yuguiyang
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#打开浏览器
browser = webdriver.Firefox()
#设置等待时长，最长等待10s
wait = WebDriverWait(browser,10)

def initial_lines():
    path = r'D:\Users\yuguiyang\Documents\GitHub\python_demo\code\crawler\1688_line.txt'
    
    file = open(path,'r')
    
    line = file.readline()
    
    lines = []
    while line:
        tmp = line.split(',')
        lines.append([tmp[0],tmp[2],tmp[4]])
        
        line = file.readline()
        
    file.close()
    
    return lines

def parse_current_page(url):
    #打开URL
    browser.get(url)
    
    #输出浏览器标题
    print('browser title: ',browser.title)
    
    #tab-body
    cmp_trs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.tab-body tr.iterable')))
    
    #browser.find_elements_by_tag_name
    #遍历每一行记录tr
    for tr in cmp_trs:
        cmp_tds = tr.find_elements_by_tag_name('td')
        
        td_company_name = cmp_tds[0].text
        
        #查看线路信息
        td_lines = cmp_tds[1].find_elements(By.CSS_SELECTOR,'span.weight-bold')
        td_line_from = td_lines[0].text
        td_line_to = td_lines[1].text
        
        td_time = cmp_tds[2].text.split('\n')[0].strip()
        td_type = cmp_tds[2].text.split('\n')[1]
        td_price_heavy = cmp_tds[3].text.split('\n')[0]
        td_price_light = cmp_tds[3].text.split('\n')[1]
        td_price_lowest = cmp_tds[3].text.split('\n')[2]
        td_eva = cmp_tds[4].text
        
        print('--------------------------------------')
        print('td_company_name:',td_company_name)
        print('td_line_from:',td_line_from)
        print('td_line_to:',td_line_to)
        print('td_time:',td_time)
        print('td_type:',td_type)
        print('td_price_heavy:',td_price_heavy)
        print('td_price_light:',td_price_light)
        print('td_price_lowest:',td_price_lowest)
        print('td_eva:\n',td_eva)
        print('\n')
    
        
def main():    
    p_url_template = 'https://56.1688.com/order/price/estimate_price.htm?_fm.es._0.s={0}&_fm.es._0.se={1}&_fm.es._0.sen={2}&_fm.es._0.r={3}&_fm.es._0.re={4}&_fm.es._0.rec={5}&notFirst=true&r=1502760547155&sizePerPage=&pageIndex=1'
    
    lines = initial_lines()
    
    for line_from in lines:
        for line_to in lines:
            p_url = p_url_template.format(line_from[0],line_from[1],line_from[2],line_to[0],line_to[1],line_to[2])
            
            try :    
                #循环，按行读取文件
                parse_current_page(p_url)    
            finally :
                browser.quit()
    

#统一转换时效为小时
def parse_time(str_time):
    if str_time=='1日' or str_time=='1天' or str_time=='次日达' or str_time=='次日':
        return 24
   # elif str_
    else :
        return str_time
        

        
        
if __name__=='__main__':
    main()