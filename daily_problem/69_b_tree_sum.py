 # This problem was asked by Google.
# 
# Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
# 
# For example, given the following tree and K of 20
# 
#     10
#    /   \
#  5      15
#        /  \
#      11    15
# Return the nodes 5 and 15.


class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def two_nodes(root,target):
    arr = post_order(root,[])
    sum = 0
    
    for x in range(len(arr)):
        for y in range(x,len(arr)):
            if is_safe(arr[x],arr[y],target):
                return arr[x],arr[y]
                    
def is_safe(current_num, add_num, target):
    if current_num + add_num == target:
        return True
    return False
    
def get_depth(node):
    if not node:
        return 0
    l = get_depth(node.left)
    r = get_depth(node.right)
    return max(l,r) + 1
    
def in_order(node):
    if node:
        in_order(node.left)
        print(node.data)
        in_order(node.right)
        
def post_order(node,arr):
    if node:
        post_order(node.left,arr)
        post_order(node.right,arr)
        arr.append(node.data)
    return arr
    

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(5)
    root.right.right.right = Node(10)
    #print(get_depth(root))
    #print(in_order(root))
    #print(post_order(root,[]))
    print(two_nodes(root,15))