pendu = [
    
#etat 1
"""

        |
        |
        |
        |
        |
=========
""",
    
#etat 2
"""
+---+
    |   |
        |
        |
        |
        |
=========

""",


#etat 3
"""
+---+
    |   |
    O   |
        |
        |
        |
=========

""",


#etat 4
"""
  +---+
    |   |
    O   |
    |   |
        |
        |
=========
""",
    

#etat 5
"""
 +---+
    |   |
    O   |
   /|\  |
        |
        |
=========

""",

#etat 6
"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========
"""
]

#fonction pour afficher un etat
def afficher_pendu(num_etat):
    #affiche le dessin du pendu
    print(pendu[num_etat])
    #affiche l'historique
    print("Lettres données : ")
    print(", ".join(lettres_donnees))


#fonction pour afficher la liste de lettre déjà données

lettres_donnees = []

def historique(lettre):
    lettres_donnees.append(lettre)
    