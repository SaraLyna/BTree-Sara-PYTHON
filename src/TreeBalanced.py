from graphviz import Digraph

from Node import Node


class TreeBalanced:

    def __init__(self, degree):
        self.degree = degree
        self.root = None


    def get_root(self):
        return self.root


    def search(self, key, node=None):
        if not node:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node
        elif len(node.childs) > 0:
            #print(f"Descending to child {i}")
            return self.search(key, node.childs[i])
        else:
            print("Key not found")
            return None

    def linearize(self, node=None):
        if not node:
            node = self.root

        res = []
        i = 0

        while i < len(node.keys):
            if len(node.childs) > i:
                res.extend(self.linearize(node.childs[i]))

            res.append(node.keys[i])
            i += 1

        if len(node.childs) > i:
            res.extend(self.linearize(node.childs[i]))

        return res


    def is_btree(self, node):
        if node is None:
            return True

        for i in range(len(node.keys) - 1):
            if node.keys[i] >= node.keys[i + 1]:
                #print(f"Violation de la propriété de tri : {node.keys[i]} >= {node.keys[i + 1]}")
                return False

        if len(node.keys) > self.degree - 1 or len(node.keys) < (self.degree // 2) - 1:
            #print(f"Violation de la taille du nœud : {len(node.keys)}")
            return False

        for i in range(len(node.childs)):
            if node.childs[i] and not self.is_btree(node.childs[i]):
                return False



        return True



    def is_balanced(self, node):
        depth = self.get_depth(node)
        if depth == -1:
            return False

        return True



    def get_depth(self, node=None):
        if not node:
            node = self.root

        if not node.childs:
            return 0

        child_depths = [self.get_depth(child) for child in node.childs]

        if len(set(child_depths)) != 1:
            #print("Violation de la propriété de même profondeur")
            return -1

        return 1 + child_depths[0]


    def coverage_ratio(self):
        def count_keys(node):
            if not node:
                return 0
            count = len(node.keys)
            for child in node.childs:
                count += count_keys(child)
            return count

        total_nodes = len(self.linearize()) - 1
        keys_count = count_keys(self.root)
        coverage_ratio = (keys_count / total_nodes) * 100
        return coverage_ratio



    def search_for_insertion(self, key, node):
        if not node.childs:
            return node

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        return self.search_for_insertion(key, node.childs[i])

    def insert(self, key, value=None):
        if not self.root:
            self.root = Node(key, value)
            return

        node = self.search_for_insertion(key, self.root)
        if node.parent is None:
            self.root = node
        self.insert_in_node(node, key, value)




    def insert_in_node(self, node, key, value=None):
        node.keys.append(key)
        node.keys.sort()

        if len(node.keys) > self.degree - 1:
            middle_index = len(node.keys) // 2
            middle_key = node.keys[middle_index]

            new_node = Node(node.keys[middle_index + 1])
            new_node.childs = node.childs[middle_index + 1:]
            for child in new_node.childs:
                child.parent = new_node

            node.keys = node.keys[:middle_index]
            node.childs = node.childs[:middle_index + 1]

            if node.parent:
                node.parent.add_child(new_node)
                self.insert_in_node(node.parent, middle_key, value)
            else:
                new_parent = Node(middle_key)
                self.root = new_parent
                self.root.add_child(node)
                self.root.add_child(new_node)






    def deleteK(self, keys_or_key):
        if isinstance(keys_or_key, list):
            success = True
            for key in keys_or_key:
                if not self.delete(key):
                    success = False
            return success
        else:
            return self.delete(keys_or_key)


    def delete(self, key):
        if not self.root:
            return False

        return self._delete(self.root, key)




    # def _delete(self, node, key):
    #     if key in node.keys:
    #         node.keys.remove(key)
    #         return True
    #
    #     for child in node.childs:
    #         if self._delete(child, key):
    #             if len(child.keys) < (self.degree - 1) // 2:
    #                 self._fill(node, node.childs.index(child))
    #             return True
    #
    #     return False

    def _fill(self, parent, index):
        left_sibling = parent.childs[index - 1] if index > 0 else None
        right_sibling = parent.childs[index + 1] if index < len(parent.childs) - 1 else None

        if left_sibling and len(left_sibling.keys) > (self.degree - 1) // 2:
            self._rotate_right(parent, index)
        elif right_sibling and len(right_sibling.keys) > (self.degree - 1) // 2:
            self._rotate_left(parent, index)
        elif left_sibling:
            self._merge(parent, index - 1)
        elif right_sibling:
            self._merge(parent, index)

    def _rotate_right(self, parent, index):
        child = parent.childs[index]
        left_sibling = parent.childs[index - 1]

        child.keys.insert(0, parent.keys[index - 1])
        parent.keys[index - 1] = left_sibling.keys.pop()

        if child.childs:
            child.childs.insert(0, left_sibling.childs.pop())

    def _rotate_left(self, parent, index):
        child = parent.childs[index]
        right_sibling = parent.childs[index + 1]

        child.keys.append(parent.keys[index])
        parent.keys[index] = right_sibling.keys.pop(0)

        if child.childs:
            child.childs.append(right_sibling.childs.pop(0))

    def _merge(self, parent, index):
        child = parent.childs[index]
        right_sibling = parent.childs[index + 1]

        child.keys.append(parent.keys.pop(index))
        child.keys.extend(right_sibling.keys)
        child.childs.extend(right_sibling.childs)

        parent.childs.pop(index + 1)


    def _delete(self, node, key):
        for i in range(len(node.keys)):
            if key == node.keys[i]:
                if not node.childs:
                    node.keys.pop(i)
                else:
                    successor = self._get_successor(node, i)
                    node.keys[i] = successor
                    self._delete(node.childs[i + 1], successor)
                return True

            elif key < node.keys[i]:
                if node.childs:
                    deleted = self._delete(node.childs[i], key)
                    if deleted:
                        if len(node.childs[i].keys) < (self.degree - 1) // 2:
                            self._fill(node, i)
                        return True
                else:
                    return False

        if node.childs:
            deleted = self._delete(node.childs[-1], key)
            if deleted:
                if len(node.childs[-1].keys) < (self.degree - 1) // 2:
                    self._fill(node, len(node.childs) - 1)
                return True
        return False

    def _get_successor(self, node, index):
        successor_node = node.childs[index + 1]
        while successor_node.childs:
            successor_node = successor_node.childs[0]
        return successor_node.keys[0]



    def visualize_tree(self):
        graph = Digraph()
        self._add_nodes_and_edges(graph, self.root)
        return graph

    def _add_nodes_and_edges(self, graph, node):
        if node:
            graph.node(str(node), label=str(node.keys))
            for child in node.childs:
                if child:
                    self._add_nodes_and_edges(graph, child)
                    graph.edge(str(node), str(child))
