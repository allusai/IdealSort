#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 18:30:20 2017

@author: saikalyan
"""

import sortingevaluation

# The testing arrays we will use
a = [2,3,4,5,1,234,245,23,547,3,543,426,3,654,2456,432,434,32,2424,423,
     652,25,4,5246,234,453,246,43,42,423,424,6,5,68,7,61,967,5,47,7988,57,64]
b = [1,34,23,86,2]
c = [2,2,2,1,1,1,5,5,5,2,2,2,2,2,2,1,1,1,1,1,1,1,1,5,5,5,5,5,5,2,1,2,1,5,2,1,
     5,5,1,2,5,1,5,2,1,2,5,2,1] # Few unique vals
d = [20,19,18,17,16,15,14,13,11,12,10,7,9,8,6,5,4,3,2,1,0] # Reversed
e = [1,2,13,4,5,6,7,8,10,11,12,3,14,15,16,19,20,111,123,10] # Nearly sorted
        
fastest = sortingevaluation.raceAlgorithms(a)
print("Fastest algorithm for a (random) was: ", 
      sortingevaluation.whichSortHasThisID(fastest))


fastest = sortingevaluation.raceAlgorithms(b)
print("Fastest algorithm for b (small,random) was: ", 
      sortingevaluation.whichSortHasThisID(fastest))

fastest = sortingevaluation.raceAlgorithms(c)
print("Fastest algorithm for c (few unique vals) was: ", 
      sortingevaluation.whichSortHasThisID(fastest))

fastest = sortingevaluation.raceAlgorithms(d)
print("Fastest algorithm for d (reversed) was: ", 
      sortingevaluation.whichSortHasThisID(fastest))

fastest = sortingevaluation.raceAlgorithms(e)
print("Fastest algorithm for e (nearly sorted) was: ", 
      sortingevaluation.whichSortHasThisID(fastest))

