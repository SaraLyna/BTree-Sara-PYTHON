 # @author Sara Lyna OUYAHIA
 # @date 10/01/2024
 
 
 # create the balanced tree, l'arbre générique mère de My-Tree

import Node.py


class TreeBalanced :
    def __init__(self, l, u):
        self.degree = degree
        self.root = None
        self.size = 0
        self.l = l 
        self.u = u
        self.k = 0
        self.keys = [None] * (u - 1)
        self.childs = [None] * u
        
    def search_value(key, node): # retrun the key value
        if node is None:
            return None  
        elif key == node.key:
            return node.value  # Clé trouvée, retourner la valeur associée
        else:
            for child in node.childs:
                if key < child.key:
                    # La clé est inférieure à celle de l'enfant, recherche récursive à gauche
                    return search_value(key, child)
                elif key == child.key:
                    # La clé est égale à celle de l'enfant, retourner la valeur associée
                    return child.value
                else:
                    # La clé est supérieure à celle de l'enfant, recherche récursive à droite
                    return search_value(key, child)


    def search_bool(self, key, node): #returnBool
        if node is None:
            return False

        index = 0
        while index < node.k and key > node.keys[index]:
            index += 1

        if index < node.k and key == node.keys[index]:
            return True
        elif node.childs[index]:
            return self.searchBool(key, node.childs[index])
        else:
            return False
        
        
    def is_Btree(self, node):
        if node is None:
            return True

        if node.k > node.u - 1 or node.k < (node.u // 2) - 1:
            return False

        for i in range(node.k):
            if node.childs[i] and not self.is_Btree(node.childs[i]):
                return False

        if node.childs[node.k] and not self.is_Btree(node.childs[node.k]):
            return False

        return True
    
    
