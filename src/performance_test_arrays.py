#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:01:01 2018

@author: saikalyan
"""

# This module is capable of generating and returning the arrays used for
# creating the performance metrics in "performance_metrics.py"

import generate_arrays as generate

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


