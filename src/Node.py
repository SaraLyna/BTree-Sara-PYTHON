
 # classe qui gére les noeuds

class Node:
    def __init__(self,key, value=None):
        self.keys = [key] #valeur utilisée pour comparer les noeuds
        self.value = value #valeur associée à la clé
        self.childs = [] #liste des enfants du noeud
        self.left = self.right = None
        self.size = 1
        self.parent = None


    def __str__(self):
        if self.keys:
            return f"{self.keys[0]} {self.value}" if self.value is not None else str(self.keys[0])
        else:
            return "Empty Node"


    def search_node(self, key):
        return key in self.keys


    def get_keys(self):
        return self.keys

    def get_childs(self):
        return self.childs

    def get_parent(self):
        return self.parent

    def get_size(self):
        size = 1
        for child in self.childs:
            size += child.get_size()
        return size

    def add_child(self, child_node):
        child_node.parent = self
        self.childs.append(child_node)
        self.size += child_node.size

    def is_leaf(self):
        return len(self.childs) == 0
