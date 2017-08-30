# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:06:08 2017

@author: yuguiyang

模拟登录豆瓣
"""

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
    'Host':'www.douban.com',
    'Connection':'keep-alive'
}
    
## 登录界面，有的时候，会有验证码，
login_url = r'https://www.douban.com/accounts/login'

#1.先访问登录界面，然后解析界面，判断是否有验证码

#2.查看登录页面
s = requests.session()

rp = s.get(login_url)

print(rp.url)
#3. 解析页面
soup = BeautifulSoup(rp.text, "html.parser")

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

rp = s.post(login_url,user_info, headers)

rp = s.post('https://www.douban.com/people/156645141/', headers)
with open('test.html','w',encoding='utf-8') as file:
    file.write(rp.text)

#print(rp.text)j 
