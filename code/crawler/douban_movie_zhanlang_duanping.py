# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 12:52:29 2017

@author: yuguiyang
"""


import requests
from bs4 import BeautifulSoup
import psycopg2
import time
from datetime import datetime
 
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#从浏览器复制的cookie
cookies = {'cookie':'bid=4Ppptf_DEyk; push_noty_num=0; push_doumail_num=0; __utma=30149280.961886527.1504079761.1504236929.1504241388.3; __utmc=30149280; __utmz=30149280.1504236929.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmv=30149280.15664; ap=1; ll="108296"; __utma=223695111.1000436152.1504081407.1504236938.1504241388.3; __utmc=223695111; __utmz=223695111.1504236938.2.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _pk_id.100001.4cf6=a804767ad70f04e7.1504081407.3.1504241403.1504236988.; ct=y; ps=y; _ga=GA1.2.961886527.1504079761; dbcl2="156645141:anOKSKef13E"; ck=PO7v; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1504241388%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _vwo_uuid_v2=45E0E88C8B2C047C8B135B77EB60F957|6fa7a4b4e5d5cdc0cf6b28794b6031e2; _pk_ses.100001.4cf6=*; __utmb=30149280.0.10.1504241388; __utmb=223695111.0.10.1504241388'}
#我们要访问的url
url = 'https://movie.douban.com/subject/26363254/comments?start={0}&limit=20&sort=new_score&status=P'

conn = psycopg2.connect(database="pydemo", user="postgres", password="shishi", host="127.0.0.1", port="5432")

def parseHtml(url):
    #使用get方式，访问页面，传入cookie
    rsp = requests.get(url, cookies=cookies,headers=headers)
    rsp.encoding = 'utf-8'
    
    return rsp.text

def save2PG(comments):
    cur = conn.cursor()
    for c in comments:
        cur.execute('insert into tm_zhanlang_comment(m_comment) values(%s)',[c])
    conn.commit()
    
    
#解析当前页面        
def parseCurrentPage(url,pageno):
    html = parseHtml(url.format(pageno))
    soup = BeautifulSoup(html, "html.parser")
    
    #获取评论信息
    p_comments = soup.select('div#comments div.comment p')

    p_lines=[]
    for com in p_comments:
        p_lines.append(com.contents[0].strip())
    
    save2PG(p_lines)
    
    #获取下一页信息，可以通过这个获取数据
    p_next = soup.select_one('div#paginator a.next')
    next_start = None
    print(p_next)
    #上一次8745次的时候，会跳出验证码程序，
    #1.先尝试sleep一会儿试试，
    #2.解析验证码，接入打码平台
    #3.使用代理，IP代理，多用户
    if p_next:
        tmp = p_next['href']
        next_start = tmp[tmp.find('=')+1:tmp.find('&')]
    else :
        #出现验证码
        print('you need to see.')
        input('gogoo')
        next_start = pageno
    
    return next_start

def main():
    next_start = parseCurrentPage(url,30047)
    
    start = datetime.now()
    while next_start:
        print(next_start)
        next_start = parseCurrentPage(url,next_start)
        
        #大于60s，则休息5秒
        end = datetime.now()
        if (end - start).seconds > 60:
            print('start to sleep')
            time.sleep(5)
            start = datetime.now()
    

if __name__=='__main__':
    main()
