# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:08:44 2017

@author: yuguiyang
"""
import numpy as np  
import matplotlib.pyplot as plt  
import matplotlib.animation as animation

#定义一个people类
class People:
    __data = 100
    __color = 'green'
    
    
    def __init__(self,data=100,color='green'):
        self.__data = data
        self.__color = color
    
    def __str__(self):
        return str(self.__data)+','+self.__color
    
    def set_data(self,data):
        self.__data = data
        
    def set_color(self,color):
        self.__color = color
    
    def get_data(self):
        return self.__data
    
    def get_color(self):
        return self.__color
    
    def give_money(self,money=1):
        self.__data = self.__data - money
        
    def rcv_money(self,money=1):
        self.__data = self.__data + money


#对数据进行排序后返回数据
def parse_people_data():
    global peoples
    
    people_data = []
    people_color = []
    for p in sorted(peoples, key=lambda p: p.get_data()):
        people_data.append(p.get_data())
        people_color.append(p.get_color())
        
    
    return people_data,people_color


####################################################

#初始状态，共100人
total_people = 100  
#每个人的x轴坐标
x = np.arange(total_people)

#每人初始100块,颜色是绿色
peoples = []
for i in range(total_people):
    peoples.append(People())
    

#局数
game_round = 0
game_max_round = 17000

#初始绘图
fig,axes = plt.subplots()

axes.bar(x,parse_people_data()[0],color=parse_people_data()[1]) 
axes.set_title(u'Round: '+str(game_round))
axes.grid(True,axis='y')


#根据下标i,随机返回另一个下标
def give_to(i):
    i_to = i
    while i == i_to:
        i_to = np.random.randint(0,100)
    
    return i_to

#重新绘制图形
#1.当拥有的钱为0，则不再支出，但可以收入
#参考plt_flash_demo2

#2.允许借贷的情况，及拥有的钱可以为负
def game2(obj): 
    global peoples
    global game_round

    #还不知道咋让循环停止，就在这判断下
    if game_round < game_max_round:
        #清空当前轴
        plt.cla()
        
        #遍历100个人
        for i in range(total_people):
            #每个人拿出1块钱，给另一个人
            peoples[i].give_money()
            people_to = give_to(i)
            peoples[people_to].rcv_money()
         
        #在第6500次游戏，修改负债者的颜色
        if game_round == 6500:
            for p in peoples :
                if p.get_data()<0:
                    p.set_color('red')
                else :
                    pass
            
        game_round += 1
        #重新绘图
        axes.set_title(u'Round: '+str(game_round))
        axes.bar(x,parse_people_data()[0],color=parse_people_data()[1])
        axes.grid(True,axis='y')
    else :
        pass
#循环调用游戏
ani = animation.FuncAnimation(fig, game2, interval=1)  

plt.show()   
