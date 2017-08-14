# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 16:51:29 2017

@author: hexo
"""

import numpy as np

a = np.zeros(10)
print(a)
print(a.dtype)
print(a.shape)

b = np.zeros([3,4])
print(b)
print(b.shape)

c = np.empty(3)
print(c)
d = np.empty([3,4])
print(d)

e = np.ones(5)
print(e)
f = np.ones([2,6])
print(f)

g = np.arange(3)
print(g)
