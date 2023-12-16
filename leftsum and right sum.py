# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:36:40 2023

@author: 926824
"""

len1=int(input())
list1=list(map(int,input().split()))
leftSum=0
rightSum=0
val=0
list2=[]
for k in range(len1):
    if k ==0:
        leftSum=0
        for l in range(k+1,len1):
            rightSum=rightSum+list1[l]
            #print(rightSum)
    elif k==len1-1:
        rightSum=0
        for r in range(len1-1):
            leftSum=leftSum+list1[r]
    else:
        for l in range(0,k):
            leftSum=leftSum+list1[l]
        for r in range(k+1,len1):
            rightSum=rightSum+list1[r]
    val=leftSum-rightSum
    list2.append(abs(val))
    val=0
    leftSum=0
    rightSum=0
for k in list2:
    print(k,end=" ")
    