# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 22:39:56 2023

@author: 926824
"""
if __name__ == '__main__':
    num = []
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
        num.append(score)
        
    num.sort()
    second_min = 0
    mini = num[0]
    arr.sort()
    for i in num:
        if i != mini:
            second_min = i
            break
    
    for i in arr:
        if i[1] == second_min:

            print(i[0])