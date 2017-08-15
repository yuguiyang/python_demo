# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 21:20:56 2017

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

#单击省份标签
def click_province():
    #这里不点击的话，下面可以通过属性获取省份名称，但是直接使用text是不行的
    li_labels = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select ul.h li span.inner')))
    li_labels[1].click()

#单击城市标签    
def click_city():
    li_labels = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select ul.h li span.inner')))
    li_labels[2].click()
        
def main():
 
    #打开URL
    browser.get('https://56.1688.com/order/price/estimate_price.htm')
    
    #输出浏览器标题
    print('browser title: ',browser.title)
    
    #单击发货输入框，显示城市选择的标签
    input_start = wait.until(EC.presence_of_element_located((By.ID,'source-area')))
    input_start.click()
    
    #单击省份标签
    click_province()
    
   
    #区域信息
    div_tabs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select div.s-tab-b')))
    
    #只使用省份
    li_provinces = div_tabs[1].find_elements(By.CSS_SELECTOR ,'a.panel-item')
    
    file = open('1688_line.txt','w')
    
    #遍历每一个省份
    for pro in li_provinces:
        #单击当前的省份，页面会跳转到该省份的城市列表
        pro.click()
        
        #获取城市信息
        div_tabs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select div.s-tab-b')))
        li_citys = div_tabs[2].find_elements(By.CSS_SELECTOR ,'a.panel-item')

        data = []
        #遍历每一个城市
        for city in li_citys:
            #单击当前城市标签，页面会跳转到该城市下的区县列表
            city.click()
            
            #获取区县信息
            div_tabs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select div.s-tab-b')))
            li_areas = div_tabs[3].find_elements(By.CSS_SELECTOR ,'a.panel-item')
            
            
            #遍历每一个区县
            for area in li_areas:
                data.append(pro.get_attribute('code')+','+pro.get_attribute('panel-item')
                            +','+city.get_attribute('code')+','+city.get_attribute('panel-item')
                            +','+area.get_attribute('code')+','+area.get_attribute('panel-item')
                            +'\n'
                            )
            
            #跳转回到城市标签，为了遍历下一个城市
            click_city()
        
        #将数据写入文件
        file.writelines(data)
        #跳转回省份标签，为了遍历下一个省份
        click_province()
        
        
    file.close()
    browser.quit()


if __name__=='__main__':
    main()