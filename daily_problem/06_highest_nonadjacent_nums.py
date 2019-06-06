# given a list of intergers return the highest
# nonadjacent sum
import pprint
nums = [2,4,6,5]

def find_sum(arr):
    incl = 0
    excl = 0

    for x in arr:
        new_excl = max(incl,excl)
        incl = excl + x
        excl = new_excl
    return max(incl,excl)

print(find_sum(nums))
