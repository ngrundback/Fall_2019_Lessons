class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def serialize(root):
    if root is None:
        return '#'
    return'{} {} {}'.format(root.val,serialize(root.left), serialize(root.right))


root = Node(1)
root.left = Node(2)
root.right = Node(3)

print(serialize(root))
