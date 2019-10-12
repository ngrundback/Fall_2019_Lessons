class Node():
    
    def __init__(self,data):
        self.right = None
        self.left = None
        self.data = data
        self.explored = False
        self.parent = None