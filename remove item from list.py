# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:44:39 2023

@author: 926824
"""

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    countOfNum=int(input())
    inputData=input()
    inputList=[]
    positionToDelete=int(input())-1
    inputList=inputData.split()
    inputList.remove(inputList[positionToDelete])
    print(countOfNum)
    print(inputList)
    


if __name__ == '__main__':
    main()