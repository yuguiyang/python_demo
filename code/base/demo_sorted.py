# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 11:47:55 2017

@author: hexo
"""

class People:
    
    def __init__(self,id,name):
        self.id=id
        self.name=name
        

p1 = People(10,'lufei')
p2 = People(5,'namei')
p3 = People(15,'qiaoba')

for p in sorted([p1,p2,p3],key=lambda p: p.id):
    print(p.id,p.name)

for p in sorted([p1,p2,p3],key=lambda p: p.name):
    print(p.id,p.name)    