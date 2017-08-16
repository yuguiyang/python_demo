# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 14:42:14 2017

@author: yuguiyang
"""

path = r'D:\Users\yuguiyang\Documents\GitHub\python_demo\code\crawler\1688_line.txt'

file = open(path,'r')

line = file.readline()

lines = []
while line:
    lines.append(line)
    
    line = file.readline()
    
print(len(lines))    
file.close()