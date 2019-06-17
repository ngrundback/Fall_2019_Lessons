import random, pprint
#https://www.youtube.com/watch?v=HEpNiOM6lto
# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

# greedy
def greddy(matrix):
  min_node = min(matrix[0])
  cost = [min_node]
  for x in range(1, len(matrix)):
    lowest = min(matrix[x])
    while lowest == cost[x-1]:
      matrix[x].remove(lowest)
      lowest = min(matrix[x])
    cost.append(lowest)
  return cost

def dp(matrix):
  n = len(matrix[0])
  # ans array
  ans = [0] * n
  # r = idx counter, row = element
  for r,row in enumerate(matrix):
    new_row = []
    for c,col in enumerate(row):
      # compare value of col 1 to all of the values in col 2 and select the smallest
      new_row.append(min(ans[i] for i in range(n) if i != c)+ col)
    # swap updated values
    ans = new_row

  return min(new_row)


if __name__ == "__main__":
  matrix = [[random.randint(0,5)for x in range(5)]for y in range(5)]
  pprint.pprint(matrix)
  print(dp(matrix))
  print(greddy(matrix))
  #print(dp(matrix))
