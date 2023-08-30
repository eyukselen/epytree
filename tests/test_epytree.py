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
        n1 = Node()
        n1.name = "note 1"
        t.add_node(n1, 0)
        n2 = Node()
        n1.name = "note 2"
        t.add_node(n2, 0)
        n11 = Node()
        n11.name = 'note 1-1'
        t.add_node(n11, 1)
        t.move_node(3, 2)
        n2_check = t.get_node(2)
        print(n2.children)


if __name__ == '__main__':
    unittest.main()