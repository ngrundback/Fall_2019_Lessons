import random
arr = [random.randint(0,100) for x in range(10)]
print(arr)

def sortMe(sorted_arr, x):
  # basic sort
  while x > 0:
    if sorted_arr[x] < sorted_arr[x-1]:
      sorted_arr[x], sorted_arr[x-1] = sorted_arr[x-1], sorted_arr[x]
    x -= 1
  return sorted_arr


def rolling(arr, cache):
  median = []
  sorted_list = [arr[0]]
  for x in range(1, len(arr)):
    sorted_list.append(arr[x])
    # sort list
    if sorted_list[x] < sorted_list[x-1]:
      sorted_list = sortMe(sorted_list, x)
    length = len(sorted_list)
    # find median
    if length % 2 != 0:
      median.append(sorted_list[length//2])
      print(sorted_list)
      print(sorted_list[length//2])
    else:
      mid = length//2
      print(sorted_list)
      med = (sorted_list[mid] + sorted_list[mid-1]) // 2
      median.append(med)
      print(med)

  return median


cache = []
print(rolling(arr,cache))
