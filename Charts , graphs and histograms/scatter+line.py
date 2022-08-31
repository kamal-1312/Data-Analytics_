# -*- coding: utf-8 -*-
"""
Created on Sat May  7 16:39:53 2022

@author: KAMAL
"""
import matplotlib.pyplot as plt

x = [3,6,3,9,10]
y = [2,5,9,0,1]

#plt.scatter(x,y)
#plt.plot(x,y)
#plt.title("Ogive plot")

#plt.figure(figsize = (10,10))
#plt.xticks(x)

#bargraph
#plt.bar(x, y)

#histogram
#plt.hist(x,bins = [0,5,10,15,20,25])


plt.boxplot( x , vert=False)
# plt.title("boxplot")
# plt.label("boxplot")
plt.show()