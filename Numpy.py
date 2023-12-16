# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 08:42:44 2023

@author: 926824
"""
"""
Numpy is essentially come in two flavors either vectors or matrices.

Vectors are strictly one d arrays and matrices are two the two that missional.

We should also note that a matrix can still only have one row or one column.
"""
#Numpy Arrays

import numpy as np

my_list=[1,2,3]
print("list is: ")
print(my_list)

arr1=np.array(my_list)
print("array is: ")
print(arr1)

my_mat=[[1,2,3],[4,5,6],[7,8,9]]
arr2=np.array(my_mat)
print("array is: ")
print(arr2)

arr3=np.arange(0,10)
print(arr3)

arr4=np.arange(0,11,2)
print(arr4)

zeroarr=np.zeros(3)
print(zeroarr)

zeroarrtwod=np.ones((2,3))
print(zeroarrtwod)

linspacarr=np.linspace(0,5,10)
print(linspacarr)

#identity matrix
idenarr=np.eye(5)
print(idenarr)

#random
rad1=np.random.rand(5)
print(rad1)

rad2=np.random.randn(5)
print(rad2)

#[0,1]
rad3=np.random.rand(2,4) 
print(rad3)

rad4=np.random.randn(2,3)
print(rad4)

rad5=np.random.randint(1,100,10)
print(rad5)

arr = np.arange(25)
print(arr.reshape(5,5))

ranarr = np.random.randint(0,50,10)
print("{} {}".format(ranarr.max(),ranarr.argmax()))
print("{} {}".format(ranarr.min(),ranarr.argmin()))

print(rad3.shape)

print(rad4.dtype)