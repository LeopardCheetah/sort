# first copied from direct access array sort
# now used as a hub for my testing


import random 
import copy # deep copy -- nice that this is built into python


def generate_random_list(bound, length):
    random_list = [random.randint(1, bound) for a in range(length)]

    return random_list


# see bottom for previous ver
# note: its terrible
def generate_random_unique_list(bound, length):
    random_list = generate_random_list(bound, length)

    # duplicate removal
    all_nums = [i for i in range(1, 1001)] # ok yes here im borrowing the fact that the max integer is 1000 

    # just remove the value from this all nums and if its already removed well too bad get out of the list :P

    c = 0
    for ind in range(len(random_list)):
        if random_list[ind] in all_nums:
            # remove it
            all_nums.remove(random_list[ind])
            # life is good

            # we're also gonna have to move this guy
            random_list[ind], random_list[ind - c] = 0, random_list[ind]
            continue
        
        # yikes we're gonna have to execute you buddy guy
        # use operation execute
        random_list[ind] = 0 
        c += 1 

    # our list should now look like:
    # [a1, a2, a3, .... , an, 0, 0, 0 ... , 0] where there are c 0s and length - c (= n) unique value integer things

    # now we just mix it up
    random.shuffle(all_nums) # the ones we haven't seen

    random_list = random_list[:len(random_list) - c] # remove the 0s
    random_list += all_nums[:c] # add first c vals

    return random_list # should be good to go :) 









tests_passed = 0


tests = 1000
max_length = 1000 # for uniqueness sake rn, max_length cannot be greater than val_upper_bound because otherwise pigeonhole and then infinite loop
val_upper_bound = 1000


for i in range(tests):
    # generate random arr of random length
    # or ok fine the length is a variable

    # hey wait this is a good time to use try error!!!!
    test_len = random.randint(1, max_length)



    # v1 -- i forgot that values have to be unique
    # random_list = [random.randint(1, val_upper_bound) for a in range(test_len)] 

    # v2 just define a new thing lol
    random_list = generate_random_unique_list(val_upper_bound, test_len)

    # print(random_list, len(random_list) == len(set(random_list)))
    # quit()

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
    print()
    print('Yay your sort sorts correctly!')
    print(f'{tests_passed}/{tests} tests passed successfully.')
    print()

    
