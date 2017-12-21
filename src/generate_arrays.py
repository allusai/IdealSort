#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:52:59 2017

@author: saikalyan
"""

#import sorting # Code re-use!
import random

def createRandomArray(size):
    arr = []
    
    # Add a random number to the array "size" times
    for i in range(0,size):
        arr.append(random.randint(0,100))
        
    return arr
    
def createNearlyAscendingArray(size):
    arr = []
    n = random.randint(1,5)
    
    # n*i provides some variation so not always [1,2,3]
    # random.randint(0,n-1) staggers the numbers so they don't
    # always increase by only 1
    for i in range(0,size):
        arr.append( (n*i) + random.randint(0,n-1) )

    # Swap around a few of the numbers to make it more random
    for s in range(0,size//40):
        firstIndex = random.randint(0,size-1)
        secondIndex = random.randint(0,size-1)
        temp = arr[firstIndex]
        arr[firstIndex] = arr[secondIndex]
        arr[secondIndex] = temp

    return arr
    
def createNearlyDescendingArray(size):
    arr = []
    n = random.randint(1,5)
    
    # n*i provides some variation so not always [5,4,3,2,1]
    # random.randint(0,n-1) staggers the numbers so they don't
    # always decrease by only 1
    for i in range(0,size):
        arr.append( (n*(size-i)) - random.randint(0,n-1) )

    # Swap around a few of the numbers to make it more random
    for s in range(0,size//40):
        firstIndex = random.randint(0,size-2)
        secondIndex = random.randint(0,size-2)
        temp = arr[firstIndex]
        arr[firstIndex] = arr[secondIndex]
        arr[secondIndex] = temp
        
    return arr

def createFewUniqueValuesArray(size):
    arr = []
    
    # Choose 1-4 different elements nUV = 2: [1,1,2,2,2,2,1,1,1]
    numUniqueVals = random.randint(1,4)
    
    # Which numbers to actually use 1-15
    numbersToChooseFrom = []
    
    for options in range(0,numUniqueVals):
        numbersToChooseFrom.append(random.randint(1,15))
        
    # Now fill up the array
    for i in range(0,size):
        # Pick a random index of the array numbersToChooseFrom
        indexOfOption = random.randint(0,numUniqueVals-1)
        n = numbersToChooseFrom[indexOfOption] # The actual number
        
        # Add the number at that index to the array
        arr.append(n)
        
    return arr
    
def createAscendingAndFewUniqueValuesArray(size):
    arr = []
    
    # Choose 1-4 different elements nUV = 2: [1,1,2,2,2,2,1,1,1]
    numUniqueVals = random.randint(1,4)
    
    # Which numbers to actually use 1-15
    numbersToChooseFrom = []
    
    for options in range(0,numUniqueVals):
        numbersToChooseFrom.append(random.randint(1,15))
        
    list.sort(numbersToChooseFrom)
        
    # Build the actual array by inserting the elements in order
    valIndex = 0
    
    for i in range(0,size):
        randNum = random.randint(0,size//numUniqueVals)
        
        if randNum == size//numUniqueVals and valIndex < numUniqueVals-1: 
            valIndex += 1
        
        arr.append(numbersToChooseFrom[valIndex])
        
    # Swap around a few of the numbers to make it more random
    for s in range(0,size//30):
        firstIndex = random.randint(0,size-1)
        secondIndex = random.randint(0,size-1)
        temp = arr[firstIndex]
        arr[firstIndex] = arr[secondIndex]
        arr[secondIndex] = temp
    
    return arr