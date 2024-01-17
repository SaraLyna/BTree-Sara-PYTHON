from Node import Node

class TreeBalanced:
    def __init__(self, degree):
        self.degree = degree
        self.root = None



#     def _insert_node(self, new_node, current_node):
#         current_node.get_keys.append(new_node.key)
#         current_node.get_childs.append(new_node.value)
#         current_node.get_size += 1

    def _insert_node(self, new_node, current_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_node(new_node, current_node.left)
        elif new_node.value > current_node.value:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_node(new_node, current_node.right)
        


    def add_node(self, node):
        if self.root is None:
            self.root = node
        else:
            self._insert_node(node, self.root)



#     def search_value(self, key, node):
#         if node is None:
#             return None
#         elif key in node.keys:
#             index = node.keys.index(key)
#             return node.childs[index]
#         else:
#             for child in node.childs:
#                 result = self._search_value(key, child)
#                 if result is not None:
#                     return result


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



#     def is_Btree(self, node):
#         if node is None:
#             return True
# 
#         if node.k > self.degree - 1 or node.k < (self.degree // 2) - 1:
#             return False
# 
#         for i in range(node.k):
#             if node.childs[i] and not self._is_Btree(node.childs[i]):
#                 return False
# 
#         if node.childs[node.k] and not self._is_Btree(node.childs[node.k]):
#             return False
# 
#         return True
#

    def is_Btree(self, node):
        if node is None:
            return True

        if len(node.keys) > self.degree - 1 or len(node.keys) < (self.degree // 2) - 1:
            return False

        for i in range(len(node.childs)):
            if node.childs[i] and not self.is_Btree(node.childs[i]):
                return False

        return True

tree = TreeBalanced(3)
 
# Adding nodes
node1 = Node(10, 'A')
node2 = Node(20, 'B')
node3 = Node(30,'C')
 
tree.add_node(node1)
tree.add_node(node2)
tree.add_node(node3)
 
# Searching for values
print(tree.search_value(10, tree.root))  # Output: 'A'
print(tree.search_value(20, tree.root))  # Output: 'B'
print(tree.search_value(30, tree.root))  # Output: 'C'
 
 # Searching for keys
print(tree.search_bool(10, tree.root))  # Output: True
print(tree.search_bool(25, tree.root))  # Output: False
 
 # Checking if it's a B-tree
print(tree.is_Btree(tree.root))  # Output: True
