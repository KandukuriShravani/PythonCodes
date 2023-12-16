# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 22:59:33 2023

@author: 926824
"""

list1=[[0, 0, 1], [0, 0, 0], [0, 0, 0]]
isIdentityMatrix=True
lengthList1=len(list1)

for i in range(lengthList1):
    for j in range(i+1):
        if i==j:
            if list1[i][j]!=1:
                isIdentityMatrix=False
                break
        else:
            if i!=j:
                if list1[i][j]!=0:
                    isIdentityMatrix=False
                    break
print(isIdentityMatrix)