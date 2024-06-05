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


print(direct_access_array_sort([5, 2, 4, 7, 9, 13, 59]))
    
