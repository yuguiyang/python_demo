# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 14:01:31 2017

@author: hexo
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties  

font_set = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=13)

'''
matplotlib.pyplot.bar(left, height, width=0.8, bottom=None, 
                      hold=None, data=None, **kwargs)
Make a bar plot
Make a bar plot with rectangles bounded by:

    left, left + width, bottom, bottom + height
        (left, right, bottom and top edges)


'''

plt.figure(u'条形图练习')

label = ['one','two','three','four','five']
data = [10,15,30,20,10]


plt.subplot(2,2,1)
plt.title(u'最简单的柱形图',fontproperties=font_set)
plt.bar(range(len(data)),data)



plt.subplot(2,2,2)
plt.title(u'不同颜色的bar',fontproperties=font_set)
#color:scalar or array-like, optional
#the colors of the bar faces
plt.bar(range(len(data)),data,color=['red','yellow','blue','green','black'],label='label2')
plt.legend()



plt.subplot(2,2,3)
plt.title(u'自定义label',fontproperties=font_set)

#plt.bar(np.arange(len(data)),data,color='green',tick_label=label)
#edgecolor：边框颜色，facecolor：填充颜色
#linewidth：线条宽度，
#alpha：透明度
#tick_label：标签
plt.bar(np.arange(len(data)),data,edgecolor='red',
        facecolor='green',linewidth=2,alpha=0.3
        ,tick_label=label,label='label3')

plt.legend()
#这个方法不行，位置显示有问题
#ax = plt.gca()
#ax.set_xticklabels(['one','two','three','four'])

plt.subplot(2,2,4)
plt.title(u'设置填充',fontproperties=font_set)

plt.bar(np.arange(len(data)),data,hatch='+',tick_label=label,label='label4')



plt.show()