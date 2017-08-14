# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:42:30 2017

@author: hexo
"""

import numpy as np
import pandas as pd

#读取第一个sheet页
df = pd.read_excel('D:\Tableau_data\示例 - 超市.xls',sheetname=0)

top_10_data = df.head(10)

#print(top_10_data)

d1 = top_10_data.loc[top_10_data['订单日期'] != '2014-10-31']
print(d1)

print(d1.dtypes)
a=np.datetime64('2017-01-01')
print(a)
print(type(a))




