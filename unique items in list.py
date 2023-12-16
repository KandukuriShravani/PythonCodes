# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 08:44:12 2023

@author: 926824
"""

length=int(input())
l=length
list1=list(map(int,input().split()))
uniqueList=[]
repeatedList=[]
counter=0

increment=0
#print(list1)
while(l>0):   
    first=list1[counter]
    for j in list1:
        if first==j:
            increment=increment+1
        if increment>=2:
            repeatedList.append(first)
    increment=0
    counter=counter+1
    l=l-1
#repeatedList=list(set(repeatedList))
#print(repeatedList)

for k in list1:
    if k not in repeatedList:
        uniqueList.append(k)

for item in uniqueList:
    print(item,end=" ")
            
        
        

        


        