# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 20:17:54 2017

@author: yuguiyang
"""


import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation  

#初始状态，共100人
total_people = 100  
#每个人的x轴坐标
x = np.arange(100)
#每人初始100块
people = [100]*total_people
#局数
game_round = 0
game_max_round = 17000

#初始绘图
fig,axes = plt.subplots()

axes.bar(x,people,facecolor='green') 
axes.set_title(u'Round: '+str(game_round))
axes.grid(True,axis='y')

#根据下标i,随机返回另一个下标
def give_to(i):
    i_to = i
    while i == i_to:
        i_to = np.random.randint(0,100)
    
    #print('from',i,'to',i_to)
    return i_to

#重新绘制图形
#1.当拥有的钱为0，则不再支出，但可以收入
def game(obj): 
    global people
    global game_round

    #还不知道咋让循环停止，就在这判断下
    if game_round < game_max_round:
        #清空当前轴
        plt.cla()
        
        #遍历100个人
        for i in range(total_people):
            #判断，当前人是否有钱
            if people[i] > 0 :
                #每个人拿出1块钱，给另一个人
                people[i] = people[i] - 1
                people_to = give_to(i)
                people[people_to] = people[people_to] + 1
                
                #print(people)
            else :
                pass
         
        
        game_round += 1
        #重新绘图
        axes.set_title(u'Round: '+str(game_round))
        axes.bar(x,sorted(people),facecolor='green')
        axes.grid(True,axis='y')
    else :
        pass

#2.允许借贷的情况，及拥有的钱可以为负
def game2(obj): 
    global people
    global game_round

    #还不知道咋让循环停止，就在这判断下
    if game_round < game_max_round:
        #清空当前轴
        plt.cla()
        
        #遍历100个人
        for i in range(total_people):
            #每个人拿出1块钱，给另一个人
            people[i] = people[i] - 1
            people_to = give_to(i)
            people[people_to] = people[people_to] + 1
         
        
        game_round += 1
        #重新绘图
        axes.set_title(u'Round: '+str(game_round))
        axes.bar(x,sorted(people),facecolor='green')
        axes.grid(True,axis='y')
    else :
        pass
#循环调用游戏
ani = animation.FuncAnimation(fig, game2, interval=0.1)  

plt.show() 