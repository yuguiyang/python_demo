# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 13:42:30 2017

@author: hexo
"""

import numpy as np
import pandas as pd

#读取第一个sheet页
df = pd.read_excel('D:\Tableau_data\示例 - 超市.xls',sheetname=0)

print(type(df))

#每一列的数据类型
print(df.dtypes)
#每种类型的数量
print(df.get_dtype_counts())

#还不知道这个ftype到底是干嘛的，sparse|dense，稀疏|密集，表示什么呢？
print(df.ftypes)
print(df.get_ftype_counts())

top_10_data=df.head(10)

#print(top_10_data)

print('----------------------------')
#axis=0表示纵轴，axis=1表示横轴
#这是每一列，每一列的均值
print(top_10_data.mean(axis=0))
print('----------------------------')
#这是每一行，每一行的均值
print(top_10_data.mean(axis=1))

print('----------------------------')
#sort_index
#坑啊，这个axis到底是个什么鬼(ok)
#但是这个level是干嘛的依然没有搞懂
#按第1列降序排列
#print(top_10_data.sort_index(axis=0,level=0,ascending=True))
#print(top_10_data.sort_index(axis=0,level=1,ascending=True))

print(top_10_data)
print('----------------------------')
#终于成功按照订单日期降序排列了！！！
#这里按多了排序的话，貌似只可以执行一个排序方式，都是降序
print(top_10_data.sort_values(by=['订单日期','行 ID'] , ascending=False).head(2))





