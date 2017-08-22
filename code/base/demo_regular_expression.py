# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:55:22 2017

    正则表达式练习
    
@author: yuguiyang
"""

import re

#re.match,尝试从字符串起始位置开始匹配，
#如果不是起始位置匹配成功的话，match就返回None
#re.match(pattern, string, flags=0)
s1 = 'www.baidu.com,www.sina.com,www.google.com'
obj = re.match(r'(w*)\.(.*)\.(com)',s1)
for o in obj.groups():
    print(o)
print(re.match('com',s1))

#可以使用group(num),groups匹配对象函数来匹配表达式
 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print("matchObj.group() : ", matchObj.group())
   print("matchObj.group(1) : ", matchObj.group(1))
   print("matchObj.group(2) : ", matchObj.group(2))
   for g in matchObj.groups():
       print(g)

else:
   print("No match!!")
   
#疑问1：怎么匹配分割，就是获取匹配的数据

'''
re.search(pattern, string, flags=0)
扫描整个字符串，并返回第一个
'''



