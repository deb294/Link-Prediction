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
#%%
##col2 = np.array(df[df.columns[1]].values)
#fh = open ("E:\LINC_Prediction/output.csv",'r')
#stack=[]
#for line in fh:
#    stack.append(line)
#    #print(line)
#    tokens = line.split(',')
#    #a = np.array(tokens[0])
#    #print(len(a))
#    ind1=np.where(col1==tokens[1])
#    #print(ind1)
#    #ind1_val=(col2[ind1[0][0]])
#    #ind2=np.where(col1==tokens[1])
#    #ind2_val=(col2[ind2[0][0]])
#    #f3 = tokens[2]
#    #ab = [ind1,ind2,f3]
#    #print(ab)
#    '''with open('ab.csv', 'a', newline='') as writeFile:
#         writer = csv.writer(writeFile)
#         writer.writerow(ab)'''
##%%
#'''df = pd.read_csv('E:\LINC_Prediction\graph.csv')
#col1 = np.array(df[df.columns[0]].values)
#print(len(col1))
##print(col1)
#'''
#
#
#'''
#fh = open ("E:\LINC_Prediction\output2.csv",'r')
#for line in fh:
#    tokens = line.split(',')
#    a=np.array(tokens[0])
#    #b= np.array(tokens[1])
#    #print(a)
#    #f1 = np.any(a == col1)
#    #print (np.where(f1)[0])
#    f1 = np.where(np.any(col1 == tokens[0]))
#    #f1 = np.where(np.in1d(a, col1))
#    #print(f1)
#    #f2 = np.where(np.in1d(b,col1))
#    #print(f2)
#    #ind1 = df.iloc[f1[0][0]]
#    #print (ind1)
#    #f2 = df[ind2[0][0]]
#    #F1 = np.f1[1:10]
#    #F2 = np.f2[1:10]'''
#    
