# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:06:45 2022

@author: mca137
"""

import pandas as pd
import math
df = pd.read_csv("Iqr.csv")

#only for dataframe by column name

df = df.sort_values(by='x')
print(df)
length = df.shape[0]

print(length)

i1 = (25/100) * length

i3 = (75/100) * length

if i1%1==0:
    i1 =  int(i1)
    q1 = (df.iat[i1-1, 0] + df.iat[i1, 0])/2
else:
    i1 = int(math.ceil(i1))
    q1 = df.iat[i1-1, 0]
    
    
if i3%1==0:
    i3 = int(i3)
    q3 = (df.iat[i3-1, 0] + df.iat[i3, 0])/2
else:
    i3 = int(math.ceil(i3))
    q3 = df.iat[i3-1, 0]
   
print(i1)
print(i3)
print(q1)
print(q3)

iqr = q3-q1
lb = q1-(iqr*1.5)
ub = q3+(iqr*1.5)
print(ub,lb)
data=[]
OUTl=[]

for i in range(length):    
     if df.iat[i,0]>lb and df.iat[i,0]<ub:
          data.append(df.iat[i,0])
     else:
          OUTl.append(df.iat[i,0])
print(data)
print(OUTl)

    