class Node():
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        
    def get_depth(self,node):
        if not node:
            return 0
        l = node.get_depth(node.left)
        r = node.get_depth(node.right)
        return max(l,r) + 1
    
    def inorder(self,node,arr):
        if node:
            self.inorder(node.left,arr)
            print(node.data)
            arr.append(node)
            self.inorder(node.right,arr)
        return arr
            
    def postOrder(self,node,arr):
        if node:
            self.postOrder(node.left,arr)
            self.postOrder(node.right,arr)
            print(node.data)
            arr.append(node)
        return arr
    
    def get_sum(self,target):
        arr = self.inorder(self,[])
        sum = 0
        for x in range(len(arr)):
            for y in range(x,len(arr)):
                if arr[x].is_safe(arr[y],target):
                    return arr[x].data, arr[y].data
        return False
    
    def is_safe(self,node,target):
        if self.data + node.data == target:
            return True
        return False
            
if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.left.left = Node(5)
    root.right.right.right = Node(10)
    # print( root.get_depth(root) )
    # print( root.inorder(root,[]))
    # print( root.postOrder(root,[]))
    print( root.get_sum(12))
    #print(in_order(root))
    #print(post_order(root,[]))