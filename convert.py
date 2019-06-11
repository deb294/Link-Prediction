# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:55:58 2019

@author: dxb36
"""
import pandas as pd
import numpy as np
import csv
import itertools



df = pd.read_csv('E:\LINC_Prediction/index.csv',delimiter=',',engine='python')

col1 = np.array(df[df.columns[0]].values)
print(len(col1))
col2 = np.array(df[df.columns[1]].values)
fh = open ("E:\LINC_Prediction/labeled_1991_1993_1994_1996_3.tsv",'r')

for line in fh:
    #print(line)
    tokens = line.split('\t')
    #a = np.array(tokens[0])
    #print(len(a))
    ind1=np.where(col1==tokens[0])
    print(ind1)
    ind1_val=(col2[ind1[0][0]])
    ind2=np.where(col1==tokens[1])
    ind2_val=(col2[ind2[0][0]])
    f3 = tokens[2]
    ab = [ind1_val,ind2_val,f3]
    #print(ab)
    with open('lable.csv', 'a', newline='') as writeFile:
         writer = csv.writer(writeFile)
         writer.writerow(ab)
'''
fh = open ("E:\LINC_Prediction/labeled_1991_1993_1994_1996_3.tsv",'r')
for line in fh:
    print(line)
    tokens = line.split()
    f3 = tokens[2]
    print(f3)
    ab = [f1[0][0],f2[0][0],f3]
    with open('label.csv', 'a', newline='') as writeFile:
         writer = csv.writer(writeFile)
         writer.writerow(ab)
'''

'''
df1 = pd.read_csv('E:\LINC_Prediction/index.tsv',delimiter='\t',engine='python')
df1 = pd.read_csv('E:\LINC_Prediction/labeled_1991_1993_1994_1996_3.tsv',delimiter='\t',engine='python')
data_ancment = "data_static.csv"
col1 = np.array(df1[df1.columns[0]].values)
col2 = np.array(df1[df1.columns[1]].values)
#df1 = pd.read_csv('E:\LINC_Prediction/output1.csv',delimiter='\t',engine='python')
fh = open ("E:\LINC_Prediction/labeled_1991_1993_1994_1996_3.tsv",'r')
for line in fh:
    tokens = line.split()
    f1 = np.where(c==tokens[0])
    f2 = np.where(c==tokens[1])
    f3 = tokens[2]
    ab = [f1[0][0],f2[0][0],f3]
    with open('output.csv', 'a', newline='') as writeFile:
         writer = csv.writer(writeFile)
         writer.writerow(ab)'''
         