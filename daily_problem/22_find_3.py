'''
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.

Do this in O(N) time and O(1) space.
'''

def find_1(arr):
  cache = {}
  for x in arr:
    if x not in cache:
      cache[x] = 0
    cache[x] += 1
  return min(cache)
arr = [6,1,3,3,1,1,3,6,6,2,2,2]
print(find_1(arr))

def find_2(arr):
  # O(nlogn)
  arr.sort()
  print(arr)
  length = len(arr) -1

  for x in range(1, length):
    if arr[x] == arr[x-1]:
      continue
    else:
      if arr[x] != arr[x+1]:
        return arr[x]
  return arr[-1] # focus on why this

print(find_2(arr))

def find_3(arr):
  pass
