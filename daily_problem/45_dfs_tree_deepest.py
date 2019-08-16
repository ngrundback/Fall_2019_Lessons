# https://www.geeksforgeeks.org/find-deepest-node-binary-tree/
def height(root):
    if not root:
        return 0
    
    left = height(root.left)
    right = height(root.right)
    
    return max(left, right) + 1

def deepest_node(root, level):
    if not root:
        return
    if level == 1:
        print(root.value)
    elif( level > 1):
        deepest_node(root.left, level-1)
        deepest_node(root.right, level-1)
        
class Node():
    
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)
    root.right.left = Node(7)
    root.right.right.right = Node(10)
    level = height(root)
    deepest_node(root,level)