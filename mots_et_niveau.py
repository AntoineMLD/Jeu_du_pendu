import random

#listes par difficulté
niveaux = {
    "1" : ["chat", "chien", "fleur", "soleil", "arbre"],
    "2" : ["ordinateur", "aventure", "banane", "étoile", "livre"],
    "3" : ["rhinocéros", "électromagnétisme", "hippopotame", "incommensurabilité", "mégalomane"]

}

#listes par difficulté
def generation_des_mots_par_niveau(demande_niveau):
    
    mot_a_trouver = random.choice(niveaux[demande_niveau])
    
    
    
    # génère le mot caché en __
    mot_cacher = list("_" * len(mot_a_trouver))
    print("".join(mot_cacher))
    return mot_a_trouver, mot_cacher

