# I'm not sure how to code this algorithm, so i'll first code it then do an analysis

# ok guys i looked at some mit notes this should work

import random

arr = [random.randint(1, 9) for i in range(20)] # 20 random numbers


# so all keys here are between 0-10
# let's do that!

max_key = max(arr)

keylist = [[] for i in range(max_key + 1)] # gotta generate 0 (not really) => max_key which has 1+max elements

# add to this mega chain list thing
for item in arr:
    keylist[item].append(item)

# ok now build it!
# since there are only O(n) items => searching should only take O(n) time

sorted_arr = []

for ls in keylist:
    sorted_arr += ls

print(sorted_arr)


# O(n + k) where k is the max key in the list
