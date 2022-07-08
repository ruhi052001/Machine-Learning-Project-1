# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 19:48:18 2021

@author: priyanka kumari
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('pima-indians-diabetes.csv')

# plot between attribute Age and pregs

x= df['Age']
y=df['pregs']

plt.scatter(x, y, color='r')
plt.title('Scatter plots between Age and pregs')
plt.xlabel('Age')
plt.ylabel('Pregs')
plt.show()

# plot between attribute Age and plas

x= df['Age']
y=df['plas']

plt.scatter(x, y, color='g')
plt.title('Scatter plots between Age and plas')
plt.xlabel('Age')
plt.ylabel('Plas')
plt.show()

# plot between attribute Age and pres

x= df['Age']
y=df['pres']

plt.scatter(x, y, color='b')
plt.title('Scatter plots between Age and pres')
plt.xlabel('Age')
plt.ylabel('Pres')
plt.show()

# plot between Age and skin

x= df['Age']
y=df['skin']

plt.scatter(x, y, color='black')
plt.title('Scatter plots between Age and pregs')
plt.xlabel('Age')
plt.ylabel('skin')
plt.show()

# plot between Age and test

x= df['Age']
y=df['test']

plt.scatter(x, y, color='orange')
plt.title('Scatter plots between Age and test')
plt.xlabel('Age')
plt.ylabel('Test')
plt.show()

# plot between Age and BMI

x= df['Age']
y=df['BMI']

plt.scatter(x, y, color='pink')
plt.title('Scatter plots between Age and BMI')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.show()

# plot between Age and pedi

x= df['Age']
y=df['pedi']

plt.scatter(x, y, color='grey')
plt.title('Scatter plots between Age and pedi')
plt.xlabel('Age')
plt.ylabel('Pedi')
plt.show()

# ---------------------------------------------------------------------------

# plot between BMI and pregs

x= df['BMI']
y=df['pregs']

plt.scatter(x, y, color='r')
plt.title('Scatter plots between BMI and pregs')
plt.xlabel('BMI')
plt.ylabel('Pregs')
plt.show()

# plot between BMI and plas

x= df['BMI']
y=df['plas']

plt.scatter(x, y, color='g')
plt.title('Scatter plots between BMI and plas')
plt.xlabel('BMI')
plt.ylabel('Plas')
plt.show()

# plot between BMI and pres

x= df['BMI']
y=df['pres']

plt.scatter(x, y, color='b')
plt.title('Scatter plots between BMI and pres')
plt.xlabel('BMI')
plt.ylabel('Pres')
plt.show()

# plot between BMI and skin

x= df['BMI']
y=df['skin']

plt.scatter(x, y, color='black')
plt.title('Scatter plots between BMI and pregs')
plt.xlabel('BMI')
plt.ylabel('skin')
plt.show()

# plot between BMI and test

x= df['BMI']
y=df['test']

plt.scatter(x, y, color='orange')
plt.title('Scatter plots between BMI and test')
plt.xlabel('BMI')
plt.ylabel('Test')
plt.show()

# plot between BMI and pedi

x= df['BMI']
y=df['pedi']

plt.scatter(x, y, color='grey')
plt.title('Scatter plots between BMI and pedi')
plt.xlabel('BMI')
plt.ylabel('Pedi')
plt.show()

# plot between BMI and Age

x= df['BMI']
y=df['Age']

plt.scatter(x, y, color='purple')
plt.title('Scatter plots between BMI and Age')
plt.xlabel('BMI')
plt.ylabel('Age')
plt.show()

