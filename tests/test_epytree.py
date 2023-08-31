import unittest
from epytree import Tree, Node


class TestNodeOperations(unittest.TestCase):
    def test_get_node(self):
        t = Tree()
        n1 = Node()
        n1.name = "note 1"
        n1.data = "data 1"
        t.add_node(n1, 0)
        self.assertEqual(t.get_node(1).name, "note 1")

    def test_add_node(self):
        t = Tree()
        n1 = Node()
        n1.name = "note 1"
        n1.data = "data 1"
        t.add_node(n1, 0)
        self.assertEqual(t.get_node(1).name, "note 1")

    def test_del_node(self):
        t = Tree()
        n1 = Node()
        n1.name = "note 1"
        n1.data = "data 1"
        t.add_node(n1, 0)
        t.del_node(1)
        self.assertEqual(None, t.get_node(1))

    def test_move_node(self):
        t = Tree()
        n1 = Node(name='note 1')  # id=1
        t.add_node(n1, 0)
        n11 = Node(name='note 1-1')  # id=2
        t.add_node(n11, 1)
        n2 = Node(name='note 2')  # id=3
        t.add_node(n2, 0)
        n111 = Node(name='note 1-1-1')  # id=4
        t.add_node(n111, 2)
        t.move_node(4, 3)
        self.assertEqual(t.get_node(3).children[4].parent_id,3)


if __name__ == '__main__':
    unittest.main()
