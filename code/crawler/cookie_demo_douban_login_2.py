# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:06:08 2017

@author: yuguiyang

模拟登录豆瓣
"""
import requests

 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#从浏览器复制的cookie
cookies = {'cookie':'bid=4Ppptf_DEyk; _pk_id.100001.8cb4=9ebccf76e16f2d72.1504079761.1.1504080394.1504079761.; _pk_ses.100001.8cb4=*; push_noty_num=0; push_doumail_num=0; __utma=30149280.961886527.1504079761.1504079761.1504079761.1; __utmb=30149280.13.10.1504079761; __utmc=30149280; __utmz=30149280.1504079761.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=30149280.15664; ap=1; ll="108296"; __utmt=1; dbcl2="156645141:qrDbtHgy+Fg"; ck=SG18'}
#我们要访问的url
url = 'http://www.douban.com'

#使用get方式，访问页面，传入cookie
r = requests.get(url, cookies=cookies,headers=headers)
r.encoding = 'utf-8'

with open('home_douban.html','w',encoding = 'utf-8') as f:
    f.write(r.text)