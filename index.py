# -*- coding: utf-8 -*-
"""
Created on Wed May 22 15:29:41 2019

@author: dxb36
"""

import pandas as pd
import numpy as np
import csv
import itertools




df = pd.read_csv('E:\LINC_Prediction/labeled_1991_1993_1994_1996_3.tsv',delimiter='\t',engine='python')


col1 = np.array(df[df.columns[0]].values)
col2 = np.array(df[df.columns[1]].values)

c1= np.unique(col1)
c2= np.unique(col2)

c = np.append(c1,c2)
c= np.unique(c)
i=0
for item in c:
    r= [item,i]
    i=i+1
    with open('index.csv', 'a', newline='') as writeFile:
         writer = csv.writer(writeFile)
         writer.writerow(r)
