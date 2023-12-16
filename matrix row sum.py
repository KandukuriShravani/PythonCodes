# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 19:43:15 2023

@author: 926824
"""
list2=list(map(int,input().split()))
len1=list2[0]
len2=list2[1]
list1=[]
for i in range(len1):
   list1.append(list(map(int,input().split())))
   
for j in list1:
    sum1=0
    for k in j:
        sum1=sum1+k
    print(sum1)

        