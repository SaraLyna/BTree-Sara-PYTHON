from Node import Node

class TreeBalanced:
    def __init__(self, degree):
        self.degree = degree
        self.root = None



    def _insert_node(self, new_node, current_node):
        current_node.keys.append(new_node.key)
        current_node.childs.append(new_node.value)
        current_node.k += 1


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
            return node.childs[index]
        else:
            for child in node.childs:
                result = self._search_value(key, child)
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

        if node.k > self.degree - 1 or node.k < (self.degree // 2) - 1:
            return False

        for i in range(node.k):
            if node.childs[i] and not self._is_Btree(node.childs[i]):
                return False

        if node.childs[node.k] and not self._is_Btree(node.childs[node.k]):
            return False

        return True
