# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:19:08 2017

@author: yuguiyang
"""

import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation  
  

fig,axes = plt.subplots()  
axes.plot(np.random.rand(10))  

#重新绘制图形
def update_line(data): 
    #清空当前轴
    plt.cla()
    #重新绘图
    axes.plot(data)

#生成绘制图形的数据
def create_line_data():
    yield np.random.rand(10)  

#传入的fig中，调用update_line函数，将create_line_data作为参数传给update_line，5秒调用一次
ani = animation.FuncAnimation(fig, update_line, create_line_data, interval=5*1000)  

plt.show() 