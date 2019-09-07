# This problem was asked by Coursera.
# 
# Given a 2D board of characters and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
# 
# For example, given the following board:
# 
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
def is_safe(x,y,matrix,visited,word,current_letter):
    n = len(matrix)
    if 0 <= x < n and 0 <= y < n:
        if (x,y) not in visited:
            if matrix[cx][cy] == word[current_letter]:
                return True
    return False
    

def bfs(matrix,start,word):
    n = len(matrix)
    visited = []
    parent = {}
    queue = [start]
    current_letter = 0
    while queue:
        node = queue.pop()
        x,y = node
        px,py = x,y
        for cx,cy in (x-1,y), (x+1,y), (x, y-1), (x, y+1), (x-1,y-1), (x+1, y+1):
            if is_safe(cx,cy,matrix,visited,word,current_letter):
                visited.append((cx,cy))
                parent[(cx,cy)] = px,py
                queue.append((cx,cy))
                if current_letter == len(word):
                    return True
                current_letter += 1
    return False
    
def find_word(matrix,word):
    n = len(matrix)
    for x in range(n):
        for y in range(len(matrix[x])):
            ans = bfs(matrix,(x,y), word)
            if ans == True:
                return True 
    return False

matrix = [['']]
print(find_word(matrix,['h','e','y']))
        
                
                    
                
            
            #add