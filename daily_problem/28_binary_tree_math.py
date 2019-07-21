'''
This problem was asked by Microsoft.

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5)
'''

# Global Signs
PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

# Object
class Node:

  def __init__(self, data, right= None, left = None):
    self.data = data
    self.right = right
    self.left = left

# recursive function
def evaluate(root):
  if root.data == PLUS:
    return evaluate(root.left) + evaluate(root.right)
  elif root.data == MINUS:
    return evaluate(root.left) - evaluate(root.right)
  elif root.data == TIMES:
    return evaluate(root.left) * evaluate(root.right)
  elif root.data == DIVIDE:
    return evaluate(root.lefft) / evaluate(root.right)
  else:
    return root.data

if __name__ == '__main__':
  root = Node('*')
  root.right = Node('+')
  root.left = Node('+')
  root.left.right = Node(2)
  root.left.left = Node(3)
  root.right.right = Node(5)
  root.right.left = Node(4)
  print(evaluate(root))
