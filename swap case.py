# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 19:33:12 2023

@author: 926824
"""

def swap_case(s):
    convertedString=""
    lengthS=len(s)
    for i in range(lengthS):
        if s[i].isupper():
            convertedString=convertedString+s[i].lower()
        elif s[i].islower():
            convertedString=convertedString+s[i].upper()
        else:
            convertedString=convertedString+s[i]
            
    return convertedString

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)