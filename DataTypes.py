# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 08:23:56 2023

@author: 926824
"""
#Lists
my_list = ['a','b','c']
print(my_list[0:2])
my_list.append('d')
print(my_list)
print(my_list[0])
print(my_list[1:])
print(my_list[:2])
my_list[0] = 'NEW'
print(my_list)
nest = [1,2,3,[4,5,['target']]]
print(nest[3])
print(nest[3][2])
print(nest[3][2][0])

#Dictionaries
d = {'key1':'item1','key2':'item2'}
print(d)
print(d['key1'])
d1={'k1':[1,2,'a']}
print(d1['k1'][0])
mylist=d1['k1']
print(mylist)
d2={'k1':{'k2':['1','a','shravani']}}
print(d2['k1']['k2'])
print(d2['k1']['k2'][2])

#Tuples
t = (1,2,3)
print(t[0])
#t[1]='New'---------------> tuples are immutable.. we can't assign the values

#Sets
s={1,2,3,3}
print(s)
s1={1,2,3,1,2,1,2,3,3,3,3,2,2,2,1,1,2}
print(s1)
s.add(4)
print(s)
s.add(4)
print(s)
print(len(s))







