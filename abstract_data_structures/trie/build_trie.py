class Node():
    def __init__(self,data):
        self.data = data
        self.count = 0
        self.children = []
        self.word_finished = False


def add(root, word):
    node = root
    for char in word:
        found_in_child = False
        for child in node.children:
            if child.char == char:
                child.count += 1
                node = child
                found_in_child = True
                break

            new_node = Node(char)
            node.children.append(new_node)
            node = new_node
    node.word_finished = True

root = Node('me')
trie = add(root,'ow')
print(root.children)
