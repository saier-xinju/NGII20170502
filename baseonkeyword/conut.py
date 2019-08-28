# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:12:00 2017

@author: npc
"""
import pandas as pd
df = pd.read_excel('to4.xlsx')
n = df[df['Description'].map(len)>10]
n.to_txt('to6.txt')