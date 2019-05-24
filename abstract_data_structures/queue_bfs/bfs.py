import maze, queue

queue = queue.Queue()
maze = maze.make_maze(10,10,2)

def bfs(maze,queue):
    length = len(maze)
    start = maze[0][0]
    goal = (9,9)
    queue.enqueue(start)

    while queue.isEmpty() == False:
        node = queue.dequeue()
        node.searched = True
        for x,y in (node.x+1, node.y), (node.x-1, node.y), (node.x, node.y-1), (node.x, node.y+1):
            if (0 <= x < length and 0<= y < length) and (maze[x][y].wall == False) and (maze[x][y].searched == False):
                if (x,y) == goal:
                    return True
                else:
                    maze[x][y].parent = node
                    queue.enqueue(maze[x][y])
    return False

print(bfs(maze,queue))
