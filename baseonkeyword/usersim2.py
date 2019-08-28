# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 22:11:33 2017

@author: npc
"""
import math
import pandas as pd
df = pd.read_excel('pernumber8.xlsx')
w=open('usersim.xlsx','w+')
df.head()
list1 = list(df["a"])
list2 = list(df["b"])
dt = dict(list(zip(list1,list2)))

c=[]
def load_sequence(from_path):
    with open(from_path) as fp:
        [c.append(line.strip().split(",")) for line in fp]
        
load_sequence('E:\\pythonwork\\1105\\to.csv')

z=0
for i in range(1,4364):
    for j in range(i+1,4364):
        usim=0
        comitems=list(set(c[i])&set(c[j]))
        if comitems:
            for item in comitems:
                if item in list(dt.keys()):
                    z = dt.get(item)
                    if z and z>0:
                        usim+=-math.log(z)
                    if z and z<0:
                        usim+=math.log(abs(z))
            w.write(str(c[i][0])+'\t'+str(c[j][0])+'\t'+str(usim)+'\n')
w.close()