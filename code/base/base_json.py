# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:56:56 2017

@author: yuguiyang
"""

import json

with open('../crawler/lagou_shujufenxi_data.json','r') as file:
    data = file.read()
    data_json = json.loads(data)
    print(data_json['content']['pageNo'])
    print(data_json['content']['pageSize'])
    print(data_json['content']['positionResult']['totalCount'])
    #print(data_json['content']['positionResult']['locationInfo'])
    #print(data_json['content']['positionResult']['queryAnalysisInfo'])
    for job in data_json['content']['positionResult']['result']:
        print('公司简称:',job['companyShortName'])
        print('公司全称:',job['companyFullName'])
        print('所属行业:',job['industryField'])
        print('工作地点:',job['district'])
        print('职位特点:',job['positionAdvantage'])
        print('薪资:',job['salary'])
        print('经验:',job['workYear'])
        print('职位名称:',job['positionName'])
        print('firstType:',job['firstType'])
        print('secondType:',job['secondType'])
        print('------------------------------')
    