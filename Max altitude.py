# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:16:12 2023

@author: 926824
"""
len1=int(input())
list1=list(map(int,input().split()))
sumOf=0
list2=[]
for i in range(len1):
    sumOf=sumOf+list1[i]
    list2.append(sumOf)

longestlength=list2[0]
for k in list2:
    if k>longestlength:
        longestlength=k
print(longestlength)
    