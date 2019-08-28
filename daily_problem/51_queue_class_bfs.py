import random, pprint

class Queue():
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, data):
        return self.items.append(data)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def show(self):
        for x in self.items:
            print(x)

class Node():
    
    def __init__(self,x,y,lvl):
        self.x = x
        self.y = y
        self.lvl = lvl
        self.visited = False
        self.data = None
        self.parent = None
        self.cost = random.randint(0,10)
        if self.cost < lvl:
            self.wall = True
        else:
            self.wall = False

def make_maze(lvl,h,w):
    matrix = [[Node(x,y,lvl)for x in range(h)]for y in range(w)]
    return matrix

def isSafe(maze,x,y):
    n = len(maze)
    nc = len(maze[0])
        
    if ( 0<= x < n) and (0 <= y < nc):
        if maze[x][y].visited == False and maze[x][y].wall == False:
            return True
    return False
    

    
def bfs(maze,queue,start,goal):
    length = len(maze)
    start = maze[start[0]][start[1]]
    queue.enqueue(start)
    parent = {}
    
    while queue.isEmpty() == False:
        node = queue.dequeue()
        px,py = node.x, node.y
        node.visited = True
        for x,y in (node.x-1, node.y), (node.x+1, node.y), (node.x, node.y-1), (node.x, node.y+1):
                
            if isSafe(maze,x,y):
                parent[(x,y)] = (px,py)
                queue.enqueue(maze[x][y])
                
                if (x,y) == goal:
                    print(parent)
                    while (x,y) != (0,0):
                        print(x,y)
                        x,y = parent[(x,y)]
                    return True
    return False

if __name__ == '__main__':
    queue = Queue()
    maze = make_maze(2,10,10)
    print(bfs(maze,queue,(0,0),(1,8)))