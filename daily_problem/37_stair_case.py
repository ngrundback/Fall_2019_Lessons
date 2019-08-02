def stair_count(n):
  if n <= 1:
    return 1
  return stair_count(n-1) + stair_count(n-2)

def iterative(n):
  a = 1
  b = 2
  for _ in range(n-1):
    a,b = b, a+b
  return a


if __name__ == '__main__':
  n = 10
  print(stair_count(n))
  print(iterative(n))
