from Node import Node


class TreeBalanced:

    def __init__(self, degree):
        self.degree = degree
        self.root = None


    def search(self, key, node=None):
        if not node:
            node = self.root
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node
        elif len(node.childs) > 0:
            print(f"Descending to child {i}")
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
                print(f"Violation de la propriété de tri : {node.keys[i]} >= {node.keys[i + 1]}")
                return False

        if len(node.keys) > self.degree - 1 or len(node.keys) < (self.degree // 2) - 1:
            print(f"Violation de la taille du nœud : {len(node.keys)}")
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
            print("Violation de la propriété de même profondeur")
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
        self.insert_in_node(node, key, value)


    def insert_in_node(self, node, key, value=None):
        node.keys.append(key)
        node.keys.sort()

        if len(node.keys) > self.degree - 1:
            middle_index = len(node.keys) // 2
            middle_key = node.keys[middle_index]

            new_node = Node(node.keys[middle_index + 1], value)
            new_node.childs = node.childs[middle_index + 1:]
            for child in new_node.childs:
                child.parent = new_node

            node.keys = node.keys[:middle_index]
            node.childs = node.childs[:middle_index + 1]

            if node.parent:
                self.insert_in_node(node.parent, middle_key, value)
            else:
                new_parent = Node(middle_key, value)
                new_parent.childs = [node, new_node]
                node.parent = new_node.parent = new_parent
                self.root = new_parent

    def search_for_deletion(self, key, node):
        if not node.childs:
            return node

        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            return node
        else:
            return self.search_for_deletion(key, node.childs[i])


           #a tester


    def delete(self, key, value=None):
        if not self.root:
            self.root = Node(key, value)
            return

             #a completer



    def delete_in_node(self,node,key, value=None):

    # a completer
