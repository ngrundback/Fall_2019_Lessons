# This problem was asked by Lyft.
# 
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
# 
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.

def sum_of(arr,num):
  
  for x in range(len(arr)):
    if arr[x] == num:
      return arr[x]
    
    target = 0

    for y in range(x,len(arr)):
      target += arr[y]
      if target > num:
        break
      elif target == num:
        return arr[x:y+1]
        

def l_sum_of(arr,num):
    previous = dict()
    sum = 0
    previous[0] = -1
    
    for last_idx, item in enumerate(arr):
        sum += item
        # key = sum
        # value = idx
        previous[sum] = last_idx
        print(previous)
        # this will show where to start the first index
        # as the key is = to the sum
        
        first_idx = previous.get(sum-num)
        print(first_idx)
        if first_idx is not None:
            return arr[first_idx+ 1: last_idx+1]
            
print(l_sum_of([1,2,3,4,5],12))
