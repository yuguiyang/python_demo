# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 13:44:21 2017

@author: hexo
"""

import pandas as pd

import numpy as np

a = pd.DataFrame({'key':list('bbccaa'),'data1':np.random.randint(0,10,size=6)})

b = pd.DataFrame({'key':list('abc'),'data2':np.random.randint(0,10,size=3)})

a.merge(b)
a.merge(b,on='key')
a.merge(b,left_on='key',right_on='key')

c = pd.DataFrame({'lkey1':list('ab'),'lkey2':list('xy'),'ldata1':np.random.randint(0,10,size=2)})
d = pd.DataFrame({'rkey1':list('ab'),'rkey2':list('xy'),'ldata1':np.random.randint(0,10,size=2)})

c.merge(d)
c.merge(d,left_on=['lkey1','lkey2'],right_on=['rkey1','rkey2'])
c.merge(d,left_on=['lkey1','lkey2'],right_on=['rkey1','rkey2'],suffixes=['_left','_right'])
  

e = pd.DataFrame({'key':list('bbccaadd'),'data':np.random.randint(0,10,size=8)})
f = pd.DataFrame({'key':list('abcx'),'data':np.random.randint(0,10,size=4)})

e.merge(f,on='key')
e.merge(f,on='key',how='left')
e.merge(f,on='key',how='right')
e.merge(f,on='key',how='outer')

g = pd.DataFrame({'data':np.random.randint(0,10,size=3)},index=list('abc'))
e.merge(g,left_on='key',right_index=True)
