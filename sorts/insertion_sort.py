import random

arr = [i+1 for i in range(20)]
# this array now holds the first 20 numbers in order

random.shuffle(arr)
# nvm it's shuffled



'''
Insertion sort is an O(n^2) worst case, O(n) best case algorithm. 
It works by basically maintaining a section of the array that is sorted, and the other section that is an unsorted mess.
On each iteration, it will take the first number in the unsorted mess and throw it into the sorted section then sort it using swaps
'''

def insertion_sort(ls):
    for iter in range(len(ls)):
        # iter represents the number of items sorted before that iteration

        to_sort_pos = iter

        if iter == 0:
            # base case, first element
            continue

        # toggle the < to switch it from sorted ascended vs sorted descended
        while ls[to_sort_pos] < ls[to_sort_pos - 1] and to_sort_pos > 0:
            # swap
            ls[to_sort_pos], ls[to_sort_pos - 1] = ls[to_sort_pos - 1], ls[to_sort_pos]
            to_sort_pos -= 1
            continue
        continue

    # yes, this can return the list but since it swaps in place ill just leave it as is
    return 

print(arr)
insertion_sort(arr)
print(arr)