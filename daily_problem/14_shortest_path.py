import random
import pprint

matrix = [[random.randint(0,9) for x in range(5)] for y in range(5)]

def is_safe(visited, length, cx, cy):
    if (cx,cy) not in visited and 0<= cx < length and 0<= cy <length:
        return True


def shortest_path(matrix, start):
    length = len(matrix)
    queue = [start]
    cache = {start:0}
    visited = []
    goal = (4,4)

    while queue:
        x,y = queue.pop(0)
        visited.append((x,y))
        px,py = x,y

        for cx,cy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if is_safe(visited, length, cx, cy):
                if matrix[cx][cy] > 2:
                    queue.append((cx,cy))
                    cache[(cx,cy)] = (px,py)
                    if (cx,cy) == goal:
                        return cache
    return False


def steps_count(cache, matrix,goal,start):
    currentNode = goal
    steps = 0

    while currentNode != start:
        steps+=1
        x,y = currentNode
        matrix[x][y] = '*'
        currentNode = cache[(x,y)]
    pprint.pprint(matrix)
    return steps

if __name__  == '__main__':
    cache = shortest_path(matrix,(0,0))
    if cache != False:
        print(steps_count(cache, matrix, (4,4), (0,0)))
    else:
        print(False)
