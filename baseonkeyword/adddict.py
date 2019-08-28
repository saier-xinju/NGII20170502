# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:27:18 2017

@author: npc
"""

import pandas as pd
df = pd.read_csv('406830+NUM.csv')
s=df["b"].sum
d = {}
ad = {}
for i in range(0,406829,1):
     if df["a"][i] in d:
        d[df["a"][i]] = d[df["a"][i]] + int(df["b"][i])
     else:
         d.setdefault(df["a"][i],int(df["b"][i]))

n={}
i=0
for key,value in d.items():
    p=key
    n[i]=value/490688.00
    ad[p]=n[i]

 

