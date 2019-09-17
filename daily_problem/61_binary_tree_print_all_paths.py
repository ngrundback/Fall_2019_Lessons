class Node():
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data


def all_paths(node,stack):
    if node is None:
        return
        
    stack.append(node.data)
    
    if (node.left == None and node.right == None):
        print(' '.join([str(n) for n in stack]))
        
    
    all_paths(node.left,stack)
    all_paths(node.right,stack)
    stack.pop()
    
def height(node):
    if node is None:
        return 0
    
    lheight = height(node.left)
    rheight = height(node.right)
    
    return max(lheight, rheight) + 1
    


if __name__ == "__main__": 
    stack = []   
    root = Node(10)
    root.right = Node(15)
    root.right.right = Node(20)
    root.right.left = Node(18)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(7)
    print(height(root))
    print(all_paths(root,stack))