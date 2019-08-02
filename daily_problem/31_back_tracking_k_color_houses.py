'''
This problem was asked by Google.

Given an undirected graph represented as an adjacency matrix and an integer k, write a function to determine whether each vertex in the graph can be colored such that no two adjacent vertices share the same color using at most k colors.

We will be sending the solution tomorrow, along with tomorrow's question. As always, feel free to shoot us an email if there's anything we can help with.

Have a great day!
'''
houses = {
  0: [1,2],
  1: [0,2,3,4],
  2: [1],
  3: [1, 2],
  4: [0]

}
def valid(graph, colors):

    last_vertex = len(colors) - 1
    last_color = colors[-1]

    colored_neighbors = [x for x in graph[last_vertex] if x < last_vertex]

    for neighbor in colored_neighbors:
        if colors[neighbor] == last_color:
            return False
    return True

def colorable(graph, k, colors=[]):

    if len(colors) == len(graph):
        return True

    for i in range(k):
        colors.append(i)
        if valid(graph, colors):
            if colorable(graph, k, colors):
              return True, colors
        colors.pop()

    return False





if __name__ == '__main__':
  print(colorable(houses, 4))
