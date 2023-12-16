# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 23:01:54 2023

@author: 926824
"""

a=input()
b=input()
spclcharCount=a.count("?")

lengthA=len(a)
lengthB=len(b)

mydict = dict()


listB=b.split()
listUniqueB=[]
for i in b:
    if listUniqueB.count(i)==0:
        listUniqueB.append(i)
print(listUniqueB)

for i in listUniqueB:
    mydict[i]=a.count(i)
print(mydict)
        
print(spclcharCount)




