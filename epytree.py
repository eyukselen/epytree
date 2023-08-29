import json


class Node:
    name = None
    id = None
    data = None
    children = []


class Tree:
    name = None
    root = Node()
    max_id = 0
    map = {}

    def __init__(self, name=None):
        self.name = name
        self.root.name = name
        self.root.id = 0
        self.map[self.root.id] = self.root

    def add_node(self, note, parent_id):
        parent = self.get_node(parent_id)
        self.max_id += 1
        note.id = self.max_id
        parent.children.append(note)
        self.map[note.id] = note

    def del_node(self, idx):
        node = self.map.pop(idx)
        del node

    def get_node(self, idx):
        return self.map.get(idx, None)


n = Tree()
n1 = Node()
n1.name = "note 1"
n1.data = "data 1"
n.add_node(n1, 0)

n2 = Node()
n2.name = "note 2"
n2.data = "data 2"
n.add_node(n2, 0)
print(n.get_node(1).name)
print(n.get_node(2).name)

print('before delete:', n.root.children)

n.del_node(2)

print('Not found' if n.get_node(2) is None else 'found')
print('after delete', n.root.children)
