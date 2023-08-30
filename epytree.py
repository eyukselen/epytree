import json


class Node:
    name = None
    id = None
    parent_id = None
    data = None
    children = None

    def __init__(self, name=None, data=None, children={}, idx=None, parent_id=None):
        self.name = name
        self.data = data
        self.children = children
        self.id = idx
        self.parent_id = parent_id

    def to_dict(self):
        return {
            'name': self.name,
            'id': self.id,
            'parent_id': self.parent_id,
            'data': self.data,
            'children': self.children,
        }


class Tree:
    def __init__(self):
        self.root = Node(name='Root', idx=0)
        self.max_id = 0
        self.map = {0: self.root}

    def add_node(self, node, parent_id):
        parent = self.get_node(parent_id)
        self.max_id += 1
        node.id = self.max_id
        node.parent_id = parent_id
        parent.children[node.id] = node
        self.map[node.id] = node

    def del_node(self, idx):
        node = self.map.pop(idx)
        del node

    def get_node(self, idx):
        return self.map.get(idx, None)

    def move_node(self, src_idx, tgt_idx):
        parent_old = self.get_node(src_idx).parent_id
        node_to_move = self.get_node(parent_old).children.pop(src_idx)
        parent_new = self.get_node(tgt_idx)
        parent_new.children[node_to_move.id] = node_to_move
        node_to_move.parent_id =parent_new

    def dump_to_json(self):
        res = self.root.to_dict()
        for idx, node in self.root.children.items():
            res['children'][idx] = node.to_dict()

        return res


t = Tree()
n1 = Node()
n1.name = 'note 1'
t.add_node(n1, 0)