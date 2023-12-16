# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 01:28:17 2023

@author: 926824
"""

list2=list(map(int,input().split()))
len1=list2[0]
len2=list2[1]
list1=[]
list2=[]
for i in range(len1):
   list1.append(list(map(int,input().split())))
for j in range(len1):
   list2.append(list(map(int,input().split())))

for row in range(len1):
    for column in range(len2):
        print(list1[row][column]+list2[row][column],end=" ")
    print()