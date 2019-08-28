# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 16:02:26 2017

@author: npc
"""


w=open('406830+NUM.csv','w+')

with open('UIN.csv','r') as f:
    lines=f.readlines()
    for i in range(1,406830): #打印文件前2行内容
        w.write(lines[i])
w.close()


