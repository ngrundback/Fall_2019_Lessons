def bellmanFord(graph, start):
  dist = {}
  for vertex in graph:
    dist[vertex] = float('Inf')
  dist[start] = 0
  unseenNodes = graph

  for i in range(len(graph)-1):
    for u in unseenNodes:
      for v,w in graph[u].items():
        if dist[u] != float('Inf') and dist[u] + w < dist[v]:
          dist[v] = w + dist[u]


  for u in unseenNodes:
    for v,w in graph[u].items():
      if dist[u] != float('Inf') and dist[u] + w < dist[v]:
        print('you got a negative cycle')

  return dist


graph = {

            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }

print(bellmanFord(graph,'a'))
