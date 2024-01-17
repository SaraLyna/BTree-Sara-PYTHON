import sys
sys.path.insert(0, '../src')
import unittest  
from Node import Node
from TreeBalanced import TreeBalanced

# class TestTreeBalanced(unittest.TestCase):  # Héritage de unittest.TestCase
def test_add_node_and_search():
    # Création de l'arbre avec un degré de 3
    my_tree = TreeBalanced(3)

    # Création de quelques nœuds
    node1 = Node(10, "Value1")
    node2 = Node(5, "Value2")
    node3 = Node(15, "Value3")

    # Ajout des nœuds à l'arbre
    my_tree.add_node(node1)
    my_tree.add_node(node2)
    my_tree.add_node(node3)

    # Recherche de la valeur associée à une clé
    assert (my_tree.search_value(5, my_tree.root) == "Value2")

    # Recherche de la présence d'une clé dans l'arbre
    self.assertTrue(my_tree.search_bool(15, my_tree.root))
    self.assertFalse(my_tree.search_bool(20, my_tree.root))

def test_is_Btree():
    # Créer un arbre non valide pour les tests
    invalid_tree = TreeBalanced(3)
    invalid_tree.root = Node(10, "Value")
    invalid_tree.root.k = 4  # k > degree - 1, rend l'arbre invalide

    valid_tree = TreeBalanced(3)
    valid_tree.add_node(Node(10, "Value"))

    self.assertFalse(invalid_tree.is_Btree(invalid_tree.root))
    self.assertTrue(valid_tree.is_Btree(valid_tree.root))

if __name__ == "__main__":
    test_is_Btree()