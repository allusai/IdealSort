#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:59:50 2017

@author: saikalyan
"""
import sorting

# The testing arrays we will use
a = [2,3,4,5,1,234,245,23,547,3,543,426,3,654,2456,432,434,32,2424,423,
     652,25,4,5246,234,453,246,43,42,423,424,6,5,68,7,61,967,5,47,7988,57,64]
b = [1,34,23,86,2]
c = [2,2,2,1,1,1,5,5,5,2,2,2,2,2,2,1,1,1,1,1,1,1,1,5,5,5,5,5,5,2,1,2,1,5,2,1,
     5,5,1,2,5,1,5,2,1,2,5,2,1] # Few unique vals
d = [20,19,18,17,16,15,14,13,11,12,10,7,9,8,6,5,4,3,2,1,0] # Reversed
e = [1,2,13,4,5,6,7,8,10,11,12,3,14,15,16,19,20,111,123,10] # Nearly sorted


# **Tests on the sorting algorithms**

# Showing that the sorting algorithms DO in fact sort the arrays
print("Starting tests to show that arrays are being sorted")

# list(a) makes a copy of the array to pass in
# so this way one test doesn't affect the other

print("Starting array: ", a)
sorting.insertionSortWithTime(a)
print("Insertion Sort works: ", a)
print()

print("Starting array: ", b)
sorting.binaryInsertionSortWithTime(b)
print("Binary Insertion Sort works: ", b)
print()

print("Starting array: ", c)
sorting.quickSortWithTime(c)
print("QuickSort works: ", c)
print()

print("Starting array: ", d)
sorting.quickSort3WithTime(d)
print("QuickSort3 works: ", d)
print()

print("Starting array: ", e)
sorting.shellSortWithTime(e)
print("Shell Sort works: ", e)
print()

print("Ending this round of tests")
print()


# Showing the time taken for each sort
print("Starting tests to show times for sorting")

arr = a # Running tests on the first array (random)
print(sorting.insertionSortWithTime(arr))
print(sorting.binaryInsertionSortWithTime(arr))
print(sorting.quickSortWithTime(arr))
print(sorting.quickSort3WithTime(arr))
print(sorting.shellSortWithTime(arr))
print("QuickSort (3rd) should be the fastest")
print()

arr = b # Running tests on the second array (small, random)
print(sorting.insertionSortWithTime(arr))
print(sorting.binaryInsertionSortWithTime(arr))
print(sorting.quickSortWithTime(arr))
print(sorting.quickSort3WithTime(arr))
print(sorting.shellSortWithTime(arr))
print("Insertion Sort (1st) should be the fastest")
print()


arr = c # Running tests on the third array (few unique vals)
print(sorting.insertionSortWithTime(arr))
print(sorting.binaryInsertionSortWithTime(arr))
print(sorting.quickSortWithTime(arr))
print(sorting.quickSort3WithTime(arr))
print(sorting.shellSortWithTime(arr))
print("QuickSort3 (4th) should be the fastest")
print()

arr = d # Running tests on the fourth array (reversed)
print(sorting.insertionSortWithTime(arr))
print(sorting.binaryInsertionSortWithTime(arr))
print(sorting.quickSortWithTime(arr))
print(sorting.quickSort3WithTime(arr))
print(sorting.shellSortWithTime(arr))
print("Shell Sort (5th) should be the fastest")
print()

arr = e # Running tests on the fifth array (nearly sorted)
print(sorting.insertionSortWithTime(arr))
print(sorting.binaryInsertionSortWithTime(arr))
print(sorting.quickSortWithTime(arr))
print(sorting.quickSort3WithTime(arr))
print(sorting.shellSortWithTime(arr))
print("Insertion Sort (1st) should be the fastest")
print()

print("Ending this round of tests")
print()

# Primitive way of comparing speed of algorithms
print("Comparing speed of algorithms")
arr = c

t = sorting.insertionSortWithTime(list(arr))
t2 = sorting.binaryInsertionSortWithTime(list(arr))
t3 = sorting.quickSortWithTime(list(arr))
t4 = sorting.quickSort3WithTime(list(arr))
t5 = sorting.shellSortWithTime(list(arr))

a = "%.2f" % (t/t4)
b = "%.2f" % (t2/t4)
d = "%.2f" % (t3/t4) 
e = "%.2f" % (t5/t4)


print("On the array: ",c)
print("Quick3 is ", a, " times as fast as Insertion Sort")
print("Quick3 is ", b, " times as fast as Binary Insertion Sort")
print("Quick3 is ", d, " times as fast as QuickSort")
print("Quick3 is ", e, " times as fast as Shell Sort")

print("Ending this round of tests")
print()

