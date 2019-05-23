import random, pprint
def make_matrix(row,col,num):
 return [[random.randint(0,num) for x in range(col)]for y in range(row)]


matrix = make_matrix(4,4,2)
pprint.pprint(matrix)
visited = {}
connected = {}



def find_most_connected(matrix,start,visited,connected):
  length = len(matrix)
  x,y = start
  cx,cy = x,y
  num = matrix[x][y]
  connected[(x,y)] = []
  unseen = [(x,y)]
  px,py = x,y
  while unseen:
    x,y = unseen.pop(0)
    cx,cy = x,y
    for cx,cy in (cx+1,cy), (cx-1,cy), (cx,cy-1), (cx,cy+1):
      if (0<= cx < length and 0<= cy < length) and ( (cx,cy) not in visited):
        if matrix[cx][cy] == num:
          connected[(px,py)].append( (cx,cy) )
          visited[(cx,cy)] = True
          unseen.append((cx,cy))

  return connected


for x in range(len(matrix)):
  for y in range(len(matrix[0])):
    if (x,y) not in visited:
      ans = find_most_connected(matrix,(x,y), visited, connected)

print(ans)
