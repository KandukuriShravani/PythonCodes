# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:33:54 2023

@author: 926824
"""

# totalLength=int(input())
# list1=list(map(int,input().split()))
# list2=[]
# for i in list1:
#     list2.insert(0, i)
# print(list2)

totalLength=int(input())
list1=list(map(int,input().split()))
lsit2=[]
list2=list1[totalLength::-1]
for i in list2:
    print(i,end=" ")