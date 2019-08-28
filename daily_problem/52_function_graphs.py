import random, pprint

def make_maze(size, lvl):
    matrix = [[random.randint(0,10) for _ in range(size)]for _ in range(size)]
    return matrix
    

def bfs(matrix, start, goal):
    length = len(matrix)
    queue = [start]
    visited = []
    parent = {}
    
    while queue:
        node = queue.pop(0)
        px,py = node
        x,y = node
        cx,cy = node
        for cx, cy in (cx+1, cy), (cx-1, cy), (cx, cy-1), (cx, cy+1):
            if (0 <= cx < length) and (0 <= cy < length):
                if (cx,cy) not in visited and matrix[cx][cy] > 2:
                    visited.append((cx,cy))
                    queue.append((cx,cy))
                    parent[(cx,cy)] = (px,py)
                    
                    if (cx,cy) == goal:
                        current_node = (cx,cy)
                        while current_node != start:
                            print(current_node)
                            nx,ny = current_node
                            current_node = parent[(nx,ny)]
                        return True
    return False
        
if __name__ == "__main__":
    matrix = make_maze(10,10)
    # pprint.pprint(matrix)

    print(bfs(matrix,(0,0), (8,8)))
                    