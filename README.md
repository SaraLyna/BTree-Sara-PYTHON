# Projet S6


# Binôme:
- Sara Lyna Ouyahia
- Mahiedine Ferdjoukh

# Présentation du projet et son lien avec le concept Objets :
Ceci est un projet en Python-objets, structuré avec des Arbre-B (Arbre-Balanced),
Un arbre de recherche est un dictionnaire qui préserve le classement d'une fonction spécifiée par l'utilisateur, également connue sous le nom de dictionnaire trié.
C'est globalement une implémentation d'un arbre binaire équilibré avec une vue (une fenetre ) et une intéraction avec l'utilisateur,
ce qui pourra permettre à l'utilisateur d'intéragir en temps réel avec la fenetre et construire l'arbre. en ajoutant/supprimant des noeuds/feuilles.
La notion d'objets sera exploré en faisant hérister la classe MyTree de TreeBalanced (classe générique),
le polymorphisme sera dans la surcharge des méthodes de la classe TreeBalanced dans la classe MyTree,
créer une fenêtre graphique (par exemple, en utilisant Tkinter) pour afficher notre arbre équilibré, on peut encapsuler la logique d'affichage dans une classe spécifique à l'interface utilisateur Window ! Cela permettra de séparer clairement la logique de l'arbre et celle de l'interface utilisateur, suivant le principe de la séparation des préoccupations.


## How To :

il suffit de lancer les tests unitaires directement dans le repertoire test 
ou via la commande `pipenv run test`

## UML :
[Diagramme UML (Lucid)](https://lucid.app/lucidchart/5362c04a-0055-4e38-96f6-b98e7b2418df/edit?view_items=hKf4u7b5I~bl&invitationId=inv_490324e7-3726-4202-810b-056d2cf5ce4e)

`pyreverse -o png -p node -A -my -S Node.py`
`pyreverse -o png -p tree_Balanced -A -my -S TreeBalanced.py`



## Journal de bord :

### Semaine 1 :
Mercredi 10 Janvier :
- Réflexion sur la manière d'implémenter un arbre binaire de recherche équilibré de manière originale.
- Possibilité de coder une sorte d'intéraction avec l'utilisateur pour lui permettre d'intéragir avec la fenetre et créer de lui meme un arbre.
- Ajouter des options telles que l'ajout ou la suppression de noeuds/feuilles.
- Commencer à créer les classes dés cette semaine.
- Mettre en surbrillance les noeuds auquels on veut ajouter des clés (par exemple).
- Rendre l'interface intéractive et drole (ajouter des chemins colorés pour les clés nouvellement ajoutées).
- explorer le double clic sur un noeud ou le passage de la souris dessus.
- D'abord commencer par afficher le squelette de l'arbre binaire équilibré.


### Semaine 2 :
Mercredi 17 Janvier :
- Modification de l'UML et ajout des différentes méthodes et relations entre les classes.
- Codage de la classe Node.py et implémentation de ses différentes méthodes.
- Suppression de la classe MyTree.py car seule la classe TreeBalanced nous intéresse finalement.
- Codage de la classe TreeBalanced.py et implémentation de ses méthodes essentielles telles que init() search_value(), search_bool() et is_Btree().
- pour cette semaine seul l'algorithme de recherche est demandé, on a fait un algo de recherche qui retourne une valeur(celle de la clé) et un 2eme algo qui retourne un booléen qui nous informe de la présence ou pas de la clé.
- En deuxième lieu on a fait les tests, les tests des méthodes de la classe Node.py
- réalisation des tests de la classe TreeBalanced.
- on a essayer de réaliser la structure de l'arbre.
- rectification de quelques erreurs dans la  classe TreeBalanced, apres le lancement des tests.



### Semaine 3 :
Mercredi 24 Janvier :
- Installation de pipenv sur le poste de travail afin d'automatiser les tests
- Modification de l'algorithme de recherche + amélioration
- codage de l'algorithme de linéarisation afin de tester l'ordre croissant des clés
- Tests pour les méthodes search(), linearize(), is_btree()
- Modification de l'UML pour etre en concordance avec le code
- Rédaction du Readme
- Finalisation des tests
- Fin de la recherche et de la linéarisation.


### Semaine 4 : 
Mercredi 31 janvier :
- ajout de la foction qui permet de calculer la profondeur d'un noeud.
- ajout d'une fonction qui verifie si l'arbre est équilibré en passant sa racine en parametre.
- amelioration de l'algorithme de recherche.
- passer le tests de is_balanced + de la fonction de get_depth qui retourne la profondeur d'un noeud.











## Sources à regarder : 

`docs.python-guide.org/writing/structure`

`packaging.python.org/en/lates+/tutorials/packaging-projects`

`McCreight, E.M. (1972), "Organization and maintenance of large ordered
indexes" (PDF), Acta Informatica`

`https://www.cs.usfca.edu/~galles/visualization/BTree.html`

`https://www.youtube.com/watch?v=coRJrcIYbF4`


## exemple de jeux :

- redblobgames.com (triangulation)
- thomas was alone
- oxyd , brainies/sqweek
- Robo Rally
- Ray tracer ? (gémoétrie + maths)






## Explication du fonctionnement du projet et des classes :
