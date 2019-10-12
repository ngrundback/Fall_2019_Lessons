class Node():
    
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data


def tree_sum(root,target):
    r_arr = in_order(root, [])
    cache = {}
    for x in r_arr:
        if target - x in cache:
            return(x, cache[target-x])
        cache[x] = x
    return False
            
    

def in_order(node, arr):
    if node:
        in_order(node.left,arr)
        arr.append(node.data)
        in_order(node.right,arr)
    return arr


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(5)
    root.right.right.right = Node(10)
    print(in_order(root,[]))
    print(tree_sum(root,9))
    
    