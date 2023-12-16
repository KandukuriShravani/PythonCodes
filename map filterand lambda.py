# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:22:51 2023

@author: 926824
"""

def powerOfVar(x):
    return x**2
# lambda x:x**2
print(powerOfVar(2))

list1=[1,2,3,4]
# list2=list(map(powerOfVar,list1))
# print(list2)

list2=list(map(lambda x: x**2,list1))
print(list2)

list3=list(filter(lambda x: x%2==0,list1))
print(list3)




