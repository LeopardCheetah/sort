'''
For all intensive purposes, bogosort is a joke algorithm. 
The psuedocode for this algorithm can be written as followed:

1. Shuffle items randomly
2. Check if they're shuffled and go back to step 1 if they're not

Time complexity:
O(n!)

Please do not use this algorithm to do anything useful
'''

import random

# to be sorted
arr = [7, 5, 3, 2, 1, 4, 6]

# sorted arr
sorted_arr = [i+1 for i in range(len(arr))]

# counter to see how many shuffles it took (this isn't part of the sorting alg but you can get a sense of how inefficient this algorithm is)
counter = 0

while arr != sorted_arr:
    random.shuffle(arr)
    counter += 1


print("\nArray was sorted in", counter, "number of random shuffles.\n")

