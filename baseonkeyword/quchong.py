# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 16:21:28 2017

@author: npc
"""


user_id= [0 for i in range(106)]
item= [0 for i in range(106)]
file = open('OR1.csv')
n=0
for line in file.readlines():
     line = line.split(',')
     user_id[n] = line[0]
     item[n]=line[1:]
     n+=1
file.close
w=open('new_OR8.txt','w+')
for j in range(1,106,1):
    if j+1<len(user_id):
        if user_id[j]!=user_id[j+1]:
            w.write(str(user_id[j])+','+str(item[j])+'\n')        
        else:
            continue
w.write(str(user_id[-1])+','+str(item[-1]))  
w.close()
