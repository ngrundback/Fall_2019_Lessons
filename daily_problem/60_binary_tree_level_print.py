# This is your coding interview problem for today.
# 
# This problem was asked by Microsoft.
# 
# Print the nodes in a binary tree level-wise. For example, 
# the following should print 1, 2, 3, 4, 5.
# 
#   1
#  / \
# 2   3
#    / \
#   4   5

class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

def printLevel(root):
    height = get_height(root)
    for node in range(1, height+1):
        print_by_level(root,node)
        
def print_by_level(root, level):
        if root is None:
            return
        if level == 1:
            print(root.data)
        elif level > 1:
            print_by_level(root.left, level-1)
            print_by_level(root.right, level-1)

def get_height(node):
    
    if node is None:
        return 0
    
    lheight = get_height(node.left)
    rheight = get_height(node.right)
    return max(lheight, rheight) + 1
    
from queue import Queue

def print_that_level(root):
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        node = queue.get()
        if node.left:
            queue.put(node.left)
        if node.right:
            queue.put(node.right)
        print(node.data) 
        
def that_height(root):
    if root is None:
        return 0 # without 0 line 64 gives error of nonetype can't compare with int
    
    lheight = that_height(root.left)
    rheight = that_height(root.right)
    
    return max(lheight, rheight) + 1
    

root = Node(15)
root.left = Node(10)
root.right = Node(20)
root.right.right = Node(25)
print(printLevel(root))
print(print_that_level(root))
print(that_height(root))