# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:41:07 2017

@author: npc
"""

user_id= [0 for i in range(406830)]
num= [0 for i in range(406830)]
file = open('406830+NUM.csv')
w=open('ADDNUMBER.csv','w+')
n=0
for line in file.readlines():
     line = line.split(',')
     user_id[n] = line[0]
     num[n] = int(line[-1])
     n+=1
file.close()
N=0
for j in range(0,406830,1):
    if j+1<len(user_id):
        if user_id[j]==user_id[j+1]:
            N+=num[j]
        else:
            N+=num[j]
            w.write(str(user_id[j])+','+str(N)+'\n')
            N=0
w.close()