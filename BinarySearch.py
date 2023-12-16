# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:54:38 2023

@author: 926824
"""
size=int(input())
k=int(input())
lst=[]
for i in range(size):
    a=int(input())
    lst.append(a)
              
lst.sort()
l=0
h=size-1
#print(lst)
while(l<=h):
    m=int((l+h)/2)
    if k==lst[m]:
        print(m)
        break
    elif lst[m]>k:
        h=m-1
    else:
        l=m+1
        
    
    