from Node import Node

class TreeBalanced:
    def __init__(self, degree):
        self.degree = degree
        self.root = None


#     def _insert_node(self, new_node, current_node):
#         if new_node.value < current_node.value:
#             if current_node.left is None:
#                 current_node.left = new_node
#             else:
#                 self._insert_node(new_node, current_node.left)
#         elif new_node.value > current_node.value:
#             if current_node.right is None:
#                 current_node.right = new_node
#             else:
#                 self._insert_node(new_node, current_node.right)
        


    def add_node(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert_node(node, self.root)



    def search_value(self, key, node):
        if node is None:
            return None
        elif key in node.keys:
            index = node.keys.index(key)
            if 0 <= index < len(node.childs):
                return node.childs[index]
            else:
                return None
        else:
            for child in node.childs:
                result = self.search_value(key, child) 
                if result is not None:
                    return result

            
            
    def search_bool(self, key, node):
        if node is None:
            return False

        if key in node.keys:
            return True
        else:
            for child in node.childs:
                if self._search_bool(key, child):
                    return True
            return False



    def is_Btree(self, node):
        if node is None:
            return True

        if len(node.keys) > self.degree - 1 or len(node.keys) < (self.degree // 2) - 1:
            return False

        for i in range(len(node.childs)):
            if node.childs[i] and not self.is_Btree(node.childs[i]):
                return False

        return True

# tree = TreeBalanced(degree=3)
# tree.root = node4 
# # Adding nodes

# node2 = Node(1, "A")
# node5 = Node(2, "B")
# node7 = Node(3, "C")
# node10 = Node(4, "D")
# node12 = Node(5, "E")
# node15 = Node(6, "F")
# node20 = Node(7, "G")

#  
# node4.childs = [node2, node6]
# node2.childs = [node1, node3]
# node6.childs = [node5, node7]
#  
# # Searching for values


# key_to_search = 5
# result_node = tree.search_value(key_to_search, tree.root)
# 
# if result_node is not None:
#     print(f"Node with key {key_to_search} found: {result_node}")
# else:
#     print(f"Node with key {key_to_search} not found.")
    
# print(tree.search_value(4, tree.root))  # Output: 'D'
# print(tree.search_value(7, tree.root))  # Output: 'G'
# print(tree.search_value(2, tree.root))  # Output: 'B'
#  
#  # Searching for keys
# print(tree.search_bool(6, tree.root))  # Output: True
# print(tree.search_bool(25, tree.root))  # Output: False
#  
#  # Checking if it's a B-tree
# is_balanced = tree.is_Btree(tree.root)
# print(f"Is the tree balanced? {is_balanced}")
