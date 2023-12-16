# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:09:18 2023

@author: 926824
"""

row = int(input())
column = row

for i in range(row):
    for j in range(column):
        print("*", end=" ")
    print(end="\n")