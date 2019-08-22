import random, pprint

cache = {}
connected = {}

def bfs(start,matrix, cache, connected):
    unseen = [start]
    length_r = (len(matrix[0]))
    count = 0
    connected[start] = []
    
    while unseen:
        node = unseen.pop(0)
        x,y = node
        for cx, cy in (x+1, y), (x-1, y), (x, y+1), (x, y-1):
            if is_safe(cx,cy,matrix,cache):
                cache[(cx,cy)] = (x,y)
                unseen.append((cx,cy))
                count += 1
                connected[start].append((cx,cy))

    return connected, count
    
def is_safe(cx,cy,matrix,cache):
    length_r = len(matrix[0])
    length_c = len(matrix)
    if 0 <= cy < length_r and 0<= cx < length_c:
        if matrix[cx][cy] != 0 and (cx,cy) not in cache:
            return True        
    return False
    
def island(matrix):
    ccount = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if (x,y) not in cache:
                ans, t_count = bfs((x,y), matrix, cache, connected)
                if t_count > ccount:
                    ccount = t_count
    return ccount
                
    
    
if __name__ ==  '__main__':
    matrix = [[random.randint(0,1) for x in range(10)]for y in range(10)]
    pprint.pprint(matrix)
    print(island(matrix))
    