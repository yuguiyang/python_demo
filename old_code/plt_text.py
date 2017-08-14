# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 09:59:35 2017

@author: hexo
"""

import matplotlib.pyplot as plt

#手动创建一个figure，标题为"one"
f1 = plt.figure('one')

#获取当前axes
current_axes = plt.gca()

plt.figtext(0.5,0.6,'figtext',fontsize=20)
plt.suptitle('hey,boy')
plt.bar(3,3)

#使用axes绘图
current_axes.plot([1,2,3],[3,2,1],color='red',label='lable1',linewidth=3)
current_axes.plot([1,2,3],[1,2,3],color='green',label='label2',linewidth=3)
current_axes.plot([1,2,3],[2,2,2],'bs')

current_axes.text(2,3,'hello world.',bbox=dict(facecolor='blue', alpha=0.1))
current_axes.text(2,1,'hahaha',fontsize=20,horizontalalignment='center',
                  verticalalignment='center',
                  bbox=dict(facecolor='blue', alpha=0.5))

current_axes.set_xlabel('x-label')
current_axes.set_ylabel('y-label')
current_axes.set_title('op-title')

#xy指向的坐标，xytext文本坐标，arrowprops定义箭头格式
current_axes.annotate('look!!',xy=(2,2),xytext=(2.5,1.75),
                      arrowprops=dict(facecolor='black', shrink=0.05))

print(type(current_axes))

plt.show()