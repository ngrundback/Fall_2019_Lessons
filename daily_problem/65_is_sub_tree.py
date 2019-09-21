# This problem was asked by Google.
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly 
# the same structure and node values with a subtree of s. A subtree of s is 
# a tree consists of a node in s and all of this node's descendants. 
# The tree s could also be considered as a subtree of itself.
class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None
        self.child = None
        self.path = []
        
        
def height(node):
    if node == None:
        return 0
    lheight = height(node.left)
    rheight = height(node.right)
    return max(lheight,rheight)+1
    
def is_subtree(s,t):
    def is_equal(s,t):
        if s == None and t == None:
            return True
        if s == None or t == None:
            return False
        if s.data != t.data:
            return False
    
        return is_equal(s.left, t.left) and is_equal(s.right, t.right)  
    
    if s is None:
        return False
    
    if is_equal(s,t):
        return True 
    
    return is_subtree(s.left, t) or (s.right, t)  

# Another way we can solve this problem is by encoding both trees using a pre-order traversal 
# (with null markers). We return whether the string representation of subtree s is found within 
# the string representation of tree t. Since we are using a pre-order traversal, subtrees of t 
# will each be found in one contiguous substring, enabling us to search for the substring from 
# the traversal of tree s. We must mark null pointers during our traversal, as pre-order 
# traversals without these can be ambiguous in how the tree should be reconstructed. We also 
# need to wrap the start and end of the traversal string, to avoid edge cases such as 12 and 1.


def pre_order(root):
    str_tree = []
    nodeStack = [root]
    while nodeStack:
        node = nodeStack.pop()
        if node is None:
            str_tree.append('.')
            continue
        else:
            # to ensure no errors such as 12 and 1 2
            str_tree.append(str(node.data)+'_')
    
        nodeStack.append(node.right)
        nodeStack.append(node.left)
    return ''.join(str_tree)

def is_a_subtree(s,t):
    s_str = pre_order(s)
    t_str = pre_order(t)
    print(s_str)
    print(t_str)
    
    return t_str in s_str        
                    
            
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(8)
    root.right = Node(15)
    root.right.right = Node(20)
    root.right.left = Node(14)
    root.left.left = Node(4)
    root.left.right = Node(9)
    print(height(root))
    print(is_subtree(root, root.left))
    print(is_a_subtree(root,root.left))