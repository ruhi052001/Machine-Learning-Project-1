# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 12:55:54 2021

@author: priyanka kumari
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('pima-indians-diabetes.csv')

# box plot for preg

plt.boxplot(df['pregs'],showmeans=(True))
plt.ylabel('Pregs frequency')
plt.xlabel('Pregs Data')
plt.title('Box plot for Pregs')
plt.show()

# box plot for plas

plt.boxplot(df['plas'],showmeans=True)
plt.ylabel('Plas frequency')
plt.xlabel('Plas Data')
plt.title('Box plot for Plas')
plt.show()

# box plot for pres

plt.boxplot(df['pres'],showmeans=True)
plt.ylabel('Pres frequency')
plt.xlabel('Pres Data')
plt.title('Box plot for Pres')
plt.show()

# box plot for skin

plt.boxplot(df['skin'],showmeans=True)
plt.ylabel('Skin frequency')
plt.xlabel('Skin Data')
plt.title('Box plot for Skin')
plt.show()

# box plot for test

plt.boxplot(df['test'],showmeans=True)
plt.ylabel('Test frequency')
plt.xlabel('Test Data')
plt.title('Box plot for Test')
plt.show()

# box plot for BMI

plt.boxplot(df['BMI'],showmeans=True)
plt.ylabel('BMI frequency')
plt.xlabel('BMI Data')
plt.title('Box plot for BMI')
plt.show()

# box plot for pedi

plt.boxplot(df['pedi'], showmeans=True)
plt.ylabel('Pedi frequency')
plt.xlabel('Pedi Data')
plt.title('Box plot for Pedi')
plt.show()

# box plot for Age

plt.boxplot(df['Age'],showmeans=True)
plt.ylabel('Age frequency')
plt.xlabel('Age Data')
plt.title('Box plot for Age')
plt.show()

