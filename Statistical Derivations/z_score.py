# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math
import pandas as pd

data = [12,11,4,2,32,12,45,32, 1000, -2000, 1500]

df = pd.DataFrame(data,columns=['x'])
M = sum(data)/len(data)
xi_x = []

for i in range(df.shape[0]):
    xi_x.append(df.iat[i,0]-M)
    
df['xi-x'] = xi_x
sq_xi_x = []    

for i in range(df.shape[0]):
    sq_xi_x.append(round(pow(df.iat[i,1],2), 2))
    
    
df['(xi-x)2']=sq_xi_x
variance=sum(sq_xi_x)/len(sq_xi_x)
std_dev=math.sqrt(variance)
#print(df)

print(variance)
print(std_dev)
z_score=[]    

for i in range(df.shape[0]):
    z_score.append(df.iat[i, 1]/std_dev)
    
df['Z-Score']=z_score    
print(df)

lst = []
out = []

for i in range(df.shape[0]):
    if  -2 <= df.iat[i, 3] <= 2:
        lst.append(df.iat[i, 0])
    else:
        out.append(df.iat[i, 0])
        
        
print(lst)
print(out)
