# time to redo this

# Counting Sort Algorithm implemented from here:
# https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/78a3c3444de1ff837f81e52991c24a86_MIT6_006S20_lec5.pdf
# see the whole doc (its 4 pages long so its pretty short)


# Direct Access Array Sort


def direct_access_array_sort(arr):
    # NOTE UNIQUENESS -- keys (or in this case for me, numbers) must be unique to be sorted

    # 1. iterate over and find max
    # 2. plug everything in
    # 3. return as found

    max_val = -1 # assuming positive inputs

    for i in arr:
        # max_val = max(max_val, i)
        if i > max_val:
            max_val = i 
    

    # use value 0 since in an if statement, will evaluate to 0
    # pre-req -- all values are positive

    # if an array is bounded (range = max - min < n) then you can just add a constant to every value in that array

    ls = [0]*(max_val + 1)
    # ls = [None]*(max_val + 1)

    for i in arr:
        ls[i] = i 
    
    # now do some fancy move valueing stuff

    ls_size = max_val + 1 
    num_of_vals = len(arr)


    # now just move values 
    # take closest value and move it to index

    c = 0 # bottom index
    for ind in range(max_val + 1):
        if ls[ind]: # True if >= 1 and False if 0
            ls[c] = ls[ind]
            ls[ind] = 0
            c += 1
    
    # truncate list
    final_ls = ls[:num_of_vals]

    return final_ls 









#######################################################
#######################################################
#######################################################
#######################################################





# time to make some scuffed unit tests

import random 
import copy # deep copy -- nice that this is built into python




# see commented code
def generate_random_list(bound, length):
    random_list = [random.randint(1, bound) for a in range(length)]

    if len(set(random_list)) == len(random_list):
        return random_list # yay

    # hmm we could tweak the array
    # we could recursively call ourselves 
    # sure lets cause a stack overflow today

    return generate_random_list(bound, length) 





tests_passed = 0

tests = 1000
max_length = 1000
val_upper_bound = 1000


for i in range(tests):
    # generate random arr of random length
    # or ok fine the length is a variable

    # hey wait this is a good time to use try error!!!!
    test_len = random.randint(1, max_length)



    # v1 -- i forgot that values have to be unique
    # random_list = [random.randint(1, val_upper_bound) for a in range(test_len)] 

    # v2 just define a new thing lol
    random_list = generate_random_list(val_upper_bound, test_len)



    answer = copy.deepcopy(random_list)

    answer.sort() 
    # we now have a verification answer


    response = []
    correctness = False

    # hehe try except
    try:
        response = direct_access_array_sort(random_list)
        
        # ok so til that the == operator in python will compare the value (at least in lists) even for a deepcopy so
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
    print('Yay your sort sorts correctly!')
    print(f'{tests_passed}/{tests} tests passed successfully.')
    print()

    
