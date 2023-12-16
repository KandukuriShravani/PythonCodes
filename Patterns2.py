# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 17:18:04 2023

@author: 926824
"""

row = int(input())

for i in range(row):
    for j in range(i+1):
        print("*", end=" ")
    print("\n")