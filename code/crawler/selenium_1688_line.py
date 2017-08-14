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

def click_province():
    #这里不点击的话，下面可以通过属性获取省份名称，但是直接使用text是不行的
    li_labels = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select ul.h li span.inner')))
    li_labels[1].click()
    
def click_city():
    li_labels = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select ul.h li span.inner')))
    li_labels[2].click()
        
def main():
 
    #打开URL
    browser.get('https://56.1688.com/order/price/estimate_price.htm')
    
    #输出浏览器标题
    print('browser title: ',browser.title)
    
    #单击发货输入框
    input_start = wait.until(EC.presence_of_element_located((By.ID,'source-area')))
    input_start.click()
    
    click_province()
    
   
    #区域信息
    div_tab = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select div.s-tab-b')))
    
    #只使用省份
    li_provinces = div_tab[1].find_elements(By.CSS_SELECTOR ,'a.panel-item')
    
    file = open('1688_line.txt','w')
    
    #遍历每一个省份
    for pro in li_provinces:
       # print(pro.get_attribute('code'),pro.get_attribute('panel-item'))
        pro.click()
        
        #每一次选择完省份后，页面会跳转
        #click_province()
        
        #获取城市信息
        div_tab = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select div.s-tab-b')))
        li_citys = div_tab[2].find_elements(By.CSS_SELECTOR ,'a.panel-item')

        data = []
        #遍历每一个城市
        for city in li_citys:
            #print(city.get_attribute('code'),city.get_attribute('panel-item'))
            city.click()
            
            #获取区县信息
            div_tab = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'#source-area-select div.s-tab-b')))
            li_areas = div_tab[3].find_elements(By.CSS_SELECTOR ,'a.panel-item')
            
            
            #遍历每一个区县
            for area in li_areas:
               # print(pro.get_attribute('code'),pro.get_attribute('panel-item'),
                #      city.get_attribute('code'),city.get_attribute('panel-item'),
                #      area.get_attribute('code'),area.get_attribute('panel-item'))
                data.append(pro.get_attribute('code')+','+pro.get_attribute('panel-item')
                            +','+city.get_attribute('code')+','+city.get_attribute('panel-item')
                            +','+area.get_attribute('code')+','+area.get_attribute('panel-item')
                            +'\n'
                            )
            
            
            click_city()
        
        file.writelines(data)
        click_province()
        
        
    file.close()
    browser.quit()

    

        
        
if __name__=='__main__':
    main()