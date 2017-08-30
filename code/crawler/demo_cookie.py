# -*- coding: utf-8 -*-
"""
<<<<<<< HEAD
Created on Wed Aug 30 09:16:06 2017

@author: yuguiyang
"""

import http.cookiejar, urllib.request

#定义一个文件，保存cookie信息
cookie = http.cookiejar.MozillaCookieJar('cookie.txt')
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

user_info = {
        'isValidate': 'true',
        'password': 'ab96c9532fdd334852aaad963469af6a'
        'request_form_verifyCode':'',
        'submit':'',
        'username':'15900597509'
        }

#<class 'http.client.HTTPResponse'>
r = opener.open("https://www.lagou.com/")

#页面信息
html = r.read().decode('utf-8')
#将cookie保存到上面的文件
cookie.save(ignore_discard=True, ignore_expires=True)

print(cookie)
#遍历输出cookie的信息
for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)

#print(html)
=======
Created on Tue Aug 22 21:15:36 2017

@author: hexo
"""


from urllib import request

>>>>>>> 73c1ef0f09e6b37143cd18a4ca23cdd5fe696552
