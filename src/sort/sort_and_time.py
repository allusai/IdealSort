#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:04:37 2017

@author: saikalyan
"""
import time
import random

#Sorting Module: Sorts an array and returns time to sort

# Useful methods:
# id 0: insertionSortWithTime() returns arr,t (need to capture both)
# 1: binaryInsertionSortWithTime()
# 2: quickSortWithTime()
# 3: quickSort3WithTime()
# 4: shellSortWithTime()
# Just pass in an array and it will sort and give you the arr and time

# Helper swap function
def swap(arr,i,j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
# Helper binary insert function, returns index where
# val is supposed to be (for insertion sort)
def binarySearch(val,start,end,array):
    mid = (start+end)//2 # Integer division to find middle
    if start < end:  
        if val > array[mid]:
            return binarySearch(val,mid+1,end,array)
        elif val < array[mid]:
            return binarySearch(val,start,mid-1,array)
        elif val == array[mid]:
            return mid
    else:
        if array[mid] < val:
            return mid+1  
        else:
            return mid

# Insertion Sort
def insertionSortWithTime(a):
    
    array = a
    # Start time
    start = time.time()
    
    for k in range(1,len(array)):
        i = k
        j = k-1
        while (array[i] < array[j] and i > 0):
            swap(array,i,j)
            i -= 1
            j -= 1
    
    #End time
    end = time.time()
    
    return (array,end-start)

# Binary Insertion Sort
def binaryInsertionSortWithTime(array):
    # Start time
    start = time.time()
    
    for i in range(1,len(array)):
        #Find the correct location for this element
        targetIndex = binarySearch(array[i],0,i-1,array)
        
        #Swap up until that location
        j = i # Points to element being sorted
        k = i-1 # Points to next swap location
        
        while targetIndex < j:
            swap(array,j,k)
            j -= 1
            k -= 1
            
    
    #End time
    end = time.time()
    
    return (array,end-start)

# Quicksort @author: Interactive Python
def quickSortWithTime(alist):
    # Start time
    start = time.time()
    
    quickSortHelper(alist,0,len(alist)-1)
    
    #End time
    end = time.time()
    
    return (alist,end-start)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


# QuickSort3 (adaptive O(n) for few unique values [1,1,2,2,2,2,3,3,3])
# @authors: Elen (original) and nino_701 (contributor) on Stack Overflow
def quickSort3WithTime(array):
    # Start time
    start = time.time()
    
    randomized_quick_sort(array,0,len(array)-1)
    
    #End time
    end = time.time()
    
    return (array,end-start)

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);
    
def partition3(a, l, r):
   x, j, t = a[l], l, r
   i = j

   while i <= t :
      if a[i] < x:
         a[j], a[i] = a[i], a[j]
         j += 1

      elif a[i] > x:
         a[t], a[i] = a[i], a[t]
         t -= 1
         i -= 1 # remain in the same i in this case
      i += 1   
   return j, t


# Shell Sort
# @authors: Interactive Python
def shellSortWithTime(alist):
    # Start time
    start = time.time()
    
    sublistcount = len(alist)//2
    while sublistcount > 0:

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      sublistcount = sublistcount // 2
      
    # End time
    end = time.time()
    
    return (alist,end-start)

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue
        
        
# Races all 5 sorting methods, compares their times and returns
# just which one was the fastest (ID)
        
# Sort(id), instead of calling each method by yourself, just pass in
# Sort(0) to do insertionSortWithTime or Sort(2) to do quickSortWithTime
# Returns the package of the sorted array and the time it took to solve
def sort(sort_id,array):
    if sort_id == 0:
        arr,t = insertionSortWithTime(array)
        return (arr,t)
    elif sort_id == 1:
        arr,t = binaryInsertionSortWithTime(array)
        return (arr,t)
    elif sort_id == 2:
        arr,t = quickSortWithTime(array)
        return (arr,t)
    elif sort_id == 3:
        arr,t = quickSort3WithTime(array)
        return (arr,t)
    elif sort_id == 4:
        arr,t = shellSortWithTime(array)
        return (arr,t)
    else:
        print("Sorry that sort doesn't exist!")


a = [2,3,4,5,1,234,245,23,547,3,543,426,3,654,2456,432,434,32,2424,423,
     652,25,4,5246,234,453,246,43,42,423,424,6,5,68,7,61,967,5,47,7988,57,64]
b = [1,34,23,86,2]
c = [2,2,2,1,1,1,5,5,5,2,2,2,2,2,2,1,1,1,1,1,1,1,1,5,5,5,5,5,5,2,1,2,1,5,2,1,
     5,5,1,2,5,1,5,2,1,2,5,2,1]
d = [20,19,18,17,16,15,14,13,11,12,10,7,9,8,6,5,4,3,2,1,0]

arr,t = insertionSortWithTime(a)
print(a)
print(arr)
arr2,t2 = binaryInsertionSortWithTime(a)
arr3,t3 = quickSortWithTime(a)
arr4,t4 = quickSort3WithTime(a)
arr5,t5 = shellSortWithTime(c)
