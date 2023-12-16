# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:36:30 2023

@author: 926824
"""

totalLength=int(input())
list1=list(map(int,input().split()))
sum=0
for i in list1:
    if i%2!=0:
        sum=sum+i
print(sum)