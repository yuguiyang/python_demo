# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 17:12:40 2017

@author: yuguiyang
"""

from HTMLParser import HTMLParser
import requests
def _attr(attrs, attrname):
    for attr in attrs:
        if attr[0] == attrname:
            return attr[1]
    return None
#获得验证码信息
def _get_captcha(content):
    class CaptchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_id = None
            self.captcha_url = None
        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs,'type') == 'hidden' and _attr(attrs,'name') == 'captcha_id':
                self.captcha_id = _attr(attrs,'value')
            if tag == 'image' and _attr(attrs,'id') == 'captcha_image' and _attr(attrs,'class') == 'captcha_image':
                self.captcha_url == _attr(attrs,'src')
    p = CaptchaParser()
    p.feed(content)
    return p.captcha_id, p.captcha_url
#获得ck属性的值
def _get_ck(content):
    class CKParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.ck = None
        def handle_starttag(self, tag, attrs):
            if tag == 'input' and _attr(attrs,'type') == 'hidden' and _attr(attrs,'name') == 'ck':
                self.ck = _attr(attrs,'value')
    p =CKParser()
    p.feed(content)
    return p.ck
class DoubanClient(object):
    def __init__(self):
        object.__init__(self)
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.84 Safari/537.36',
                   'origin':'http/www.douban.com'}
        #create requests session
        self.session = requests.session()
        #对session的头进行定制，这样以后，以后所有的请求都会包含上面headers中的数据
        self.session.headers.update(headers)
    #登录豆瓣
    def login(self,username,password,source='index_nav',
              redir = 'http://www.douban.com/',login = '登录'):
        url = 'https://www.douban.com/accounts/login'
        #access login page to get captcha
        #湖区登录界面中的验证码图片
        #r = requests.get(url)
        #应为登录和修改签名在同一个session中，故使用session.get(url)的方式登录
        r = self.session.get(url)
        (captcha_id,captcha_url) = _get_captcha(r.content)
        if captcha_id:
            print(captcha_url)
            captcha_solution = input('please input solution for')
        #post login request
        data = {'from_email':username,'from_passwd':password,'source':source,
                'redir':redir,'login':login}
        #将验证信息加入到post data中
        if captcha_id:
            data['captcha_id'] = captcha_id
            data['captcha_url'] = captcha_url
        headers = {'referer':'http://www.douban.com/accounts/login?source=main',
                   'host':'accounts.douban.com'}
        #r = requests.post(url,data=data,headers=headers)
        r = self.session.post(url,data=data,headers=headers)
        print(self.session.cookies.items())
    
    #编辑签名
    def edit_signature(self,username,signature):
        #access user's homepage
        url = 'https://www.douban.com/people/%s/' % username
        r  = self.session.get(url)
        #从操作页面的HTML代码中获取post data数据中参数ck的值
        ck = _get_ck(r.content)
        #post request to change signature
        url = 'https://www.douban.com/j/people/%s/edit_signature' % username
        headers = {'referer':url,'host':'www.douban.com',
                 'x-requested-with':'XMLHTTPRequest'}
        data = {'ck':ck,'signature':signature}
        r = self.session.post(url,data=data,headers=headers)
        print(r.content)
        
if __name__ == '__main__':
    c = DoubanClient()
    c.login('15900597509','!!@@ygy6157177')
    #c.edit_signature('146925119','Hello')
   







