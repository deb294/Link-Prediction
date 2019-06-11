# -*- coding: utf-8 -*-
"""
Created on Fri May 24 19:41:12 2019

@author: dxb36
"""

import pandas as pd
import numpy as np
import csv

def csv_retrieve(name):  
    fh = open (name,'r')
    STACK_2=[]
    for line in fh:
        tokens = line.split(' ')
        STACK_2.append(tokens)
    return STACK_2
out_put=csv_retrieve("/home/debanjalib/label.csv")
graph=csv_retrieve('/home/debanjalib/94-96_graph.csv')

#%%
def average(list_1,list_2):
    average=[]
    for i in range(0,len(list_1)):
        average.append(str((float(list_1[i])+float(list_2[i])/2)))
    return average

#%%
final=[]
for j  in range(0,len(out_put)):
    chk_1=False
    chk_2=False
    for i in range(0,len(graph)):
        if int(graph[i][0])==int(out_put[j][0]):
            chk_1=True
            list_1=graph[i][1:11]
        if int(graph[i][0])==int(out_put[j][1]):
            chk_2=True
            list_2 = graph[i][1:11]
        if chk_1 and chk_2:
            print('here')
            temp_2=average(list_1,list_2)+[out_put[j][2]]
            final.append(temp_2)
 #%%

file = open('91_final.csv','w') 
for row in final:
    for k in final[i][0:10]:
        file.write(k+',') 
    file.write(final[i][-1])
   #file.write(final[i][-1] +'\n')
file.close()
print('done')      
