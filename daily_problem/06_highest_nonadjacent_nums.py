# given a list of intergers return the highest
# nonadjacent sum
import pprint
nums = [2,4,6,5]

# O(2n)
def r_find_sum(arr):
    if not arr:
        return 0
    return max(r_find_sum(arr[1:]),arr[0] + r_find_sum(arr[2:]) )

print(r_find_sum(nums))

# O(n)
def memo(arr):
    # small boy case
    if len(arr) <= 2:
        return max(arr[0],arr[1])

    # create table
    cache = [0 for i in arr]
    # check if first num is -
    cache[0] = max(arr[0], 0)
    # check if arr[0] or arr[1] is bigger
    cache[1] = max(cache[0],arr[1])

    for x in range(2, len(arr)):
        # next iteration is the max between
        # current number and last nonadjacent
        # or
        # the left adjacent number
        cache[x] = max(arr[x] + cache[x-2], cache[x-1])
    return cache[-1]
print(memo(nums))

# O(n)
def find_sum(arr):
    incl = 0
    excl = 0

    for x in arr:
        new_excl = max(incl,excl)
        incl = excl + x
        excl = new_excl
    return max(incl,excl)

print(find_sum(nums))
