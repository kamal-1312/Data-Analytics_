# -*- coding: utf-8 -*-
"""
Created on Sat May  7 12:31:45 2022

@author: mca137
"""
import pandas as pd
import matplotlib.pyplot as plt

sample = [12,11,4,2,32,12,45,32, 100, -200, 150]
#plt.figure(figsize=(10, 10))
plt.boxplot(sample, vert=False)
plt.title("Detecting outliers using Boxplot")
plt.xlabel('Sample')
