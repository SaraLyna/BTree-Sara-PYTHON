import sys

sys.path.insert(0, "../src")

from Node import Node
from TreeBalanced import TreeBalanced


def set_nodes():
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
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()

    tree = TreeBalanced(degree=3)
    tree.root = node4
    node4.childs = [node2, node6]
    node2.childs = [node1, node3]
    node6.childs = [node5, node7]

    linearized_tree = tree.linearize()
    assert sorted(linearized_tree) == linearized_tree


def test_is_not_btree():
    node1, node2, node3, _, _, node6, _ = set_nodes()

    invalid_tree = TreeBalanced(1)
    invalid_tree.root = node6
    node6.childs = [node1, node3]
    node1.childs = [node2]

    assert invalid_tree.is_btree(invalid_tree.root) is False
    print("Test d'un arbre invalide réussi")


def test_is_btree():
    _, _, _, _, _, node6, _ = set_nodes()

    tree = TreeBalanced(degree=3)
    tree.root = node6

    assert tree.is_btree(tree.root)


def test_get_depth():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()

    tree = TreeBalanced(degree=3)
    tree.root = node4

    node4.childs = [node2, node6]
    node2.childs = [node1, node3]
    node6.childs = [node5, node7]

    assert tree.get_depth() == 2


def test_coverage_ratio():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()

    tree = TreeBalanced(degree=3)
    tree.root = node4
    node4.childs = [node2, node6]
    node2.childs = [node1, node3]
    node6.childs = [node5, node7]

    coverage_ratio = tree.coverage_ratio()

    assert coverage_ratio >= 50


def test_not_balanced():
    tree = TreeBalanced(degree=3)
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree.root = node4
    node4.childs = [node2, node6]
    node2.childs = [node1, node3]
    assert not tree.is_balanced(tree.root)


def test_is_balanced():
    tree = TreeBalanced(degree=3)
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree.root = node4
    node4.childs = [node2, node6]
    node2.childs = [node1, node3]
    node6.childs = [node5, node7]
    assert tree.is_balanced(tree.root)


def test_insert_in_root():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree = TreeBalanced(3)
    tree.insert(5)
    tree.insert(4)
    assert len(tree.root.keys) == 2
    assert tree.root.keys[0] == 4


def test_insertion_single_key():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree = TreeBalanced(3)
    node2 = Node(2, "G")
    tree.insert(5, "S")
    assert tree.search_for_insertion(5, tree.root) is not None


def test_insertion_multiple_keys():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree = TreeBalanced(4)
    tree.insert(6)
    tree.insert(5)
    assert (tree.search_for_insertion(6, tree.root)) is not None
    assert (tree.search_for_insertion(5, tree.root)) is not None
    assert (tree.search_for_insertion(3, tree.root)) is not None
    assert tree.root.keys[0] == 5
    assert tree.is_balanced(tree.root)


def test_insertion_list_of_keys():
    tree = TreeBalanced(100)
    keys = [
        2,
        4,
        5,
        6,
        8,
        10,
        12,
        14,
        16,
        18,
        20,
        22,
        24,
        26,
        28,
        30,
        32,
        34,
        36,
        7,
        9,
        11,
        13,
    ]
    for key in keys:
        tree.insert(key)
    for key in keys:
        assert (tree.search_for_insertion(key, tree.root)) is not None
    assert tree.is_balanced(tree.root)

def test_789():
    tree = TreeBalanced(3)
    tree.insert(8)
    tree.insert(9)
    tree.insert(7)
    assert tree.root.keys[0] == 8
    
    
def test_search_insert():
    tree = TreeBalanced(3)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node1.childs = [node2, node3]
    assert tree.search_for_insertion(3, node1).keys == [3]
    

def test_insert_create_new_child():
    tree = TreeBalanced(3)
    node6 = Node(6)
    node2 = Node(2)
    node4 = Node(4)
    node5 = Node(5)
    tree.insert(node2.keys[0])
    tree.insert(node4.keys[0])
    tree.insert(node5.keys[0])
    assert tree.root.keys == [4]
    tree.insert(node6.keys[0])
    assert len(tree.root.childs) == 2
    tree.insert(8)
    assert len(tree.root.childs) == 3
    
    
def test_insert_non_empty_tree():
    tree = TreeBalanced(3)

    tree.insert(5, "valeur1")
    tree.insert(3, "valeur2")
    tree.insert(7, "valeur3")
    tree.insert(4, "valeur4")

    assert tree.root.keys == [5]
    assert tree.root.childs[0].keys == [3, 4]
    assert tree.root.childs[1].keys == [7]

    
    
    
def test_insert_in_node_split():
    
    tree = TreeBalanced(3)
    
    node = Node(3)
    node.keys = [1, 2]
    
    tree.insert_in_node(node, 4)
    
    assert node.keys == [1]
    assert tree.root.keys == [2]

    assert len(tree.root.childs) == 2
    
    assert tree.root.childs[0].keys == [1]
    assert tree.root.childs[1].keys == [4]

    
    
    
    
    
    
    
    
    
    



def test_post_conditions():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree = TreeBalanced(3)
    node7 = Node(7, "G")
    tree.insert(3)
    assert (tree.search_for_insertion(3, tree.root)) is not None
    size_before = len(tree.linearize())
    tree.insert(7)
    assert len(tree.linearize()), size_before + 1
    assert tree.is_balanced(tree.root)

def test_delete_single_key():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree = TreeBalanced(10)
    keys = [10, 5, 15, 2, 7, 12, 17]
    for key in keys:
       tree.insert(key)

    assert (tree.search_for_insertion(3, tree.root)) is not None
    key_to_delete = 5
    assert (tree.delete(key_to_delete))
    assert not (tree.delete(8))
    assert tree.search(key_to_delete) is None
    assert not tree.search(5, tree.root)
    assert tree.is_balanced(tree.root)

def test_delete_multiple_keys():
    node1, node2, node3, node4, node5, node6, node7 = set_nodes()
    tree = TreeBalanced(10)
    keys = [10, 5, 15, 2, 7, 12, 17]
    for key in keys:
       tree.insert(key)
    size_before = len(tree.linearize())
    assert tree.search(5, tree.root)
    assert tree.deleteK(keys)
    assert len(tree.linearize()) == size_before -7
    assert not (tree.deleteK([5, 7]))
    assert not (tree.deleteK([8, 9]))
    for key in keys:
        assert not tree.search(key)

    assert tree.is_balanced(tree.root)
    
    
    
  
    
    
    
    
    
    
    
    

