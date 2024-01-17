import sys
sys.path.insert(0, '../src')  

from Node import Node

def test_node_class():
    # Test du constructeur
    node1 = Node(10, "A")
    assert node1.get_keys() == [10]
    assert node1.get_childs() == []
    assert node1.get_parent() is None
    assert node1.get_size() == 1
    # Test de __str__
    assert str(node1) == "10 A"

    # Test de search_node
    assert node1.search_node(10) is True
    assert node1.search_node(20) is False

    # Test de set_child
    node2 = Node(20, "B")
    node1.set_child(node2)
    assert node2.get_parent() == node1
    assert node1.get_childs() == [node2]
    assert node1.get_size() == 2

    # Test de la taille après ajout d'un enfant à un enfant existant
    node3 = Node(30, "C")
    node2.set_child(node3)
    assert node3.get_parent() == node2
    assert node1.get_size() == 3

    # Test de la taille après ajout de plusieurs enfants
    node4 = Node(40, "D")
    node5 = Node(50, "E")
    node1.set_child(node4)
    node1.set_child(node5)
    assert node1.get_size() == 5

    print("Tous les tests sont passés ")



if __name__ == "__main__":
    test_node_class()
    
