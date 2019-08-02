'''
This problem was asked by Facebook.

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

'''

def ways(n, m):
  if 1 == n or 1 == m:
    return 1
  cache = [[0 for _ in range(m)]for _ in range(n)]
  # set top row and left col to 1
  # row
  for x in range(m):
    cache[0][x] = 1
  # col
  for y in range(n):
    cache[y][0] = 1

  for x in range(1, n):
    for y in range(1, m):
      cache[x][y] = cache[x-1][y] + cache[x][y-1]
  return cache[-1][-1]


def recursion(n,m):
  if n == 1 or m == 1:
    return 1
  return recursion(n-1, m) + recursion(n, m-1)


if __name__ == '__main__':
  n = 10
  m = 10
  print(ways(n,m))
  print(recursion(n,m))
