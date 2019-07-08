'''
This problem was asked by Google.

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''

def is_safe(current_num, add_num, target):
  if current_num + add_num <= target:
    return True
  return False

def solve(arr,target,current_num):
  if current_num == target:
    return True

  for x in range(len(arr)):

    if is_safe(arr[x], current_num, target):
      current_num += arr[x]

      if solve(arr[x+1:], target, current_num):
        #print(arr[x])
        ans.append(arr[x])
        return True

      current_num  -= arr[x]
  return False




if __name__ == '__main__':
  global ans
  ans = []
  arr = [12, 1, 61, 5, 9, 2]
#arr = [25,0,2,7,8,25,50]
  print(solve(arr, 24, 0))
  print(ans)
