# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 21:04:03 2021

@author: priyanka kumari
"""

import pandas as pd
#import matplotlib.pyplot as plt

def cov(A,B):
    if len(A)==len(B):
        Ea=A.mean(); Eb=B.mean()
        cosum=0
        for i in range(len(A)):
            cosum+=(A[i]-Ea)*(B[i]-Eb)
        covr=cosum/(len(A)-1)
    else:
        print("Unequal array size!!")
    return covr

def var(k):
    s=0
    m=k.mean()
    for i in k:
        s+=(i-m)**2
    v=s/(len(k)-1)
    return v

def corr_coeff(df,x,y):
   
    # standard deviation of 2 columns
    #x_sd=df[x].std()
    #y_sd=df[y].std()
    
    # finding correlation coffection
    corr= cov(x,y)/((var(x)**0.5)*var(y)**0.5)
    
    return corr

# correlation coffection between Age with all other attributes (excluding class)

df=pd.read_csv('pima-indians-diabetes.csv')
pregs=corr_coeff(df, df['Age'], df['pregs'])
plas=corr_coeff(df, df['Age'], df['plas'])
pres=corr_coeff(df, df['Age'], df['pres'])
skin=corr_coeff(df, df['Age'], df['skin'])
test=corr_coeff(df, df['Age'], df['test'])
BMI=corr_coeff(df, df['Age'], df['BMI'])
pedi=corr_coeff(df, df['Age'], df['pedi'])

print("Correlation coffection between Age and pregs is: ", pregs)
print("Correlation coffection between Age and plas is: ", plas)
print("Correlation coffection between Age and pres is: ", pres)
print("Correlation coffection between Age and skin is: ", skin)
print("Correlation coffection between Age and test is: ", test)
print("Correlation coffection between Age and BMI is: ", BMI)
print("Correlation coffection between Age and pedi is: ", pedi)

print()

# correlation coffection between BMI with all other attributes (excluding class)

pregs=corr_coeff(df, df['BMI'], df['pregs'])
plas=corr_coeff(df, df['BMI'], df['plas'])
pres=corr_coeff(df, df['BMI'], df['pres'])
skin=corr_coeff(df, df['BMI'], df['skin'])
test=corr_coeff(df, df['BMI'], df['test'])
BMI=corr_coeff(df, df['BMI'], df['BMI'])
pedi=corr_coeff(df, df['BMI'], df['pedi'])

print("Correlation coffection between BMI and pregs is: ", pregs)
print("Correlation coffection between BMI and plas is: ", plas)
print("Correlation coffection between BMI and pres is: ", pres)
print("Correlation coffection between BMI and skin is: ", skin)
print("Correlation coffection between BMI and test is: ", test)
print("Correlation coffection between BMI and BMI is: ", BMI)
print("Correlation coffection between BMI and pedi is: ", pedi)

