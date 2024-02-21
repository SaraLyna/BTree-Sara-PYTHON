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
        
    
    
    def delete(self, key):
        if not self.root:
            return

        self._delete(self.root, key)
        
    
    def _delete(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1

        if i < len(node.keys) and key == node.keys[i]:
            if node.childs[i].is_leaf():
                del node.keys[i]
            else:
                if len(node.childs[i].keys) >= self.degree:
                    predecessor_key = self._get_predecessor(node, i)
                    node.keys[i] = predecessor_key
                    self._delete(node.childs[i], predecessor_key)
                elif len(node.childs[i + 1].keys) >= self.degree:
                    successor_key = self._get_successor(node, i)
                    node.keys[i] = successor_key
                    self._delete(node.childs[i + 1], successor_key)
                else:
                    self._merge(node, i)
                    self._delete(node.childs[i], key)
        else:
            if node.childs[i].is_leaf():
                return
            if len(node.childs[i].keys) < self.degree:
                self._fill(node, i)
            if i == len(node.keys) or key < node.keys[i]:
                self._delete(node.childs[i], key)
            else:
                self._delete(node.childs[i + 1], key)
    
    
    
    def _get_predecessor(self, node, i):
        current = node.childs[i]
        while not current.is_leaf():
            current = current.childs[-1]
        return current.keys[-1]
    
    
    def _get_successor(self, node, i):
        current = node.childs[i + 1]
        while not current.is_leaf():
            current = current.childs[0]
        return current.keys[0]
        
    
    def _merge(self, node, i):
        child = node.childs[i]
        sibling = node.childs[i + 1]
        child.keys.append(node.keys[i])
        child.keys.extend(sibling.keys)
        if not child.is_leaf():
            child.childs.extend(sibling.childs)
        del node.keys[i]
        del node.childs[i + 1]
        del sibling
       
       
        
    def _fill(self, node, i):
        if i != 0 and len(node.childs[i - 1].keys) >= self.degree:
            self._borrow_from_prev(node, i)
        elif i != len(node.keys) and len(node.childs[i + 1].keys) >= self.degree:
            self._borrow_from_next(node, i)
        else:
            if i != len(node.keys):
                self._merge(node, i)
            else:
                self._merge(node, i - 1)
                
                
    
    def _borrow_from_prev(self, node, i):
            child = node.childs[i]
            sibling = node.childs[i - 1]
            child.keys.insert(0, node.keys[i - 1])
            if not child.is_leaf():
                child.childs.insert(0, sibling.childs.pop())
            node.keys[i - 1] = sibling.keys.pop()
        



    def _borrow_from_next(self, node, i):
        child = node.childs[i]
        sibling = node.childs[i + 1]
        child.keys.append(node.keys[i])
        if not child.is_leaf():
            child.childs.append(sibling.childs.pop(0))
        node.keys[i] = sibling.keys.pop(0)
               

        
        
        
