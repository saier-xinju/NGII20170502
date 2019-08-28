# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 11:43:37 2017

@author: npc
"""

import pandas as pd
df = pd.read_csv('ORsimply.csv')
df1 = df.groupby("CustomerID")['Description'].apply(','.join).reset_index()
df2 = df1.loc[df1["Description"].map(len) > 10]
df2.to_csv('to1.csv', columns=['CustomerID','Description'])