import unittest
from tree import Tree
from node import Node


class TestFind(unittest.TestCase):
    """Unit tests pentru metoda _find din clasa Tree."""

    def setUp(self):
        """Construiește un arbore folosit de toate testele.

        Structura după inserări (3, 4, 0, 8, 2):
                3
               / \
              0   4
               \   \
                2   8
        """
        self.tree = Tree()
        for value in [3, 4, 0, 8, 2]:
            self.tree.add(value)

    def test_find_root(self):
        """_find trebuie să returneze nodul rădăcină când e căutat."""
        result = self.tree._find(3, self.tree.root)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, Node)
        self.assertEqual(result.data, 3)

    def test_find_left_child(self):
        """_find trebuie să găsească un nod în subarborele stâng."""
        result = self.tree._find(0, self.tree.root)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 0)

    def test_find_right_child(self):
        """_find trebuie să găsească un nod în subarborele drept."""
        result = self.tree._find(4, self.tree.root)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 4)

    def test_find_deep_node(self):
        """_find trebuie să găsească un nod aflat la adâncime mai mare."""
        result = self.tree._find(8, self.tree.root)
        self.assertIsNotNone(result)
        self.assertEqual(result.data, 8)

    def test_find_nonexistent_value(self):
        """_find trebuie să returneze None pentru o valoare care nu există."""
        result = self.tree._find(99, self.tree.root)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()