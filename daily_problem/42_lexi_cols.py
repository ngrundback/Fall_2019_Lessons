
def lexi_col(matrix):
    # locate cols to remove
    cols_to_remove = []
    n = len(matrix[0])
    p = 0
    while p < n:
        for x in range(n-1):
            if matrix[p][x] > matrix[p][x + 1]:
                cols_to_remove.append(p)
        p += 1 
    # ans = []
    # 
    # for x in range(len(matrix)):
    #     if x not in cols_to_remove:
    #         ans.append(matrix[x])
    # 
    # return ans
    # 


if __name__ == '__main__':
    matrix = [['a','b','c'], ['e','a','g'], ['h','a','j']]
    print(lexi_col(matrix))
