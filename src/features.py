#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 16:13:31 2017

@author: saikalyan
"""
import numpy as np

#Features module: contains useful methods to find features of an array

# Returns the number of elements in the given array
def numElements(array):
    # Just returns the length of the array
    return len(array)

# Returns a number from -1.0 (completely descending)
# to 1.0 (completely ascending)
def sortScore(array):
    score = 0.0
    for i in range(0,len(array)-1):
        if array[i] < array[i+1]:
            score += 1.0
        elif array[i] > array[i+1]:
            score -= 1.0
    #Now normalize the sum
    score = score / (len(array)-1)
   # print(score)
    return score

# Returns the percentage of numbers that are unique
# If n = 10, 0.1 means 1 unique val, 1.0 means all unique vals
def uniqueVals(array):
    # Returns an array of the unique numbers, length of
    # this new array is how many unique elements there are
    u = np.unique(array)
   # print(len(u) / len(array))
    return len(u) / len(array)



#Tests
sortScore([5,1,7,3,5,3,8,2])
uniqueVals([3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,1,1,1,1])

a = [1,2,3,4,5]
print("Sort Score: ",sortScore(a))
print("Unique Vals: ",uniqueVals(a))
print("Number of Elements: ",numElements(a))
    