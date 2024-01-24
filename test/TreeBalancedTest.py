import sys
sys.path.insert(0, '../src') 
from Node import Node
from TreeBalanced import TreeBalanced

def test_add_node_and_search():
    my_tree = TreeBalanced(3)

    node1 = Node(10, "Value1")
    node2 = Node(5, "Value2")
    node3 = Node(15, "Value3")

    # Ajout des nœuds à l'arbre
    my_tree.add_node(node1)
    my_tree.add_node(node2)
    my_tree.add_node(node3)

    # Recherche de la valeur associée à une clé
    #assert (my_tree.search_value(10, my_tree.root) == "Value1")

    # Recherche de la présence d'une clé dans l'arbre
    assert (my_tree.search_bool(10, my_tree.root)) is True
    assert (my_tree.search_bool(20, my_tree.root)) is False

def test_is_Btree():
    # Créer un arbre non valide pour les tests
    invalid_tree = TreeBalanced(3)
    node20 = Node(20, "Value20")
    
    valid_tree = TreeBalanced(5)
    valid_tree.add_node(Node(30, "Value30"))
    valid_tree.add_node(node20)
    node30 = Node(30, "Value30")

    assert (valid_tree.is_Btree(node30)) is True
    
    print("Tous les tests sont passés ")

if __name__ == "__main__":
    test_add_node_and_search()
    test_is_Btree()