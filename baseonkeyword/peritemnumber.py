# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:47:30 2017

@author: npc
"""
w=open('pernumber2.xls','w+')
import pandas as pd
df = pd.read_csv('406830+NUM.csv')
d = {}
for i in range(0,406829,1):
     if df["a"][i] in d:
        d[df["a"][i]] = d[df["a"][i]] + int(df["b"][i])
     else:
         d.setdefault(df["a"][i],int(df["b"][i]))

for key,value in d.items():
    w.write(str(key)+'\t '+str(value)+'\n')
w.close()
