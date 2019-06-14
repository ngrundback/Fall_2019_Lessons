class Node():

    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        # if there is already data
        if self.data:
            # left side
            if data <= self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # right side
            elif data >= self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        # if there is no data
        else:
            self.data = data

    def add(self,data,pos):
        if pos == "left":
            if self.left:
                self.left.add(data,pos)
            else:
                self.left = Node(data)
        elif pos == "right":
            if self.right:
                self.right.add(data,pos)
            else:
                self.right = Node(data)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def post_order(self):
        #(left,right,root)

        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()
        print(self.data)

    def pre_order(self):
        # (root,left,right)
        nodeStack = [self]
        while nodeStack:
            node = nodeStack.pop()
            print(node.data)

            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)

    def in_order(self):
        #(left, root, right)
        if self.left:
            self.left.in_order()
        print(self.data)
        if self.right:
            self.right.in_order()

    def find(self,data):
        if data == self.data:
            return True
        elif self.data:
            if data < self.data:
                if self.left == None:
                    return False
                return self.left.find(data)
            elif data > self.data:
                if self.right == None:
                    return False
                return self.right.find(data)

    def make_array(self, arr):
        # inorder
        if self.left:
            self.left.make_array(arr)
        arr.append(self.data)
        if self.right:
            self.right.make_array(arr)
        return arr

# tree = Node(1)
# tree.left = Node(2)
# tree.right = Node(3)
# tree.left.left = Node(4)
# tree.left.right = Node(5)

tree = Node(1)
tree.add(2,'left')
tree.add(3, 'right')
tree.left.add(4,'left')
tree.left.add(5,'right')


print('post_order')
tree.post_order()
print('pre_order')
tree.pre_order()
print('in_order')
tree.in_order()
