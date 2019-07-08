'''
This problem was asked by Facebook.

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

'''

def flight(arr, depart, arrive):
  # preprocess data
  cache = {}
  visited = [depart]
  for x,y in arr:
    cache[x] = [y]
  queue = [depart]

  # bfs
  while queue:
    city = queue.pop(0)
    print(city)
    for edge in cache[city]:
      if edge not in visited:
        queue.append(edge)
        visited.append(edge)
        if edge == arrive:
          return visited
  return False




arr = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
# ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
print(flight(arr, 'YUL', 'ORD'))
