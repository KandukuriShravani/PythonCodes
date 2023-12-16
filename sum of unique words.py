# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 21:21:35 2023

@author: 926824
"""

def set_operation(sent1,sent2):
    ''' input:sent1,sent2-two sentences taken as inputs
         output:return the sum of length of unique words.'''
    
    # YOUR CODE GOES HERE
    list1=sent1.split()
    list2=sent2.split()
    list3=[]
    list4=[]
    length1=len(list1)
    length2=len(list2)
    for i in list1:
        if sent1.count(i)>1:
            if list3.count(i)==0:                
                list3.append(i)
                length1=length1-1            
    #print(length1)
    for j in list2:
        if sent2.count(j)>1:
            if list4.count(j)==0:                
                list4.append(j)
                length2=length2-1
    #print(length2)
    print(length1+length2)

i1=input()
i2=input()
set_operation(i1,i2)
