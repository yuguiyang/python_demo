# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

#打开浏览器
browser = webdriver.Firefox()
#设置等待时长，最长等待10s
wait = WebDriverWait(browser,10)

#定义电影排名
comment_index = 0

#定义一个movie
class Movie:
    
    __movie_id = 0
    __movie_name = ''
    __movie_star = ''
    __movie_releasetime = ''
    __movie_score = ''
    
    def __init__(self , movie_id,movie_name,movie_star,movie_releasetime,movie_score):
        self.__movie_id = movie_id
        self.__movie_name = movie_name
        self.__movie_star = movie_star
        self.__movie_releasetime = movie_releasetime
        self.__movie_score = movie_score
        
    def show(self):
        print('影片排名: ', self.__movie_id)
        print('影片名称: ', self.__movie_name)
        print(self.__movie_star)
        print(self.__movie_releasetime)
        print('影片评分', self.__movie_score)
        print('')
        
    def simple_list(self):
        return [self.__movie_id, self.__movie_name, self.__movie_star, self.__movie_releasetime, self.__movie_score]
        
def save2csv(movie_list):
    with open('movie.csv', 'a', newline='',encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        for m in movie_list:
            csv_writer.writerow(m.simple_list())
    
        csvfile.close()
        
        
def main():
    #打开URL
    browser.get('http://maoyan.com/board/4')
    
    #输出浏览器标题
    print('browser title: ',browser.title)
    
    #数据更新信息
    p_update_info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.main p.update-time')))
    print('更新信息: ',p_update_info.text)
    
    #输出当前页信息
    show_current_page()
    

def show_current_page():
    print('-----------------------------------')
    print('current url: ',browser.current_url)
    
    #获取当前页信息
    div_page = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.pager-main li.active')))
    print('current page: ',div_page.text)
    
    #当前页总数量
    div_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,'div.main div.board-item-main div.board-item-content')))
    print('total count: ',len(div_items))
    
    movie_list = []
    #结果集有很多结果，我们获取
    for item in div_items:
        #调用全局变量
        global comment_index
        comment_index += 1
        
        #获取我们需要的信息
        p_name = item.find_element_by_css_selector('div.movie-item-info p.name')
        
        p_star = item.find_element_by_css_selector('div.movie-item-info p.star')
        
        p_releasetime = item.find_element_by_css_selector('div.movie-item-info p.releasetime')
        
        p_score_integer = item.find_element_by_css_selector('div.movie-item-number p.score i.integer')
        p_score_fraction = item.find_element_by_css_selector('div.movie-item-number p.score i.fraction')

        #初始化movie对象
        m = Movie(comment_index , p_name.text , p_star.text, p_releasetime.text, p_score_integer.text+p_score_fraction.text)
        movie_list.append(m)
    
    save2csv(movie_list)
    #获取下一页
    show_next_page()


def show_next_page():
    try:
        #获取下一页的标签
        #最后1页，没有下一页标签
        a_next = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT,'下一页')))
        a_next.click()
        
        show_current_page()
    except TimeoutException:
        #找不到下一页
        print('get all movies.')
        #也有可能真是网络异常
    finally:
        browser.quit()
        
        
if __name__=='__main__':
    main()