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
