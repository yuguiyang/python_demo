# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 15:22:20 2017

@author: yuguiyang
"""

import urllib
import json
import math
import csv
import time
import os

total_page = 1
current_page = 1

#更新结果集的总页数
def update_total_page(page_size,totalCount):
    global total_page
    
    total_page = math.ceil(totalCount/page_size)
    

#解析HTML页面
def parse_html(url,headers,post_data):
    post_data = urllib.parse.urlencode(post_data).encode('utf-8')
    req = urllib.request.Request(url,headers=headers,data=post_data)
    page = urllib.request.urlopen(req)
    
    return page.read().decode('utf-8')
    
#解析返回的json数据
def parse_result(html):
    data_json = json.loads(html)
    print(data_json['content']['pageNo'])
    
    #第一页的话，更新下总页数
    if data_json['content']['pageNo'] == 1 :
        update_total_page(data_json['content']['pageSize'],data_json['content']['positionResult']['totalCount'])

    #将结果保存到csv文件
    with open('lagou_shujufenxi_data.csv','a',newline='',encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile,quotechar='"',quoting=csv.QUOTE_MINIMAL)
        #在第一页的时候，写入标题
        if data_json['content']['pageNo'] == 1 :
            csv_writer.writerow(['公司简称','公司全称','所属行业','工作地点','职位特点','薪资','经验','职位名称','firstType','secondType'])
        
        #遍历招聘信息
        for job in data_json['content']['positionResult']['result']:
            line = []
            line.append(job['companyShortName'])
            line.append(job['companyFullName'])
            line.append(job['industryField'])
            line.append(job['district'])
            line.append(job['positionAdvantage'])
            line.append(job['salary'])
            line.append(job['workYear'])
            line.append(job['positionName'])
            line.append(job['firstType'])
            line.append(job['secondType'])
            
            csv_writer.writerow(line)

def main():
    headers = {
            'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'Referer':r'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput',
            'Host':'www.lagou.com'
            }
            
    url = 'https://www.lagou.com/jobs/positionAjax.json'
    
    #判断要导出的文件是否存在
    if os.path.exists(r'lagou_shujufenxi_data.csv'):
        print('hey,delete the file')
        os.remove(r'lagou_shujufenxi_data.csv')
    
    global current_page
    global total_page
    #循环所有页数，取导出数据    
    while current_page <= total_page:
        #post参数,每次修改页码就行了
        post_data = {'city':'上海','isSchoolJob':'0','needAddtionalResult':'false','kd':'数据分析','pn':current_page}
        #解析每一个页面
        html = parse_html(url ,headers, post_data)
        #处理获取的json数据
        parse_result(html)
        
        #当前页码加1
        current_page += 1
        
        #这里sleep5秒，不停一下，偶尔会报错
        time.sleep(5)
    
if __name__=='__main__':
    main()