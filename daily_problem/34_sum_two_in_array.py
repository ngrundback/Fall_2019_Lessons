import random, pprint

'''
This problem was asked by Facebook.

Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since we can't split it up into two subsets that add up to the same sum.

'''

def find_sum(arr):
  total_sum = sum(arr)
  # if odd, this can't be done
  if total_sum % 2 != 0:
    return False
  d_sum = total_sum // 2
  # Create a matrix of size k + 1 by len(s) + 1 of booleans (all initialized to False)
  cache = [[False for _ in range(len(arr)+1)] for _ in range(d_sum + 1)]
  # Initialize the top row to True, since we can make 0 with anything (by not picking anything)
  for x in range(len(arr)+1):
    cache[0][x] = True
  # Initialize the left column to False (except for the one in the first row), since we can't make anything other than 0 with nothing
  for x in range(1, d_sum+1):
    cache[x][0] = False
  # loop over cache
  for x in range(1, (d_sum+1)):
    for y in range(1,len(arr)+1):
      last = x - arr[y-1]
      if last >= 0:
        cache[x][y] = cache[x][y-1] or cache[last][y-1]
      else:
        cache[x][y] = cache[x][y-1]
  return cache[-1][-1]


  return cache







if __name__ == '__main__':
  arr = [random.randint(0,10) for x in range(10)]
  arr2 = [15, 5, 20, 10, 35, 15, 10]
  pprint.pprint(find_sum(arr2))
