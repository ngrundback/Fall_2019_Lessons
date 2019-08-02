'''
This problem was asked by Amazon.

An sorted array of integers was rotated an unknown number of times.

Given such an array, find the index of the element in the array in faster than linear time. If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8, return 4 (the index of 8 in the array).

You can assume all the integers in the array are unique.

'''
def binary_search(arr, target):

  if len(arr) == 0 or (len(arr)==1 and arr[0]!= target):
	  return False

  mid = arr[len(arr)//2]

  if mid == target:
    return True

  elif target > mid:
    return binary_search(arr[len(arr)//2:],target)

  elif target < mid:
    return binary_search(arr[:len(arr)//2], target)

def iterative_binary_search(arr, target):
  l = 0
  r = len(arr)-1

  while l <= r:
    mid = l + (r - l)//2;
    print(mid)
    print(r,l)

    # Check if x is present at mid
    if arr[mid] == target:
      return mid

    # If x is greater, ignore left half
    elif arr[mid] < target:
      l = mid + 1

    # If x is smaller, ignore right half
    else:
      r = mid - 1

  return False




def find_me(arr):
  pass


if __name__ == '__main__':
  arr1 =  [13, 18, 25, 2, 8, 10]
  arr2 = [x+1 for x in range(100)]
  print(arr2)
  #print(find_me(arr1))
  #print(binary_search(arr2, 100))
  print(iterative_binary_search(arr2, 23))
