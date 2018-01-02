#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:01:01 2018

@author: saikalyan
"""

# This module is capable of generating and returning the arrays used for
# creating the performance metrics in "performance_metrics.py"

import generate_arrays as generate
import sortingevaluation as sorteval

def createDataArrays():
    # This is the matrix that will store our 300 arrays
    dataArrays = [[] for _ in range(300)]

    # This is the syntax we should use!
    # dataArrays[0] = setArray(dataArrays[0]) 

    # The first 100 rows will be arrays that are all nearly ascending (Insertion)
    for index in range(0,100):
        size = 100
        dataArrays[index] = generate.createNearlyAscendingArray(size)
    
    # The next 100 rows will be arrays that are all nearly descending (Shell)
    for index in range(100,200):
        size = 100
        dataArrays[index] = generate.createNearlyDescendingArray(size)
    
    # The next 100 rows will be arrays that have few unique vals (QuickSort3)
    for index in range(200,300):
        size = 100
        dataArrays[index] = generate.createFewUniqueValuesArray(size)
        
    return dataArrays

# Pass in a matrix and the indexes of the arrays you want to use
def averageIdealSortTime(arrays,start,end):
    
    totalTime = 0
    
    # Loop through the given indexes
    for i in range(start,end):
        #Fastest algorithm (ideal sorting algorithm)
        ID = sorteval.raceAlgorithms(arrays[i])
        
        #Time the speed of that array
        t = sorteval.sort(ID,arrays[i])
        
        #Add to the total
        totalTime += t
        
    return totalTime/(end-start)

# Pass in a matrix and the indexes of the arrays you want to use
def averageInsertionSortTime(arrays,start,end):
    
    totalTime = 0
    
    # Loop through the given indexes
    for i in range(start,end):
        #Fastest algorithm (ideal sorting algorithm)
        ID = 0
        
        #Time the speed of that array
        t = sorteval.sort(ID,arrays[i])
        
        #Add to the total
        totalTime += t
        
    return totalTime/(end-start)

# Pass in a matrix and the indexes of the arrays you want to use
def averageBinaryInsertionSortTime(arrays,start,end):
    
    totalTime = 0
    
    # Loop through the given indexes
    for i in range(start,end):
        #Fastest algorithm (ideal sorting algorithm)
        ID = 1
        
        #Time the speed of that array
        t = sorteval.sort(ID,arrays[i])
        
        #Add to the total
        totalTime += t
        
    return totalTime/(end-start)

# Pass in a matrix and the indexes of the arrays you want to use
def averageQuickSortTime(arrays,start,end):
    
    totalTime = 0
    
    # Loop through the given indexes
    for i in range(start,end):
        #Fastest algorithm (ideal sorting algorithm)
        ID = 2
        
        #Time the speed of that array
        t = sorteval.sort(ID,arrays[i])
        
        #Add to the total
        totalTime += t
        
    return totalTime/(end-start)

# Pass in a matrix and the indexes of the arrays you want to use
def averageQuickSort3Time(arrays,start,end):
    
    totalTime = 0
    
    # Loop through the given indexes
    for i in range(start,end):
        #Fastest algorithm (ideal sorting algorithm)
        ID = 3
        
        #Time the speed of that array
        t = sorteval.sort(ID,arrays[i])
        
        #Add to the total
        totalTime += t
        
    return totalTime/(end-start)

# Pass in a matrix and the indexes of the arrays you want to use
def averageShellSortTime(arrays,start,end):
    
    totalTime = 0
    
    # Loop through the given indexes
    for i in range(start,end):
        #Fastest algorithm (ideal sorting algorithm)
        ID = 4
        
        #Time the speed of that array
        t = sorteval.sort(ID,arrays[i])
        
        #Add to the total
        totalTime += t
        
    return totalTime/(end-start)
    