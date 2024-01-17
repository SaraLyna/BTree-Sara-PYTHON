 # @author Sara Lyna OUYAHIA
 # @date 10/01/2024
 
 # classe qui gére les noeuds
 
 class Node:
    def __init__(self, value=None):
        self.keys = [value] #valeur utilisée pour comparer les noeuds
        self.value = value #valeur associée à la clé
        self.childs = [] #liste des enfants du noeud
        self.left = self.right = None
        self.size = 1
        self.parent = None
        
        
    def __str__(self):
        return str(self.value)
    
    def search_node(self, key):
        return key in self.keys
    
    
    def get_keys(self):
        return self.keys

    def get_childs(self):
        return self.childs

    def get_parent(self):
        return self.parent

    def get_size(self):
        return self.size

    def set_child(self, child_node):
        child_node.parent = self
        self.childs.append(child_node)
        self.size += child_node.size
 
