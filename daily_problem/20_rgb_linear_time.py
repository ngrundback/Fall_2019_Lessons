# This problem was asked by Google. https://en.wikipedia.org/wiki/Dutch_national_flag_problem
# Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, # the Gs come second, and the Bs come last. You can only swap elements of the array.
# Do this in linear time and in-place.

# For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

def partition_2(arr):
  low, high = 0, len(arr) - 1
  while low <= high:
    if arr[low] == 'R':
      low += 1
    else:
      arr[low], arr[high] = arr[high], arr[low]
      high -= 1
  return arr

print(partition_2(['R','G','G','R','G','R','G']))

# We'll initialize low and mid both to 0, and high to len(array) - 1 so that our unknown section is the whole array, as before. To maintain this invariant, we should do the following:

# Look at array[mid]:
# If it's R, then swap array[low] with array[mid] and increment low and mid
# If it's G, then just increment mid; it's where it should be
# If it's B, then swap array[mid] with array[high] and decrement high

def partition(arr):
  low,mid,high, = 0, 0, len(arr)-1

  while mid <= high:
    if arr[mid] == 'R':
      arr[low], arr[mid] = arr[mid], arr[low]
      low += 1
      mid += 1
    elif arr[mid] == 'G':
      mid += 1
    else:
      arr[mid], arr[high] = arr[high], arr[mid]
      high -= 1
  return arr

print(partition(['G', 'B', 'R', 'R', 'B', 'R', 'G']))
