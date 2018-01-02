#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:23:00 2017

@author: saikalyan
"""

import generate_arrays as generate
import random
import features
import sortingevaluation

# This program will create the .data file that is our dataset

# This is the matrix that will store our 200 arrays
dataArrays = [[] for _ in range(200)]

# This is the syntax we should use!
# dataArrays[0] = setArray(dataArrays[0]) 

# The first 20 rows will be random arrays of size 100 (QuickSort)
for index in range(0,20):
    size = 100
    dataArrays[index] = generate.createRandomArray(size)
    
# The next 20 rows will be arrays that are all nearly ascending (Insertion)
for index in range(20,40):
    size = 100
    dataArrays[index] = generate.createNearlyAscendingArray(size)
    
# The next 20 rows will be arrays that are all nearly descending (Shell)
for index in range(40,60):
    size = 100
    dataArrays[index] = generate.createNearlyDescendingArray(size)
    
# The next 20 rows will be arrays that have few unique vals (QuickSort3)
for index in range(60,80):
    size = 100
    dataArrays[index] = generate.createFewUniqueValuesArray(size)
    
# The next 20 rows will be arrays that are very small (Insertion)
for index in range(80,100):
    size = 8
    dataArrays[index] = generate.createRandomArray(size)
    

# Now, the above cases should be very straightforward but most of the time
# the array won't be as clear cut, so we have to provide some "real data"
# which could have multiple significant features

# Small and random
for index in range(100,120):
    size = random.randint(5,50)
    dataArrays[index] = generate.createRandomArray(size)
    
# Small and ascending
for index in range(120,140):
    size = random.randint(5,20)
    dataArrays[index] = generate.createNearlyAscendingArray(size)
    
# Small and few unique vals
for index in range(140,160):
    size = random.randint(5,20)
    dataArrays[index] = generate.createFewUniqueValuesArray(size)
    
# Ascending and few unique vals
for index in range(160,180):
    size = random.randint(50,100)
    dataArrays[index] = generate.createAscendingAndFewUniqueValuesArray(size)

# Small and descending
for index in range(180,200):
    size = 100
    dataArrays[index] = generate.createNearlyDescendingArray(size)
    

# Now to actually write the file that contains the data in csv format
file = open("testfile.txt","w")

for i in range(0,200):
    arr = dataArrays[i]
    
    # Analyze the features of this array
    feature1 = features.sortScore(arr)
    feature2 = features.uniqueVals(arr)
    feature3 = features.numElements(arr)
    
    # Find the fastest algorithm for this array
    algorithm = sortingevaluation.raceAlgorithms(arr)
    
    # Write this data
    line = str(feature1) + "," + str(feature2) + "," + str(feature3)
    line += "," + str(algorithm) + "\n"
    
    file.write(line)
    
    