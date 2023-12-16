# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 12:29:52 2023

@author: 926824
"""

import numpy as np
arr = np.arange(0,10)
print(arr + arr)
print(arr - arr)
print(arr * arr)
print(arr ** arr)

#this is only possible with numpy libs , we will get warning but it will print output
print(arr/arr)
print(1/arr)

#Taking Square Roots
print(np.sqrt(arr))

#Calcualting exponential (e^)
print(np.exp(arr))

#same as arr.max()
print(np.max(arr))
#or
print(arr.max())

print(np.log(arr))

print(np.sin(arr))