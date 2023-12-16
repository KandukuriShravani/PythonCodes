# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 23:16:46 2023

@author: 926824
"""
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    AB=set(arr)
    A=list(AB)    
    largest=A[0]
    
    for i in range(1,len(A)):
        if A[i]>largest:
            largest=A[i]
    
    A.remove(largest)  
    if len(A)>0:
        secondLargest=A[0]
        for j in range(1,len(A)):
            if A[j]>secondLargest:
                secondLargest=A[j]
    
    if len(A)>0:        
        print(secondLargest)
    else:
        print(-1)
    