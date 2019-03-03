# -*- coding: utf-8 -*-
"""

@author: sachin saini

Topic: QuickSort in Python

"""


#funvtion to calculate the position of pivot
def findPositionOfPivot(inputarray,left,right):
    pivot=inputarray[right] #choose pivot as last element of the array
    i=left-1 #set i to left-1
    for j in range(left,right): #start loop from left to right
        if(inputarray[j]<=pivot): #if element is less than the pivot element then swap i+1th element to jth element
            i=i+1
            inputarray[i],inputarray[j]=inputarray[j],inputarray[i]
    inputarray[i+1],inputarray[right]=inputarray[right],inputarray[i+1] #finally swap the i+1th element to pivot(last element) 
    return i+1 #i+1 is the position of pivot element so return it

#function to perform quicksort    
def quick_sort(inputarray,left,right):
    if(left<right):
        middle=findPositionOfPivot(inputarray,left,right)
        quick_sort(inputarray,left,middle-1)
        quick_sort(inputarray,middle+1,right)
        
    
print("Enter the size of input array")
size= int(input())

print("Enter the ", size ," elements of array")

#Take input from user
inputarray=[int(x) for x in input().split()]
print("elements before sorting ",inputarray)
quick_sort(inputarray,0,size-1)
print("elements after sorting ",inputarray)

