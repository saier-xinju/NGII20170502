# -*- coding: utf-8 -*-
"""
Created on Tue Nov 07 12:31:32 2017

@author: npc
"""
c=[]
def load_sequence(from_path):
    with open(from_path) as fp:
        [c.append(line.strip().split(",")) for line in fp]
def main():
    load_sequence('trainsample2.txt')
    w=open('allitem2.txt','w+')
    ids = []
    for line in c:
        ids=list(set(line))
        if len(ids)>10:
            w.write(str(ids).lower()+'\n')
    w.close()
if __name__ == "__main__":  
    main()