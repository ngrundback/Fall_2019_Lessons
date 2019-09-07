import random, pprint

# Global Signs
PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

def power_set(arr):
    if not arr:
        return [[]]
    result = power_set(arr[1:])
    return result + [subset + [arr[0]] for subset in result]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        r = arr[mid:]
        l = arr[:mid]

        merge_sort(r)
        merge_sort(l)

        i,j,k = 0,0,0

        while i < len(r) and j < len(l):
            if r[i] > l[j]:
                arr[k] = r[i]
                i += 1
            else:
                arr[k] = l[j]
                j += 1

            k += 1

        while i < len(r):
            arr[k] = r[i]
            i += 1
            k += 1

        while j < len(l):
            arr[k] = l[j]
            j += 1
            k += 1
        return arr



class Node():

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def evaluate(node):
    if node.data == PLUS:
        return evaluate(node.left) + evaluate(node.right)
    elif node.data == MINUS:
        return evaluate(node.left) - evaluate(node.right)
    elif node.data == TIMES:
        return evaluate(node.left) * evaluate(node.right)
    elif node.data == DIVIDE:
        return evaluate(node.left)//evaluate(node.right)
    else:
        return node.data

def bfs(matrix, start, end):
    length = len(matrix)
    queue = [start]
    visited = [start]
    parent = {start:0}
    while queue:
        current_node = queue.pop()
        x,y = current_node

        for cx,cy in ((x+1, y), (x-1,y), (x, y-1), (x, y+1)):
            if 0<= cx < length and 0<= cy < length and (cx,cy) not in visited:
                queue.append((cx,cy))
                visited.append((cx,cy))
                parent[(cx,cy)] = current_node
                if (cx,cy) == end:
                    return parent
    return False

def stairs(n, steps):
    step_l = len(steps)
    cache = {}

    for x in range(step_l):
        cache[x] = steps[x]

    for x in range(step_l,n):
        cache[x] = cache[x-1] + cache[x-2] + cache[x-3]
    return cache[n-1]

def steps(n):
    a = 1
    b = 2
    c = 3
    for _ in range(n-1):
        a,b, c = b, c, a+b+c
    return a



if __name__ == '__main__':
    print(stairs(25,[1,2,3]))
    print(steps(25))
  # matrix = [[random.randint(0,10) for x in range(10)]for y in range(10)]
  # print(bfs(matrix,(0,0),(9,9)))
  # print(power_set([1,2,3]))
  # print(merge_sort([20,1,3,5,100]))
  # root = Node('*')
  # root.right = Node('+')
  # root.left = Node('+')
  # root.left.right = Node(2)
  # root.left.left = Node(3)
  # root.right.right = Node(5)
  # root.right.left = Node(4)
  # print(evaluate(root))
