# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 16:23:33 2017

@author: npc
"""

user_id= [0 for i in range(4373)]
item= [0 for i in range(4373)]
file = open('to4.csv')
w=open('allitem2.xlsx','w+')
n=0
for line in file.readlines():
     line = line.split(',')
     user_id[n] = line[0]
     item[n] = line[1:]
     n+=1
file.close()
u={}
i={}
u = user_id.replace("'","")
i = user_id.replacee("'","")
for i in range(1,4373):
    if len(item[i])>10:
        w.write(str(user_id[i])+'\t'+str(item[i])+'\n')
w.close()