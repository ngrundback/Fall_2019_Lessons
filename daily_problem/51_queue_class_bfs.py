import random, pprint

class Queue():
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, data):
        return self.items.append(data)
    
    def pop(self):
        return self.items.pop(0)
    
    def show(self):
        for x in self.items:
            print(x)

class PriorityQueue(Queue):
    
    def merge_sort(self,arr):
        if len(arr) > 1:
            mid = len(arr)//2
            r = arr[mid:]
            l = arr[:mid]
            
            self.merge_sort(r)
            self.merge_sort(l) 
            
            i,j,k = 0,0,0
            
            while i < len(r) and j < len(l):
                if r[i].weight < l[j].weight:
                    arr[k] = r[i]
                    i += 1
                else:
                    arr[k] = l[j]
                    j += 1        
                k+=1
            
            while i < len(r):
                arr[k] = r[i]
                i += 1
                k += 1
            
            while j < len(l):
                arr[k] = l[j]
                j += 1
                k += 1
            
            self.items = arr
            return self.items
    
    def add(self, data):
        if self.items == []:
            self.items.append(data)
            return self.items
        if data.weight < self.items[0].weight:
            self.items.insert(0, data)
            return self.items
        else:
            self.items.append(data)
            return self.merge_sort(self.items)
    
    def popI(self):
        return self.items.pop(0)
    
    

class Node():
    
    def __init__(self,x,y,lvl):
        self.x = x
        self.y = y
        self.lvl = lvl
        self.visited = False
        self.weight = 0
        self.data = None
        self.parent = None
        self.cost = random.randint(0,10)
        if self.cost < lvl:
            self.wall = True
        else:
            self.wall = False
    
    def show(self):
        return self.cost, self.weight, self.x,self.y

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
    
    while queue.isEmpty() == False:
        node = queue.dequeue()
        px,py = node.x, node.y
        node.visited = True
        
        for cx,cy in (node.x-1, node.y), (node.x+1, node.y), (node.x, node.y-1), (node.x, node.y+1):
                
            if isSafe(maze,cx,cy):
                maze[cx][cy].parent = maze[px][py]
                queue.enqueue(maze[cx][cy])
                
                if (cx,cy) == goal:
                    # parent = maze[cx][cy].parent
                    # ex,ey = parent.x, parent.y
                    
                    ex,ey = px,cy
                
                    while (ex,ey) != (0,0):
                        print(ex,ey)
                        parent = maze[ex][ey].parent
                        ex,ey = parent.x, parent.y
                    return True
    return False
    
def astar(maze,pqueue,str,fin):
    n = len(maze)
    str = maze[str[0]][str[1]]
    pqueue.add(str)
    paths = {}
    visited = []
    
    while pqueue.items:
        node = pqueue.pop()
        x,y = node.x, node.y
        visited.append((x,y))
        px,py = x,y
        for cx, cy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            
            if isSafe(maze, cx, cy):
                if (cx,cy) == (fin[0], fin[1]):
                    paths[(cx,cy)] = (px,py)
                    print('hey, hey, hey')
                    return paths
                
                print(cx,cy)
                dist_m = abs(fin[0] - cx) + abs(fin[1]-cy)
                maze[cx][cy].weight = dist_m
                maze[cx][cy].parent = (px,py)
                maze[cx][cy].visited = True
                paths[(cx,cy)] = (px,py)
                pqueue.add(maze[cx][cy])
                
            
        
    
    return 'Nope'
    

if __name__ == '__main__':
     pqueue = PriorityQueue()
     maze = make_maze(2,10,10)
     ans = astar(maze,pqueue,(0,0),(9,9))
     print(ans)
    # print(bfs(maze,queue,(0,0),(1,4)))
    