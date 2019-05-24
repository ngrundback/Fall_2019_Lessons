graph1 = {
    'A' : ['B','E'],
    'B': ['C'],
    'C': ['D'],
    'D': [],
    'E': ['D']

}
def dfs(graph, node, visited,ordered):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:

          dfs(graph,n, visited,ordered)
        ordered.append(node)
    return ordered

def topo(graph1, node):
    ordered=[]
    visited=[]
    dfs(graph1, node, visited,ordered)
    ordered.reverse()
    return ordered

print(topo(graph1, 'A'))
