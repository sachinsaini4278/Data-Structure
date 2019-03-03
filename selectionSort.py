# -*- coding: utf-8 -*-
"""
@author: sachin saini

Topic : Selection Sort in python
"""

#Function for performing selection sort. 
def selection_sort(inputarray):
    for i in range(size-1):
        min_index=i #let intially minimum element is element on ith index
        for j in range(i+1,size):  #loop through ith + 1 to find the minimum 
            if (inputarray[j]<inputarray[min_index]):
                min_index=j #if any element found then chanage the minimum index
            
        inputarray[min_index],inputarray[i]=inputarray[i],inputarray[min_index] #swap minimum to ith position element
        
        
        
print("Enter the size of input array")
size = int(input())
print("Enter the ", size ," elements of array")

#Take input from user
inputarray=[int(x) for x in input().split()] # input().split() reads a line which is then split into its whitespace-separated components. So a line like 1 3 2 5 7 3 becomes the list ['1', '3', '2', '5', '7', '3'].
                                        #int(x) for x in  .This expression evaluates to a generator which transforms the elements of the list into their int() representations.
print("elements before sorting ",inputarray)
selection_sort(inputarray)
print("elements after sorting ",inputarray)

