# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:34:27 2021

@author: priyanka kumari
"""

import pandas as pd
import numpy as np

def mean(a):
    s=0
    for i in a:
        s+=i
    mean=s/len(a)
    return mean

def median(b):
    c=sorted(b)
    n=len(b)
    if n%2==0:
        median=(c[int(n/2)]+c[int((n/2)+1)])/2
    else:
        median=c[int((n+1)/2)]
    return median

def Std_Dev(d):
    temp=0
    N=len(d)
    std_dev=0
    mn=mean(d)
    for i in d:
        temp+=(i-mn)**2
    std_dev= (temp/N)**0.5
    return std_dev

def maximum(m):
    return max(m)

def minimum(n):
    return min(n)

def mode(k):
    return k.mode()

df=pd.read_csv('pima-indians-diabetes.csv')

# mean
print("MEAN")
print()
pregs=mean(df['pregs'])
plas=mean(df['plas'])
pres=mean(df['pres'])
skin=mean(df['skin'])
test=mean(df['test'])
BMI=mean(df['BMI'])
pedi=mean(df['pedi'])
Age=mean(df['Age'])

print("pregs : ", pregs)
print("plas : ", plas)
print("pres : ", pres)
print("skin : ", skin)
print("test : ", test)
print("BMI : ", BMI)
print("pedi : ", pedi)
print("Age : ", Age)

print()

# median
print("MEDIAN")
print()
pregs=median(df['pregs'])
plas=median(df['plas'])
pres=median(df['pres'])
skin=median(df['skin'])
test=median(df['test'])
BMI=median(df['BMI'])
pedi=median(df['pedi'])
Age=median(df['Age'])

print("pregs : ", pregs)
print("plas : ", plas)
print("pres : ", pres)
print("skin : ", skin)
print("test : ", test)
print("BMI : ", BMI)
print("pedi : ", pedi)
print("Age : ", Age)

print()

# Standar deviation
print("STANDAR DEVIATION")
print()
pregs=Std_Dev(df['pregs'])
plas=Std_Dev(df['plas'])
pres=Std_Dev(df['pres'])
skin=Std_Dev(df['skin'])
test=Std_Dev(df['test'])
BMI=Std_Dev(df['BMI'])
pedi=Std_Dev(df['pedi'])
Age=Std_Dev(df['Age'])

print("pregs : ", pregs)
print("plas : ", plas)
print("pres : ", pres)
print("skin : ", skin)
print("test : ", test)
print("BMI : ", BMI)
print("pedi : ", pedi)
print("Age : ", Age)
print()

# maximum
print("MAXIMUM")
print()
pregs=maximum(df['pregs'])
plas=maximum(df['plas'])
pres=maximum(df['pres'])
skin=maximum(df['skin'])
test=maximum(df['test'])
BMI=maximum(df['BMI'])
pedi=maximum(df['pedi'])
Age=maximum(df['Age'])

print("pregs : ", pregs)
print("plas : ", plas)
print("pres : ", pres)
print("skin : ", skin)
print("test : ", test)
print("BMI : ", BMI)
print("pedi : ", pedi)
print("Age : ", Age)
print()

# minimum
print("MINIMUM")
print()
pregs=minimum(df['pregs'])
plas=minimum(df['plas'])
pres=minimum(df['pres'])
skin=minimum(df['skin'])
test=minimum(df['test'])
BMI=minimum(df['BMI'])
pedi=minimum(df['pedi'])
Age=minimum(df['Age'])

print("pregs : ", pregs)
print("plas : ", plas)
print("pres : ", pres)
print("skin : ", skin)
print("test : ", test)
print("BMI : ", BMI)
print("pedi : ", pedi)
print("Age : ", Age)
print()

# mode
print("MODE")
print()
pregs=mode(df['pregs'])
plas=mode(df['plas'])
pres=mode(df['pres'])
skin=mode(df['skin'])
test=mode(df['test'])
BMI=mode(df['BMI'])
pedi=mode(df['pedi'])
Age=mode(df['Age'])

print("pregs : ", pregs)
print("plas : ", plas)
print("pres : ", pres)
print("skin : ", skin)
print("test : ", test)
print("BMI : ", BMI)
print("pedi : ", pedi)
print("Age : ", Age)

