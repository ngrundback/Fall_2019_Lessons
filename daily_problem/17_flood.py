# You are given an array of non-negative integers that represents a two-dimensional elevation map
# where each element is unit-width wall and the integer is the height. Suppose it will rain and all
# spots between two walls get filled up.

# Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
# For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

# Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second,
# and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap
# 8 units of water.

def over_flow(arr):
  l_wall = arr[0]
  r_wall = arr[-1]
  wall = min(l_wall, r_wall)
  total = 0
  for x in range(len(arr)-1):
    if arr[x] < wall:
      total += wall - arr[x]
    else:
      wall = arr[x]
  return total



print(over_flow([3,0,1,3,0,5]))
