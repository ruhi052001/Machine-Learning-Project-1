# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 16:04:58 2021

@author: priyanka kumari
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('pima-indians-diabetes.csv')

# Grouping of data with respect to class
d=df.groupby('class')

# data of class 0
d0=d.get_group(0)

# histogram plot 
plt.hist(d0['pregs'],color='g')
plt.xlabel('Pregs')
plt.ylabel('frequency')
plt.title('Histogram of attribute of pregs for class 0')
plt.show()

# data of class 1
d1=d.get_group(1)

#histogram plot
plt.hist(d1['pregs'],color='purple')
plt.xlabel('Pregs')
plt.ylabel('frequency')
plt.title('Histogram of attribute of pregs for class 1')
plt.show()