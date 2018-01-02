#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 16:44:00 2017

@author: saikalyan
"""
import sorting

# Sorting Evaluation module: This module contains the methods
# to determine which sorting algorithm (defined by an ID) is the
# fastest by manually trying out all of them (racing them).

# ID's
# 0: insertionSortWithTime()
# 1: binaryInsertionSortWithTime()
# 2: quickSortWithTime()
# 3: quickSort3WithTime()
# 4: shellSortWithTime()

# Races all 5 sorting methods, compares their times and returns
# just which one was the fastest (ID)
def raceAlgorithms(array):
    fastestTime = 10000 # 10000 seconds
    fastestID = -1
    
    for i in range(0,5):
        # Time each sorting algorithm on a copy of the array
        t = sort(i,list(array))
        
        if t < fastestTime:
            fastestTime = t
            fastestID = i
    
    return fastestID

        
# Sort(id), instead of calling each method by yourself, just pass in
# Sort(0) to do insertionSortWithTime or Sort(2) to do quickSortWithTime
# Returns the package of the sorted array and the time it took to solve
def sort(sort_id,array):
    if sort_id == 0:
        t = sorting.insertionSortWithTime(array)
        return t
    elif sort_id == 1:
        t = sorting.binaryInsertionSortWithTime(array)
        return t
    elif sort_id == 2:
        t = sorting.quickSortWithTime(array)
        return t
    elif sort_id == 3:
        t = sorting.quickSort3WithTime(array)
        return t
    elif sort_id == 4:
        t = sorting.shellSortWithTime(array)
        return t
    else:
        print("Sorry that sort doesn't exist!")
      
a = [2,3,4,5,1,234,245,23,547,3,543,426,3,654,2456,432,434,32,2424,423,
     652,25,4,5246,234,453,246,43,42,423,424,6,5,68,7,61,967,5,47,7988,57,64]
b = [1,34,23,86,2]
c = [2,2,2,1,1,1,5,5,5,2,2,2,2,2,2,1,1,1,1,1,1,1,1,5,5,5,5,5,5,2,1,2,1,5,2,1,
     5,5,1,2,5,1,5,2,1,2,5,2,1]
d = [20,19,18,17,16,15,14,13,11,12,10,7,9,8,6,5,4,3,2,1,0]

# This is a helpful function for the user to understand which ID
# corresponds to each sorting algorithm
def whichSortHasThisID(sort_id):
    if sort_id == 0:
        return "Insertion Sort"
    elif sort_id == 1:
         return "Binary Insertion Sort"
    elif sort_id == 2:
         return "QuickSort"
    elif sort_id == 3:
         return "QuickSort3"
    elif sort_id == 4:
         return "Shell Sort"
    else:
        return "Sorry that sort doesn't exist!"

        
fastest = raceAlgorithms(c)
print("Fastest algorithm was: ", fastest)

# Write these same trials in a test file that uses this module