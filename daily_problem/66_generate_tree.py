import random

class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.right_checked = False
        self.left_checked = False

def generate():
    node = Node(0)
    if random.random() < 0.5:
        node.left = generate()
    if random.random() < 0.5:
        node.right = generate()
    return node
    
def pre_order(node):
    ans = []
    nodeStack =[node]
    
    while nodeStack:
        node = nodeStack.pop()
        if node is None:
            ans.append('.')
            continue
        else:
            ans.append(node.data)
            
        nodeStack.append(node.left)
        nodeStack.append(node.right)
    return ans
    

tree = generate()
print(tree)
print(pre_order(tree))
    
    