import random
# so slow
def power_set(s):
  # if empty
    if not s:
      # stop and make matrix
        return [[]]
    # recursively call while subtracting one
    result = power_set(s[1:])
    # return the set of all subsets of result
    return result + [subset + [s[0]] for subset in result]

def solve(arr):
  all_sets = {}
  # sum array
  k = sum(arr)
  # if odd, can't be done
  if k % 2 != 0:
    return False
  # cycle through each powerset
  powerset = power_set(arr)
  x = 0
  for subset in powerset:
    # if powerset adds up to half, bingo
    if sum(subset) == k//2:
      # return the subset, and the arr with subset subtracted
      all_sets[x] = subset
      x += 1
  return all_sets


if __name__ == '__main__':
  arr = [1,2,3]
  arr2 = [random.randint(0,10) for x in range(10)]
  print(solve(arr2))
  arr = [1,2,3]
  meow = [ [x] + [arr[0]] for x in arr]
  print('meow',meow)
