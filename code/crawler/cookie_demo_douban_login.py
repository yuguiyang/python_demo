# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:06:08 2017

@author: yuguiyang

模拟登录豆瓣
"""

import http.cookiejar, urllib
from bs4 import BeautifulSoup
import requests

user_info = {
    'form_email':'15900597509',
    'form_password':'!!@@ygy6157177',
    'login':u'登录',
    'redir':'https://www.douban.com/',
    'source':'index_nav'
}



headers = {
    'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Referer':r'https://accounts.douban.com/login',
    'Host':'accounts.douban.com',
    'Connection':'keep-alive'
}
    
## 登录界面，有的时候，会有验证码，
login_url = r'https://accounts.douban.com/login'

#1.先访问登录界面，然后解析界面，判断是否有验证码

###cookie
cookie = http.cookiejar.MozillaCookieJar('douban_cookie.txt')
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

#2.查看登录页面
post_data = urllib.parse.urlencode(user_info).encode('utf-8')
rq = urllib.request.Request(login_url, post_data, headers)

login_html = opener.open(rq).read().decode('utf-8')

#3. 解析页面
soup = BeautifulSoup(login_html, "html.parser")

#判断验证码是否存在
captcha = soup.find('img', id='captcha_image')
if captcha:
    captcha_url = captcha['src']
    
    print('captcha_url:',captcha_url)
    
    captcha_id = soup.find(attrs={'name':'captcha-id','type':'hidden'})
    print('captcha_id:',captcha_id['value'])
    
    captcha_text = input('输入验证码:\n')
    user_info['captcha_id'] = captcha_id['value']
    user_info['captcha-solution'] = captcha_text
    
print(user_info)

post_data = urllib.parse.urlencode(user_info).encode('utf-8')

rq = urllib.request.Request(login_url, post_data, headers)

response = opener.open(rq)

page = response.read().decode('utf-8')
#这里貌似是登录成功的，但是没有办法跳转，跳转后依然会显示要登录
print(page)

#将cookie保存到上面的文件
cookie.save(ignore_discard=True, ignore_expires=True)


#遍历输出cookie的信息
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)
    

