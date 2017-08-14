# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:02:57 2017

@author: hexo
"""

import matplotlib.pyplot as plt

'''
plt.bar([10,12,14],[10,15,20],facecolor='green',tick_label=['one','two','three'],label='green')

plt.bar([10,12,14],[5,30,10],bottom=[10,15,20],facecolor='orange',label='orange')

plt.legend()
'''

common_width=1
plt.bar([10,20,30],[10,15,20],width=common_width,facecolor='red',label='red')
#只需要将left+width就行了
plt.bar([11,21,31],[5,20,10],width=common_width,facecolor='green',label='green')

plt.legend()


plt.show()