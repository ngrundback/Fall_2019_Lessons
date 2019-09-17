# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
# Assume that each node in the tree also has a pointer to its parent.

# The lowest common ancestor between two nodes n1 and n2 is defined as 
# the lowest node in T that has both n1 and n2 as descendants 


# If root doesn’t match with any of the keys, we recur for left and right subtree. 
# The node which has one key present in its left subtree and the other key present in right subtree is the LCA. 
# If both keys lie in left subtree, then left subtree has LCA also, otherwise LCA lies in right subtree.

class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
        self.parent = None

def height(node):
    if node == None:
        return 0
    
    lheight = height(node.left)
    rheight = height(node.right)
    
    return max(lheight, rheight) + 1 

def lca(root, n1,n2):
    # base case
    if root is None:
        return None
    
    # if root is n1 or n2
    if root.data == n1 or root.data == n2:
        return root.data
    
    # search left and right subtree
    l_lca = lca(root.left,n1,n2)
    r_lca = lca(root.right,n1,n2)
    
    # if both return any value, then this is the LCA 
    # meaning, the left subtree and right subtree contain
    # one of the searched nodes each 
    if l_lca and r_lca:
        return root.data
    
    # otherwise, either the left or right subtree has
    # both nodes. So, return accordingly
    return l_lca if l_lca is not None else r_lca
    
    
    
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(12)
    root.left.left = Node(2)
    root.left.right = Node(8)
    root.right.left = Node(11)
    root.right.right = Node(20)
    print(lca(root,2,8))
    print(height(root))