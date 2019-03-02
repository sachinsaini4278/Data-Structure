# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 07:18:31 2019

@author: sachin saini
"""

def insertion_sort(inputarray):
    for i in range(size):
        temp=inputarray[i]
        j=i
        while(inputarray[j-1]>temp and j >=1):
            inputarray[j]=inputarray[j-1];
            j=j-1
        inputarray[j]=temp


print("Enter the size of input array")
size=int(input())

print("Enter the ", size ," elements of array")
inputarray=[int(x) for x in input().split()]

print("elements before sorting ",inputarray)
insertion_sort(inputarray)
print("elements after sorting ",inputarray)




