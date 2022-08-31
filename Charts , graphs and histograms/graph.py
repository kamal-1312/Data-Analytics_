# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:26:12 2022

@author: KAMAL
"""

import pandas as pd
import matplotlib.pyplot as plt

unidata = [5, 10, 15, 20, 25, 15, 12, 15, 26, 65, 38, 85, 87, 90]

mini = min(unidata)
maxi = max(unidata)
cwidth = int((maxi - mini) / 8)

lst1 = []
var = mini
lst1.append(mini)
for i in range(8):
    var += cwidth
    lst1.append(var)
  

print(lst1)
    
    
#y =[0, 25, 50, 75, 100]
plt.xlabel("Soft Drink")
plt.ylabel("unidatauency")
plt.xticks(lst1)
plt.hist(unidata, bins=lst1)
#plt.bar(y, unidata)
plt.show()


# Creating histogram

#fig, ax = plt.subplots(figsize =(10, 7))

#ax.hist(unidata, bins = lst1)
 
# Show plot
plt.show()