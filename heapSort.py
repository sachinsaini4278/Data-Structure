# -*- coding: utf-8 -*-
"""
@author: sachin saini

Topic: Heap Sort 
"""
#we are using max heap 

def build_max_heap(inputarray,totalsize,parent_node):
    largest=parent_node #take a variable largest and initially parent is largest
    leftChild=(2*largest)+1 #left child will be on the position of 2*i+1 where i is the parent node
    rightChild=(2*largest)+2 #same as right child will be on the position of 2*i+2
    
    #As we know that all leaf nodes are already max heap so we will only put the condition on nonleaf nodes
    if(leftChild<totalsize and inputarray[largest]<inputarray[leftChild]):#Check the condition that is left node is not leaf node and find the largest among parent and leftChild 
        largest=leftChild
    if(rightChild<totalsize and inputarray[largest]<inputarray[rightChild]):
        largest=rightChild
    if(largest is not parent_node):#//if current node is not max heap then swap with largest of its left/right children
        inputarray[largest],inputarray[parent_node]=inputarray[parent_node],inputarray[largest]
        build_max_heap(inputarray,totalsize,largest)#we call this fumction again to check whether after swapping node is following the max heap condition or not

def heap_sort(inputarray,totalsize):
    #as leaf node are already sorted then we start from the nonleaf nodes 
    for i in range(int(totalsize/2)-1,-1,-1):
        build_max_heap(inputarray,totalsize,i)
    #now extract the element one by one so here we will swap last element to the root node and call build_max_heap function on it
    for i in range((totalsize-1),-1,-1):
        inputarray[0],inputarray[i]=inputarray[i],inputarray[0]
        build_max_heap(inputarray,i,0)

print("Enter the size of input array")
size = int(input())
print("Enter the ", size ," elements of array")

#Take input from user
inputarray=[int(x) for x in input().split()]
print("elements before sorting ",inputarray)
heap_sort(inputarray,size)
print("elements after sorting ",inputarray)