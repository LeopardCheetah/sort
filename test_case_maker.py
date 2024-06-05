



##############################################################################################
##############################################################################################
############################                                  ################################
############################           TEST CASES             ################################
############################                                  ################################
##############################################################################################
##############################################################################################



# the test case base
# note: please do not touch anything
# and if you do, some guidelines


# if it should be manually user-inputted -- use the config section (right below this)
# if you need a fundamentally different list (aka maybe all odds or something) -
# make a new function definition with a good and descriptive name

# otherwise don't touch!


########################
####### CONFIG #########
########################

# this is the stuff you should change



NUM_OF_TESTS = 1000 
MAX_ARRAY_LENGTH = 1000 
ARR_VALUE_UPPER_BOUND = 1000


# do the values (numbers) need to be unique?
UNIQUENESS_NEEDED = False 


#############################
#############################





# generates a list of random numbers that has length length and has a max value of max_array_value
def generate_random_list(max_array_value, length):
    random_list = [random.randint(1, max_array_value) for a in range(length)]

    return random_list

# generate a list of random numbers (1 - max_array_value) with length length
def generate_random_unique_list(max_array_value, length):
    random_list = generate_random_list(max_array_value, length)
    all_nums = [i for i in range(1, max_array_value + 1)] 

    c = 0
    for ind in range(len(random_list)):
        if random_list[ind] in all_nums:
            all_nums.remove(random_list[ind])
            random_list[ind], random_list[ind - c] = 0, random_list[ind]
            continue

        random_list[ind] = 0 
        c += 1 

    random.shuffle(all_nums)

    random_list = random_list[:len(random_list) - c] 
    random_list += all_nums[:c] 

    return random_list 



import random 
import copy 

tests_passed = 0

for i in range(NUM_OF_TESTS):

    test_len = random.randint(1, MAX_ARRAY_LENGTH)

    # test-case selection channel
    if UNIQUENESS_NEEDED:
        random_list = generate_random_unique_list(ARR_VALUE_UPPER_BOUND, test_len)
    else:
        random_list = generate_random_list(ARR_VALUE_UPPER_BOUND, test_len)




    answer = copy.deepcopy(random_list)
    answer.sort() 

    response = []
    correctness = False

    try:
        response = direct_access_array_sort(random_list)
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

    
