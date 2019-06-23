import random
import pprint

def make_matrix(size, lvl):
    matrix = [[random.randint(0,lvl) for x in range(size)] for y in range(size)]
    return matrix


def is_safe(visited, length, rlength, cx, cy):
    if (cx,cy) not in visited and 0<= cx < length and 0<= cy < rlength:
        return True

def shortest_path(matrix, start, goal):
    length = len(matrix)
    rlength = len(matrix[0])
    queue = [start]
    cache = {start:0}
    visited = []

    while queue:
        x,y = queue.pop(0)
        visited.append((x,y))
        px,py = x,y

        for cx,cy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if is_safe(visited, length, rlength, cx, cy):
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
    size = int(input('what size maze'))
    lvl = int(input('what lvl maze'))
    startx = int(input('what is start x'))
    starty = int(input('what is start y'))
    start = (startx,starty)
    goalx = int(input('what is goal x'))
    goaly = int(input('what is goal y'))
    goal = (goalx,goaly)


    matrix = make_matrix(size,lvl)
    cache = shortest_path(matrix,start, goal)
    if cache != False:
        print(steps_count(cache, matrix, goal, start))
    else:
        print(False)
