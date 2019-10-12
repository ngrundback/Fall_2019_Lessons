# This question was asked by Apple.
# 
# Given a binary tree, find a minimum path sum from root to a leaf.
# 
# For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.

import node

def in_order(node,arr):
    if node:
        in_order(node.left,arr)
        arr.append(node.data)
        print(node.data)
        in_order(node.right,arr)
        
def lcp(node):
    if node:
        l_list = lcp(node.left)
        r_list = lcp(node.right)
        min_list = min(l_list, r_list, key=lambda lst: sum(node for node in lst))
        min_list.append(node.data)
        return min_list
    return []

if __name__ == "__main__":
    # [10, 5, 1, -1] => 15
#   10
#  /  \
# 5    5
#  \     \
#    2    1
#        /
#      -1

    root = node.Node(10)
    root.right = node.Node(5)
    root.left = node.Node(5)
    root.left.right = node.Node(2)
    root.right.right = node.Node(1)
    root.right.right.right = node.Node(1)
    print(lcp(root))