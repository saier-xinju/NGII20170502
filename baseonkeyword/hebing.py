# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 15:34:52 2017

@author: npc
"""


user_id= [0 for i in range(106)]
item= [0 for i in range(106)]
file = open('simply4.csv')

n=0
for line in file.readlines():
     line = line.replace("\n"," ")
     line = line.replace("\r"," ")
     line = line.split(',')
     user_id[n] = line[0]
     item[n] = line[1]
     n+=1
file.close()
for j in range(1,106,1):
    if j+1<len(user_id):
        if user_id[j]==user_id[j+1]:
            item[j+1]=str(item[j])+','+str(item[j+1])
        else:
            continue


w=open('OR2.csv','w+')
for i in range(len(user_id)):
	w.write(str(user_id[i])+','+str(item[i])+'\n')
w.close()