# This problem was asked by Lyft.
# 
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
# 
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.
# 
# We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.
# 
# Have a great day!

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