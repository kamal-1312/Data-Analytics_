# -*- coding: utf-8 -*-
"""
Created on Sat May  7 08:57:25 2022

@author: mca137
"""

import pandas as pd
import math
x = [12,14,24,26,9,19,5,17]
y = [68,74,96,89,56,61,48,55]
meanx = sum(x)/len(x)
meany = sum(y)/len(y)
xi_x = []
yi_y = []
xi_x_yi_y = []

for i in x:
    xi_x.append(i-meanx)

for i in y:
   yi_y.append(i-meany)

for i in range(len(x)):
    xi_x_yi_y.append(xi_x[i] * yi_y[i])
    
print("x\t\ty\t\txi-x\t\tyi-y\t\t(xi-x)(yi-y)")
for i in range(len(x)):  
    print(x[i],"\t\t",y[i],"\t\t",xi_x[i],"\t\t",yi_y[i],"\t\t",xi_x_yi_y[i])
   # print("")

print(sum(x),"\t\t",sum(y),"\t\t",sum(xi_x),"\t\t",sum(yi_y),"\t\t",sum(xi_x_yi_y))

print("Covariance = ",sum(xi_x_yi_y)/len(x))