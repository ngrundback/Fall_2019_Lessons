# https://www.tutorialspoint.com/python/python_linked_lists.htm
class Node():

    def __init__(self,data):
        self.data = data
        self.pointer = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.pointer

class LinkedList():

    def __init__(self):
        self.head = None
        self.Tail = None

    def add(self,node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.pointer = node
            self.tail = node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.get_data())
            current_node = current_node.pointer

head = Node(1)
item1 = Node(2)
item2 = Node(3)
item3 = Node(4)
tail = Node(5)

list = LinkedList()
list.add(head)
list.add(item1)
list.add(item2)
list.add(item3)
list.add(tail)

list.print_list()
