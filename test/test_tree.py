import sys

sys.path.insert(0, '../src') 
from Node import Node
from TreeBalanced import TreeBalanced


def set_nodes():
    # Adding nodes
    node1 = Node(1, "A")
    node2 = Node(2, "B")
    node3 = Node(3, "C")
    node4 = Node(4, "D")
    node5 = Node(5, "E")
    node6 = Node(6, "F")
    node7 = Node(7, "G")

    
    return node1, node2, node3, node4, node5, node6, node7

def test_search():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()

    tree = TreeBalanced(degree=3)
    tree.root = node4

    node4.childs = [node2, node6]
    node2.childs = [node1, node3]
    node6.childs = [node5, node7]

    key_to_search = 5
    result_node = tree.search(key_to_search, tree.root)


    assert result_node is not None
    assert key_to_search in result_node.keys
        
    assert tree.search(4, tree.root)
    assert not tree.search(8, tree.root)
    assert tree.search(2, tree.root)

def test_linearize():
    _, _, _, _, _, _, node7 = set_nodes()

    tree = TreeBalanced(degree=2)
    tree.root = node7

    assert tree.linearize() == [7]



def test_is_not_btree():
    node1, node2, node3, _, _, node6, _ = set_nodes()
    
    invalid_tree = TreeBalanced(1)
    invalid_tree.root = node6
    node6.childs = [node1, node3]
    node1.childs =[node2]
    

    assert invalid_tree.is_btree(invalid_tree.root) is False
    print("Test d'un arbre invalide réussi")
    
    
    
def test_is_btree():

    _, _, _, _, _, node6, _ = set_nodes()

    tree = TreeBalanced(degree=3)
    tree.root = node6

    assert tree.is_btree(tree.root)
    

# if __name__ == "__main__":
#     set_nodes()
#     test_search()
#     test_linearize()
#     test_is_btree()
    