# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 18:19:24 2023

@author: 926824
"""
import numpy as np

#Indexing
arr = np.arange(0,11)
print(arr)
print(arr[8])
print(arr[1:5])
arr[0:5]=100
print(arr)


arr = np.arange(0,11)
slice_of_arr = arr[0:6]
print(slice_of_arr)
print(arr)

slice_of_arr[:]=99
print(slice_of_arr)
print(arr)

copy_arr=arr.copy()
copy_arr[:]=100
print(copy_arr)
print(arr)

arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))
print(arr_2d)

print(arr_2d[1])
print(arr_2d[1][0])

print(arr_2d[1,0])

# 2D array slicing

#Shape (2,2) from top right corner
print(arr_2d[:2,1:])

arr = np.arange(1,11)
print(arr)
print(arr > 4)
bool_arr = arr>4
print(bool_arr)

print(arr[bool_arr])


arr2d = np.zeros((11,10))
arr_length = arr2d.shape[1]
#Set up array

for i in range(arr_length):
    arr2d[i] = i

print(arr2d)




