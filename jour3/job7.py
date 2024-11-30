# Chaîne de départ (alphabet répété 10 fois)
chaine = "abcdefghijklmnopqrstuvwxyz" 

# Initialisation du nombre de caractères à afficher
ligne = 1  # La première ligne contient 1 caractère

# Boucle pour afficher les sous-chaînes croissantes
while ligne <= 26:  # On veut arrêter une fois qu'on atteint 'z'
    print(chaine[:ligne])  # Affiche les premiers 'ligne' caractères de la chaîne
    ligne += 2  # Augmente le nombre de caractères pour la prochaine ligne