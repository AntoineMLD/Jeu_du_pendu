import random
from affichage import *
from mots_et_niveau import generation_des_mots_par_niveau

#tentatives possibles
tentatives = 6

#affiche le menu et le niveau
demande_niveau = input("Choisissez votre niveau de diffulté : 1 , 2 ou 3 : ")

#appel de la fonction pour générer les mots
mot_a_trouver, mot_cacher = generation_des_mots_par_niveau(demande_niveau)



#boucle pour trouver le mot
while tentatives > 0:
    demande_utilisateur = input("Devinez une lettre :")
    for i in demande_utilisateur:
        historique(demande_utilisateur)
    

    trouve = False
    #cherche l'index de la lettre
    for index, lettre in enumerate(mot_a_trouver):
        if lettre == demande_utilisateur:
            mot_cacher[index] = demande_utilisateur
            trouve = True 

    #astuces du niveau 3 à la troisième tentatives
    if tentatives == 4 and demande_niveau == "3":
        #trouve une lettre du mot à trouver qui n'est pas dans la liste données
        lettre_indice = ""
        for lettre in mot_a_trouver:
            if lettre not in lettres_donnees:
                lettre_indice = lettre
                break
        if lettre_indice:
            index_alea = random.randint(0, len(mot_cacher)-1)
            mot_cacher[index_alea] = lettre_indice
            print(f"Voici un indice : {lettre_indice}")




    if trouve:
        print(f"Bravo ! Vous avez trouvez {demande_utilisateur}")
        print("Lettres données : " + ", ".join(lettres_donnees))
        print("".join(mot_cacher))

    # tentatives et leurs etats associés
    else:
        tentatives -= 1
        if tentatives == 5:
            afficher_pendu(1)
            print(f"Dommage, il vous reste {tentatives}, tentatives ! ")
            
        elif tentatives == 4:
            afficher_pendu(2)
            print(f"Dommage, il vous reste {tentatives}, tentatives ! ")
            
        elif tentatives == 3:
            afficher_pendu(3)
            print(f"Dommage, il vous reste {tentatives}, tentatives ! ")
            
        elif tentatives == 2:
            afficher_pendu(4)
            print(f"Dommage, il vous reste {tentatives}, tentatives ! ")
            
        elif tentatives == 1:
            afficher_pendu(5)
            print(f"Dommage, il vous reste {tentatives}, tentatives ! ")
            
        elif tentatives == 0:
            afficher_pendu(6)
            print(f"Dommage, il vous reste {tentatives}, tentatives ! ")
            print(historique(demande_utilisateur))
        else:
            print(f"Dommage, il vous reste {tentatives}, tentatives ! ")

    if "".join(mot_cacher) == "".join(mot_a_trouver):
        print("Félicitations, vous avez trouvé le mot !")
        break

else:
    print(f"Vos tentatives sont arrivées à néant ! Le mot était : {mot_a_trouver}")
    
        
        
    
        



