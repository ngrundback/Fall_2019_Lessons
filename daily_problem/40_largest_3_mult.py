# fix neg problem
# sort arr highest to lowest
# multiply first three
# linear time

def mult(arr):

  only_neg = [num for num in arr if num < 0]

  if len(only_neg)%2 != 0:
    only_neg.sort()
    remove_me = only_neg[-1]
    print(remove_me)
    arr.remove(remove_me)

  arr = [abs(num) for num in arr]
  arr.sort()

  # bubble sort
  # n = len(arr)
  # for x in range(n):
  #   for y in range(0,n-x-1):
  #     if arr[y] < arr[y+1]:
  #       arr[y], arr[y+1] = arr[y+1], arr[y]

  return arr[0] * arr[1] * arr[2]







if __name__ == '__main__':
  arr = [10,4,8,9]
  arr_n = [-10,-10,5,2,-10]
  print(mult(arr_n))
