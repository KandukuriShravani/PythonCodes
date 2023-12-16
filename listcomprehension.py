# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 19:06:23 2023

@author: 926824
"""

list1=[1,2,3,4]
# list2=[(item**2) for item in list1]
# print(list2)

# list2=[item for item in list1 if(item%2==0)]
# print(list2)

list2=[[j for j in list1]for item in list1]
print(list2)