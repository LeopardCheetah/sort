# see https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/78a3c3444de1ff837f81e52991c24a86_MIT6_006S20_lec5.pdf
# page 3

# basically instead of sorting a big long thing, break it up and sort the individual pieces from back to front



# DISCLAIMER
# Tuple sort uses bubble sort
# bubble sort is O(n^2), and one round of tuple sort will call bubble sort multiple (4 for now) times
# so this algorithm takes a long time to run or at least pass 100 test cases with




######################################
############# UNUSED #################
######################################

def get_bound(mod, max_num):
    # get bound
    # or how many bits/chars in the specific mod needed to hold that max_num
    # you could theoretically bsearch this
    # that's a little goofy for what I'm doing


    bound = 0
    while max_num >= 1:
        bound += 1
        max_num = max_num // mod 
    
    return bound

######################################
######################################
######################################



import copy


# we're gonna use bubble sort as our sorting algorithm
# (comments removed)
# edited to sort based on keys

def bubble_sort(ls, key):
    # key will just be a number (index of value being sorted)

    arr = copy.deepcopy(ls) # lets not change what's given thanks

    items_sorted = 0
    swapped = True

    while swapped:
        swapped = False
        for index in range(len(arr) - items_sorted - 1):
            if get_val(arr[index + 1], key) < get_val(arr[index], key):
                swapped = True
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
    
    return arr


def generic_sorting_algorithm(arr):
    return bubble_sort(arr)


def num_to_tuple(num, mod, bits):
    # so i implemented finding the number of bits or chars needed
    # but to ensure consistency and so that there are same number of chars (0, 0, 1) compared to (1, 2, 0) vs (1) compared to (1, 2, 0)
    # im just gonna need a preset number of bits

    digits = []

    v = num

    for i in range(bits):
        digits.append(v // (mod**(bits - i - 1)))
        v = v % (mod**(bits - i - 1))

    # convert list to tuple
    # holy shit im saved you can add tuples :O

    return tuple(digits)


    # me when i look back at my code (written like 60 minutes ago) and realize that there's a built in method for this:
    tupl = () # empty, len 0
    for digit in digits:
        digit_tupl = (digit, ) # looks terrible but this is a singleton tuple
        tupl += digit_tupl 
    
    return tupl 
    


def tuple_to_num(t, mod): 

    digits = list(t) # wow so simple
    digits = digits[::-1]

    num = 0
    for i in range(len(digits)):
        num += digits[i]*(mod**i)
    
    return num



def get_val(value, index):
    # value is a tuple
    # index is whatever

    # for me i just return tuple index -- for other purposes might be useful
    return value[index]




def tuple_sort(arr):
    # note: uniqueness is not needed
    # but the generic sorting algorithm needs to be STABLE -- aka [a]2, [b]3, [c]4, [d]3 CANNOT be sorted to [a]2, [d]3, [b]3, c[4]

    # bubble sort is stable tho :P
    # if i implemented it correctly


    # basically you do the algorithm by
    # 1. breaking up all the values
    # sorting those by specific tuple
    # then just recovering the old values



    mod = 7
    # since inputs < 1001, 4 bits are needed (7**4 = 2401 > 1000)
    bits = 4

    new_arr = [num_to_tuple(i, mod, bits) for i in arr]

    # now just sort this tuple by least significant bits
    # to do this we define a key value thingy
    # weird stuff i know


    sorted_arr = new_arr

    for i in range(bits):
        # sort in backwards bit order
        sorted_arr = bubble_sort(sorted_arr, bits - i - 1)
    
    

    # now to convert all the values back eh?
    new_arr = [tuple_to_num(i, mod) for i in sorted_arr]

    return new_arr




######################################
#######   Unit Testing   #############
######################################


import random 
import copy


def generate_random_list(bound, length):
    random_list = [random.randint(1, bound) for a in range(length)]

    return random_list




tests_passed = 0


tests = 100 # 1000 takes too long with bubble sort being called so much
max_length = 1000
val_upper_bound = 1000


for i in range(tests):
    test_len = random.randint(1, max_length)
    random_list = generate_random_list(val_upper_bound, test_len)
    answer = copy.deepcopy(random_list)

    answer.sort() 

    response = []
    correctness = False

    # hehe try except
    try:
        response = tuple_sort(random_list)
        correctness = (response == answer)
    except:
        print()
        print('Your sort hit some sort of error with input:')
        print(random_list)
        print()
        break # leave the loop
    

    if correctness:
        tests_passed += 1
        continue

    # incorrect!!

    print()
    print('Your sort is incorrect :(')
    print(f'On test case #{i + 1} your algorithm failed.')
    print()
    print('Test Array:')
    print(random_list)
    print()
    print('Expected Answer:')
    print(answer)
    print()
    print('Your answer:')
    print(response)
    print()
    break # just leave the loop


if tests_passed == tests:
    print()
    print('Yay your sort sorts correctly!')
    print(f'{tests_passed}/{tests} tests passed successfully.')
    print()
