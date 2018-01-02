# IdealSort
Analyzes the dataset for features and uses a machine learning model to pick the optimal sorting algorithm.

IdealSort is faster by 30% than just using any one sorting algorithm by taking advantage of "adaptive" sorting algorithms.
Some sorting algorithms like QuickSort3 or Shell Sort perform in nearly O(n) time for special situations. For extremely large
datasets (think 100 arrays of size 100 each), IdealSort's forethought actually results in an average 85% increase in sorting
speed even after accounting for the time to analyze the features of the dataset.

This is an oversimplification of the machine learning decision tree of the model, but usually:
When the list is nearly sorted, IdealSort picks Insertion Sort.        ex: [1,2,4,3,5]
When the list is small, IdealSort also picks Insertion Sort.           ex: [1,2,3]
When the list is nearly reversed, IdealSort picks Shell Sort.          ex: [9,7,8,6,5,4,3,1,2]
When the list only has a few key values, IdealSort picks QuickSort3.   ex: [2,2,1,1,1,1,3,3,3]
When the list is random, IdealSort picks QuickSort.                    ex: [3,18,4,7,0,1]

Descriptions of each sorting algorithm can be found at: https://www.toptal.com/developers/sorting-algorithms


