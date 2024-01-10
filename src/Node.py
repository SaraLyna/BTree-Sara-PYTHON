 # @author Sara Lyna OUYAHIA
 # @date 10/01/2024
 
 # classe qui gére les noeuds
 
 class Node:
    def __init__(self, valeur):
        self.valeur = valeur
        self.gauche = None
        self.droite = None
        self.hauteur = 1 

    def __str__(self):
        return str(self.valeur)
 
