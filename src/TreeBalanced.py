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

        if len(node.keys) > self.degree - 1 or len(node.keys) < (self.degree // 2) - 1:
            return False

        for i in range(len(node.childs)):
            if node.childs[i] and not self.is_btree(node.childs[i]):
                return False

        return True
    