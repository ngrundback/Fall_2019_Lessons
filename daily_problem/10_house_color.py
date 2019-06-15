import random, pprint
matrix = [[random.randint(0,10) for x in range(5)]for y in range(5)]

def not_edge(node,color,color_of_edges,matrix):
    if node <= 1:
        return True

    if color != color_of_edges[color-1]:
        return True


def is_lowest(node,color, matrix,color_of_edges):
    if color in matrix[node] and color != color_of_edges[node-1]:
        return True

def get_color(node,length,matrix,color_of_edges):
    for color in range(length):
        if is_lowest(node,color,matrix,color_of_edges):
            return color

def low_cost(matrix):
    length = len(matrix)
    low = min(matrix[0])
    color_of_edges = {0:low}
    for node in range(1,length):
        color_of_edges[node] = get_color(node,length,matrix,color_of_edges)
    return color_of_edges

pprint.pprint(matrix)
print(low_cost(matrix))
