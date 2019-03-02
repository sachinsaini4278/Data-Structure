# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 06:30:44 2019

@author: sachin saini

"""

def bubble_sort(inputarray):
    
    for i in range(size):
        for j in range(0,size-i-1):
            if inputarray[j]>inputarray[j+1]:
                inputarray[j],inputarray[j+1]=inputarray[j+1],inputarray[j]



print("Enter the size of input array")
size = int(input())
print("Enter the ", size ," elements of array")

#Take input from user
inputarray=[int(x) for x in input().split()] # input().split() reads a line which is then split into its whitespace-separated components. So a line like 1 3 2 5 7 3 becomes the list ['1', '3', '2', '5', '7', '3'].
                                        #int(x) for x in  .This expression evaluates to a generator which transforms the elements of the list into their int() representations.
print("elements before sorting ",inputarray)
bubble_sort(inputarray)
print("elements after sorting ",inputarray)

