# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
        
def main():
    #打开URL
    browser.get('http://www.stats.gov.cn/tjsj/tjbz/xzqhdm/201703/t20170310_1471429.html')
    
    #输出浏览器标题
    print('browser title: ',browser.title)
    
    #数据更新信息
    areas = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.TRS_PreAppend p.MsoNormal')))
    
    file = open('area.txt','w')
    for i in areas:
        file.write(i.text[:6]+','+i.text[7:].strip()+'\n')
    
    file.close()
    #输出当前页信息
    #show_current_page()
    browser.quit()

        
        
if __name__=='__main__':
    main()