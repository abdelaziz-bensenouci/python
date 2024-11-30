# Étape 1 : Découper la chaîne en mots
 # Si le caractère n'est pas un espace
# Ajoute à mot_courant
# Si espace, traite le mot complet
# S'assure qu'il y a un mot

# Étape 2 : Compte la longueur du mot
# Étape 3 : Vérifie la longueur et ajouter si nécessaire
# Réinitialise pour le prochain mot
 # Traite le dernier mot s'il n'est pas suivi d'un espace
# Étape 4 : Joindre les mots sélectionnés dans une chaîne
# Ajouter un espace entre les mots
def my_long_word(n, texte):
    
    mots_longueur = []
    mot_courant = "" 

    for caractere in texte:
        if caractere != " ": 
            mot_courant += caractere  
        else:
            
            if mot_courant:  
                
                longueur = 0
                for _ in mot_courant:
                    longueur += 1
                
                
                if longueur > n:
                    mots_longueur.append(mot_courant)
                
                mot_courant = ""  

   
    if mot_courant:
        longueur = 0
        for _ in mot_courant:
            longueur += 1
        if longueur > n:
            mots_longueur.append(mot_courant)

    
    resultat = ""
    for mot in mots_longueur:
        if resultat:
            resultat += " "  
        resultat += mot

    return resultat

texte = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"
print(my_long_word(3, texte))