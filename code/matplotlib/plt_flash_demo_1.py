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


def init():
    print('init')
    #清空当前轴
    plt.cla()

    
#重新绘制图形
def update_line(data): 
    print(datetime.now(),'--',data)
    #清空当前轴
    plt.cla()
    #重新绘图
    axes.plot(np.random.rand(10))
    
#传入的fig中，调用update_line函数，将create_line_data作为参数传给update_line，5秒调用一次
#repeat 参数，可以控制变量遍历之后，是否重复
#repeat delay应该是控制每一次循环之后的间隔时间
ani = animation.FuncAnimation(fig, update_line, 3, repeat=False, interval=3000,init_func=init)  

plt.show() 