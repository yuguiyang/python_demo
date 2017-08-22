# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:19:08 2017

@author: yuguiyang
"""

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation  
from datetime import datetime 
  

fig,axes = plt.subplots()  
axes.plot(np.random.rand(10))  

t_count = 0

#重新绘制图形
def update_line(data): 
    global t_count
    t_count = t_count+1
    
    print('\n')
    print(t_count,':',datetime.now(),':',data)
    print('------------------------------------\n')
    #清空当前轴
    plt.cla()
    #重新绘图
    axes.plot(np.random.rand(10))

#生成绘制图形的数据
def create_line_data():
    yield np.random.rand(10)  

#传入的fig中，调用update_line函数，将create_line_data作为参数传给update_line，5秒调用一次
#ani = animation.FuncAnimation(fig, update_line, 5, interval=2*1000)  
ani = animation.FuncAnimation(fig, update_line, 5, interval=5000,bl)  

plt.show() 