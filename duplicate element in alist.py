# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:47:57 2023

@author: 926824
"""

totalLength=int(input())
list1=list(map(int,input().split()))
list2=[]
num=0
duplicate=0
count=0
while(totalLength>0):
    duplicate=list1[num]
    for i in list1:
        #print(duplicate)
        if duplicate==i:
            #print(duplicate,i)
            count=count+1
        if count==2:
            print(i)
            break
    if count==2:        
        break
    count=0
    num=num+1
    totalLength=totalLength-1
        
        
        