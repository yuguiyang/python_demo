# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:13:24 2017

@author: yuguiyang
"""

import os
import urllib
from bs4 import BeautifulSoup

file_name = 'douban_movie_zhanlang.txt'

def getHtml(url):
    req = urllib.request.Request(url)
    page = urllib.request.urlopen(req).read().decode('utf-8')
    
    return page

def clearFile(file_name):
    if os.path.exists(file_name):
        os.remove(file_name)
    

def save2file(lines,file_name):
    with open(file_name,'a') as file:
        file.writelines(lines)
        
def parseCurrentPage(html):
    soup = BeautifulSoup(html, "html.parser")
    
    #获取评论信息
    p_comments = soup.select('div#comments div.comment p')

    p_lines=[]
    for com in p_comments:
        p_lines.append(com.contents[0].strip()+'\n')
    
    save2file(p_lines,file_name)
    
    #获取下一页信息
    p_next = soup.select_one('div#paginator a.next')
    print(p_next)
    print(p_next['href'])
    

def main():   
    global file_name
    clearFile(file_name)
    
    url = 'https://movie.douban.com/subject/26363254/comments?start=0&limit=20&sort=new_score&status=P'

    html = getHtml(url)
    
    parseCurrentPage(html)
    

if __name__=='__main__':
    main()