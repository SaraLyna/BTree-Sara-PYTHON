

# TreeTest.py
import unittest
from TreeBalanced import TreeBalanced

class TestTreeBalanced(unittest.TestCase):
    def test_search(self):
        my_tree = TreeBalanced(3)
        self.assertEqual(my_tree.search_value(5), "Value2")
        self.assertTrue(my_tree.search_bool(15))
        self.assertFalse(my_tree.search_bool(20))

    def test_is_Btree(self):
        # Créer un arbre non valide pour les tests
        invalid_tree = TreeBalanced(3)
        invalid_tree.root = invalid_tree.Node(10, "Value")
        invalid_tree.root.k = 4  # k > degree - 1, rend l'arbre invalide

        valid_tree = TreeBalanced(3)
        valid_tree.insert(10, "Value")

        self.assertFalse(invalid_tree.is_Btree())
        self.assertTrue(valid_tree.is_Btree())

if __name__ == "__main__":
    unittest.main()
