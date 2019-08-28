# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:44:38 2017

@author: npc
"""
c=[]
def load_sequence(from_path):
    with open(from_path) as fp:
        [c.append(line.strip().split(",")) for line in fp]
        
load_sequence('E:\\wordpython\\1105\\allitem.txt')
w=open('cfzs2.csv','w')
for i in range(3707):
    for j in range(i+1,3707):
        item=len(set(c[i])&set(c[j]))
        if item>=10:
            w.write(str(c[i][0])+','+str(c[j][0])+','+str(item)+'\n')
w.close()
