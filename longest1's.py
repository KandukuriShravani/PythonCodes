# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 15:03:52 2023

@author: 926824
"""

len1=int(input())
list1=list(map(int,input().split()))
list2=[]
counter=0
for i in range(len1):
    if list1[i]==1:
        counter=counter+1
        temp=i+1
        #print(temp)
        for j in range(temp,len1):
            if list1[j]==1:
                counter=counter+1
            else:
                break
    list2.append(counter)
    counter=0
longestlength=list2[0]
for k in list2:
    if k>longestlength:
        longestlength=k
print(longestlength)