# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:39:10 2023

@author: 926824
"""


list1=[]
outputlist=[]
N = int(input())
for i in range(N):
    x=input().split()
    list1.append(x)
for j in range(N):
    if list1[j][0]=="insert":
        outputlist.insert(int(list1[j][1]),int(list1[j][2]))
    elif list1[j][0]=="print":
        print(outputlist)
    elif list1[j][0]=="append":
        outputlist.append(int(list1[j][1]))
    elif list1[j][0]=="sort":
        outputlist.sort()
    elif list1[j][0]=="pop":
        outputlist.pop()
    else:
        outputlist.reverse()
print(outputlist)

            
            