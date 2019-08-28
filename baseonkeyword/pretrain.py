# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 18:31:45 2017

@author: npc
"""

user_id= [0 for i in range(406830)]
item= [0 for i in range(406830)]
file = open('allsample.csv')
w=open('trainsample3.txt','w+')
n=0
for line in file.readlines():
     line = line.replace("\n"," ")
     line = line.replace("\r"," ")
     line = line.split(',')
     user_id[n] = line[0]
     item[n] = line[1]
     n+=1
file.close()
for j in range(1,406830,1):
    if j+1<len(user_id):
        if user_id[j]==user_id[j+1]:
            item[j+1]=str(item[j])+','+str(item[j+1])
        else:
            w.write(str(user_id[j])+','+str(item[j])+'\n') 
w.write(str(item[-1]))  
w.close()



