#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 22:24:58 2018

@author: saikalyan
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import performance_test_arrays as gen

 
objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
y_pos = np.arange(len(objects))
performance = [10,8,6,4,2,1]
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Usage')
plt.title('Programming language usage')
 
plt.show()

# 3 Key Cases: Nearly ascending, nearly descending, few unique vals

# The graph is going to be a line graph with the x-axis representing
# an increase in the size of the array, and the y-axis as the time to
# sort the array in 10^-5 seconds. There will be a line for each sorting
# algorithm. There will be three graphs (one for each of the cases)

names = ['Insertion','Binary Insertion','Quick','Quick3','Shell','Ideal']

# The matrix of test arrays
arrays = gen.createDataArrays()
# print(arrays[251])  Works!

# These are the average times on these 300 arrays for each sorting algorithm
averageIdealSort = gen.averageIdealSortTime(arrays,0,300)
averageInsertionSort = gen.averageInsertionSortTime(arrays,0,300)
averageBinInsertionSort = gen.averageBinaryInsertionSortTime(arrays,0,300)
averageQuickSort = gen.averageQuickSortTime(arrays,0,300)
averageQuickSort3 = gen.averageQuickSort3Time(arrays,0,300)
averageShellSort = gen.averageShellSortTime(arrays,0,300)

# Store the average times in an array for convenience
averageTimes = [averageIdealSort,averageInsertionSort,averageBinInsertionSort,
                averageQuickSort,averageQuickSort3,averageShellSort] 
for n in range(1,6):
    print(averageTimes[n]/averageTimes[0])