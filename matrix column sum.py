# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 01:23:53 2023

@author: 926824
"""

list2=list(map(int,input().split()))
len1=list2[0]
len2=list2[1]
list1=[]
for i in range(len1):
   list1.append(list(map(int,input().split())))
   
for j in range(len2):
    sum1=0
    for k in range(len1):
        sum1=sum1+list1[k][j]
    print(sum1)