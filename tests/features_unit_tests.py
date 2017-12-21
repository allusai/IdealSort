#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:16:07 2017

@author: saikalyan
"""

import features

# These are tests for identifying the features of various arrays
a = [1,2,3,4,5]
print("For the array: ", a)
print("Sort Score: ", features.sortScore(a)) # 1.0 since sorted
print("Unique Vals: ", features.uniqueVals(a)) # 1.0 since all different
print("Number of Elements: ", features.numElements(a)) # n = 5
print()

a = [1,1,1,1,1]
print("For the array: ", a)
print("Sort Score: ", features.sortScore(a)) # 1.0 since sorted
print("Unique Vals: ", features.uniqueVals(a)) # 0.0 since all same
print("Number of Elements: ", features.numElements(a)) # n = 5
print()

a = [3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,1,1,1,1]
print("For the array: ", a)
print("Sort Score: ", features.sortScore(a))
print("Unique Vals: ", features.uniqueVals(a))
print("Number of Elements: ", features.numElements(a))
print()

a = [5,1,7,3,5,3,8,2]
print("For the array: ", a)
print("Sort Score: ", features.sortScore(a))
print("Unique Vals: ", features.uniqueVals(a))
print("Number of Elements: ", features.numElements(a))
print()

a = [20,19,18,17,16,15,14,13,11,12,10,7,9,8,6,5,4,3,2,1,0] # Reversed
print("For the array: ", a)
print("Sort Score: ", features.sortScore(a))
print("Unique Vals: ", features.uniqueVals(a))
print("Number of Elements: ", features.numElements(a))
print()

a = [1,2,13,4,5,6,7,8,10,11,12,3,14,15,16,19,20,111,123,10] # Nearly sorted
print("For the array: ", a)
print("Sort Score: ", features.sortScore(a))
print("Unique Vals: ", features.uniqueVals(a))
print("Number of Elements: ", features.numElements(a))
print()
