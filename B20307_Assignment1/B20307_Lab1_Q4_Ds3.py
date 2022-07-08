# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:04:20 2021

@author: priyanka kumari
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('pima-indians-diabetes.csv')

# histogram for the attributes pregs 

x=df['pregs']
plt.hist(x,bins=10,color='b',alpha=0.28)
plt.title("Histogram of Pregs")
plt.ylabel("Frequency")
plt.xlabel('Pregs')
plt.show()

# histogram for the attribute skin

x=df['skin']
plt.hist(x,bins=10,color='c',alpha=0.97)
plt.ylabel("Frequency")
plt.xlabel("Skin")
plt.title("Histogram of skin")
plt.show()