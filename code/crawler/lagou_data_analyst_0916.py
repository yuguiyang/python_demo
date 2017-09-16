# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:25:31 2017

@author: yuguiyang
"""

import json
import math
import csv
import time
import os
import requests
import psycopg2

total_page = 1
current_page = 1

conn = psycopg2.connect(database="pydemo", user="postgres", password="shishi", host="127.0.0.1", port="5432")



#更新结果集的总页数
def update_total_page(page_size,totalCount):
    global total_page
    print('page_size',page_size)
    print('totalCount',totalCount)
    total_page = math.ceil(totalCount/page_size)
    

def save2PG(jobs):
    cur = conn.cursor()
    #print(jobs)
    cur.execute('INSERT INTO public.tm_lagou_data(city, company_short_name, company_full_name, company_industry,company_location, position_advantage, position_salary, position_workyear,position_name,position_first_type, position_second_type, position_lables, position_id,create_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',jobs)
    conn.commit()
    
    
#解析HTML页面
def parse_html(url,post_data):
    headers = {
            'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
            'Referer':r'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput',
            'Host':'www.lagou.com'
    }
    
    cookies = r'user_trace_token=20170830104712-c9f61baf-00fe-4ab7-9ef4-a0a2de890a87; _ga=GA1.2.1867481716.1504061233; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1504055816,1504061233,1505383105,1505487770; LGUID=20170830104712-86865616-8d2d-11e7-96df-525400f775ce; index_location_city=%E4%B8%8A%E6%B5%B7; _gid=GA1.2.246867487.1505487770; SEARCH_ID=735baaebfe9544dab5ba23160d857df1; JSESSIONID=ABAAABAAAGFABEF61B9756CD1DCF8ACD838844175D85DB0; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1505572628; LGRID=20170916223701-80a614d3-9aec-11e7-9536-525400f775ce; X_HTTP_TOKEN=ba0238ab10e43dacc7636bb0e9fa9af3; TG-TRACK-CODE=index_search; LGSID=20170916221839-efa29369-9ae9-11e7-9196-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3Fcity%3D%25E4%25B8%258A%25E6%25B5%25B7%26cl%3Dfalse%26fromSearch%3Dtrue%26labelWords%3D%26suginput%3D; _gat=1'
    
    a = cookies.split(';')
    x = {}
    for s in a:
        t = s.split('=')
        x[t[0]]=t[1]

    r = requests.post(url,data = post_data,headers=headers,cookies=x)
    
    return r.text
    
#解析返回的json数据
def parse_result(html):
    data_json = json.loads(html)
    # print(data_json)
    print(data_json['content']['pageNo'])
    
    #第一页的话，更新下总页数
    if data_json['content']['pageNo'] == 1 :
        update_total_page(data_json['content']['pageSize'],data_json['content']['positionResult']['totalCount'])

    #将结果保存到csv文件
    with open('lagou_shujufenxi_data.csv','a',newline='',encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile,quotechar='"',quoting=csv.QUOTE_MINIMAL)
        #在第一页的时候，写入标题
        if data_json['content']['pageNo'] == 1 :
            csv_writer.writerow(['city','公司简称','公司全称','所属行业','工作地点','职位特点','薪资','经验','职位名称','firstType','secondType','职位标签','positionId','createTime'])
        
        city_info = data_json['content']['positionResult']['locationInfo']['city']
        #遍历招聘信息
        for job in data_json['content']['positionResult']['result']:
            line = []
            line.append(city_info)
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
            line.append(','.join(job['positionLables']))
            line.append(job['positionId'])
            line.append(job['createTime'])
            
            csv_writer.writerow(line)
            # print(line)
            save2PG(line)

def main():            
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
        post_data = {'city':'深圳','isSchoolJob':'0','needAddtionalResult':'false','kd':'数据分析','pn':current_page}
        #解析每一个页面
        html = parse_html(url, post_data)
        #处理获取的json数据
        parse_result(html)
        
        #当前页码加1
        current_page += 1
        
        #这里sleep5秒，不停一下，偶尔会报错
        time.sleep(3)
    
if __name__=='__main__':
    main()