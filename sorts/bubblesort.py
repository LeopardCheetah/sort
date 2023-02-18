'''
I'll do an explanation for bubble sort later

This sorting algorithm runs in O(n^2) time.
Analysis for the time complexity of the algorithm is at the bottom.
'''


import random


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# shuffle array (so it can be sorted)
random.shuffle(arr)


def bubble_sort(arr):
    items_sorted = 0
    swapped = True


    # again, another counter
    swaps_needed = 0


    # keep on taking the 0th index item and start swapping it with all the other indices
    while swapped:
        swapped = False
        for index in range(len(arr) - items_sorted - 1):
            # compare two indices and swap them if necessary

            if arr[index + 1] < arr[index]:
                # swap since the index before is bigger
                swapped = True
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swaps_needed += 1
        
        items_sorted += 1
        # this line technically isn't need but it def speeds up the algorithm by a factor of 2 (potentially)
    
    return arr

print()
print(arr)
print('This array was sorted in', swaps_needed, 'swaps.\n')

# Analysis:
# (Note: n is the number of items in the array)
#
# there is a for loop inside a while loop - the for loop scans thru at most n items (more specifically it scans thru (n - items sorted) number of items), 
# while the while loop will keep running while the array isn't sorted
#
# because in each iteration one item is getting sorted
# therefore the last iteration can have at most 1 swap
# the second to last can have at most 2 
# etc.
# therefore the first iteration can have at most n-1 swaps
# so the total number of swaps is (1 + 2 + 3 + ... + n-2 + n-1) = n(n-1)/2 = O(n^2)
# therefore this algorithm runs in worst case O(n^2)