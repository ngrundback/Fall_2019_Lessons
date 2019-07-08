import random, pprint
matrix = [[random.randint(-2,10) for x in range(5)]for y in range(5)]
pprint.pprint(matrix)

def relax(row,col,matrix,min_dist, n):
    for cx,cy in (row+1, col), (row-1, col), (row, col-1), (row, col+1):
        if 0<= cx < n and 0 <= cy < n:
            if min_dist[cx][cy] > matrix[cx][cy] + min_dist[row][col]:
                min_dist[cx][cy] = matrix[cx][cy] + min_dist[row][col]
    return min_dist

def neg_cycle_check(row, col, matrix, min_dist, n):
    for cx,cy in (row+1, col), (row-1, col), (row, col-1), (row, col+1):
        if 0<= cx < n and 0 <= cy < n:
            if min_dist[cx][cy] > matrix[cx][cy] + min_dist[row][col]:
                return True

def currency_rates(matrix):
    n = len(matrix)
    min_dist = [[float('inf') for x in range(n)] for y in range(n)]
    min_dist[0][0] = 0

    # relax edges
    for x in range(n-1):
        for row in range(n):
            for col in range(n):
                min_dist = relax(row,col,matrix, min_dist, n)
    print('after relaxtion, here are the costs\n')
    pprint.pprint(min_dist)


    # if you can further relax edges, than there is a negative cycle
    for v in range(n):
        for w in range(n):
            if neg_cycle_check(v, w, matrix, min_dist, n):
                return True

    return False


pprint.pprint(currency_rates(matrix))
