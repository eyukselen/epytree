import json
from json import JSONEncoder


class NodeEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class Node:
    name = None
    id = None
    parent_id = None
    data = None
    children = None

    def __init__(self, name=None, data=None, idx=None, parent_id=None):
        self.id = idx
        self.parent_id = parent_id
        self.name = name
        self.data = data
        self.children = {}


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
        node_to_move.parent_id = tgt_idx

    def to_json(self):
        return json.dumps(self.root, indent=2, cls=NodeEncoder)

    def save(self, filename):
        with open(filename, 'w') as f:
            f.write(self.to_json())

    def load(self, filename):
        self.root = Node(name='Root', idx=0)
        self.max_id = 0
        self.map = {0: self.root}
        with open(filename, 'r') as f:
            json_tree = json.loads(f.read())
        self.loads(json_tree)

    def loads(self, js, level=0):
        for k, v in js.items():
            if k == "children" and len(v) > 0:
                print(' ' * level, k)
                for kk, vv in v.items():
                    level += 1
                    self.loads(vv, level)
            else:
                print(' ' * level, k, v)


t = Tree()
t.load('tree.json')


# {'id': 0, 'parent_id': None, 'name': 'Root', 'data': None, 'children': {'1': {'id': 1, 'parent_id': 0, 'name': 'note 1', 'data': None, 'children': {'2': {'id': 2, 'parent_id': 1, 'name': 'note 1-1', 'data': None, 'children': {}}}}, '3': {'id': 3, 'parent_id': 0, 'name': 'note 2', 'data': None, 'children': {'4': {'id': 4, 'parent_id': 3, 'name': 'note 1-1-1', 'data': None, 'children': {}}}}}}
