# This question was asked by Google.
# 
# Given an N by M matrix consisting only of 1's and 0's, 
# find the largest rectangle containing only 1's and return its area.
# 
# For example, given the following matrix:
# 
# [[1, 0, 0, 0],
#  [1, 0, 1, 1],
#  [1, 0, 1, 1],
#  [0, 1, 0, 0]]
# Return 4.

def area(matrix,target):
    arr, num = largest_area(matrix,target)
    return len(arr)
    # row = {}
    # col = {}
    # tr = 0
    # tc = 0
    # 
    # for x in range(len(arr)):
    #     r,c = arr[x]
    #     if r not in row and c not in col:
    #         tr += 1
    # return (tr)
        
        
    

def largest_area(matrix,target):
    explored = []
    all_areas = {}
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] not in explored:
                nums, ans = bfs((x,y), matrix, explored, target)
                all_areas[ans] = nums
    tots = max(all_areas)
    return all_areas[tots], ans
    
def bfs(start, matrix, explored, target):
    n = len(matrix)
    nr = len(matrix[0])
    queue = [start]
    ans = []
    count = 0

    while queue:
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            x,y = node
            if matrix[x][y] == target:
                queue.append(node)
                count += 1
                x,y = node
                ans.append((x,y))
                for cx,cy in (x+1, y), (x-1, y), (x, y-1), (x, y+1):
                    if 0 <= cx < n and 0 <= cy < nr:
                        queue.append((cx,cy))
    return ans, count


if __name__ == "__main__":
    matrix = [[1, 0, 0, 0],[1, 0, 1, 1],[1, 0, 1, 1],[0, 1, 0, 0]]    
    print(area(matrix, 0))          
                
    
    