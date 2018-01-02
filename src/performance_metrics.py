#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 22:24:58 2018

@author: saikalyan
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import subprocess # Runs helper python scripts in other python scripts
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