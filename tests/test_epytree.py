from epytree import Tree, Node


def test_add_node():
    t = Tree()
    n1 = Node()
    n1.name = "note 1"
    n1.data = "data 1"
    t.add_node(n1, 0)
    assert t.get_node(1).name == "note 1"

# def test_del_node():
#     assert False


def test_get_node():
    t = Tree()
    n1 = Node()
    n1.name = "note 1"
    n1.data = "data 1"
    t.add_node(n1, 0)
    assert t.get_node(1).name == "note 1"
