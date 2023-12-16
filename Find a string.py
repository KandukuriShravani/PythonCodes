# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:24:35 2023

@author: 926824
"""

def count_substring(string, sub_string):
    lengthString=len(string)
    lengthSub=len(sub_string)
    counter=0
    for i in range((lengthString-lengthSub)+1):
        print(string[i:lengthSub+i])
        if string[i:lengthSub+i]==sub_string:
            counter= counter+1 
        
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)