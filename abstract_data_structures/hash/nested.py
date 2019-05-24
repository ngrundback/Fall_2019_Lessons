graph = {
            's': {'a': 0, 'b': 1},
            'a': {'s': 3, 'b': 4, 'c':8},
            'b': {'s': 4, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 7, 't': 4},
            'd': {'b': 1, 'c': 11, 't': 5},
            't': {'c': 3, 'd': 5}
            }

# for key, value in graph.items():
#     print('For Key', key)
#     for edge_key, edge_value in graph[key].items():
#         print(edge_key,":",edge_value)
# arr = list('sabcdt')
# for i in range(len(graph)-1):
#     key = arr[i]
#     print(graph[key])

dist = {}
for x in graph:
    dist[x] = float('inf')
dist['s'] = 0
print(dist)
