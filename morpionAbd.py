import random

plateau = [" " for _ in range(9)]

#### Détermine qui seront les joueurs #####
def choixJoueurs():
    choix = 0
    while choix < 1 or choix > 2:
        choix = int(input("Si vous désirez jouer contre l'IA, tapez 1, sinon tapez 2 pour jouer contre un autre joueur: "))
        if choix == 1:
            joueurPrenom1 = input("Entrez le nom du joueur: ")
            print(joueurPrenom1.upper(), "aura le symbole X")
            joueurs = [joueurPrenom1, "IA"]

        elif choix == 2:
            joueurPrenom1 = input("Entrez le nom du premier joueur: ")
            joueurPrenom2 = input("Entrez le nom du deuxième joueur: ")
            joueurs = [joueurPrenom1, joueurPrenom2]
            listSymbole = ["X", "O"]
            for i in range(len(joueurs)):
                print(joueurs[i].upper(), "aura le symbole", listSymbole[i])
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
    
    return joueurs 

joueurs = choixJoueurs()

#### Affichage du plateau #####
def affich_plateau(plateau, initial=False):
    if initial:
        print("Plateau initial : (utilisez les numéros pour jouer)")
        print("1 | 2 | 3")
        print("---------")
        print("4 | 5 | 6")
        print("---------")
        print("7 | 8 | 9")
    else:
        for ligne in range(3):
            start = ligne * 3
            print(plateau[start], "|", plateau[start + 1], "|", plateau[start + 2])
            if ligne < 2:
                print("---------")
                	#	Chaque ligne contient 3 cases, donc les indices des cases sont :
                    #	Ligne 0 : indices 0, 1, 2
                    #	Ligne 1 : indices 3, 4, 5
                    #
                    #	Ligne 2 : indices 6, 7, 8
                    #	La formule ligne * 3 calcule l’indice de départ de chaque ligne :
                    #	Si ligne = 0 → start = 0
                    #	Si ligne = 1 → start = 3
                    #	Si ligne = 2 → start = 6

#### Vérifie si il y a un gagnant #####
def verifieGagnant(plateau, symbole):
    for i in range(3):
        if plateau[i * 3] == plateau[i * 3 + 1] == plateau[i * 3 + 2] == symbole:
            return True
    for i in range(3):
        if plateau[i] == plateau[i + 3] == plateau[i + 6] == symbole:
            return True
    if plateau[0] == plateau[4] == plateau[8] == symbole:
        return True
    if plateau[2] == plateau[4] == plateau[6] == symbole:
        return True
    return False

#### Vérifie si le plateau est plein ####
def plateauComplet(plateau):
    return " " not in plateau

#### IA ####
def IA(plateau, symbole):
    ################################### Priorité 1: Vérifie si l'IA peut gagner #########################
    for i in range(3):
        # Vérif des lignes
        if plateau[i * 3] == plateau[i * 3 + 1] == symbole and plateau[i * 3 + 2] == " ":
            plateau[i * 3 + 2] = symbole
            return
        if plateau[i * 3 + 1] == plateau[i * 3 + 2] == symbole and plateau[i * 3] == " ":
            plateau[i * 3] = symbole
            return
        if plateau[i * 3] == plateau[i * 3 + 2] == symbole and plateau[i * 3 + 1] == " ":
            plateau[i * 3 + 1] = symbole
            return

    # Vérif des colonnes
    for i in range(3):
        if plateau[i] == plateau[i + 3] == symbole and plateau[i + 6] == " ":
            plateau[i + 6] = symbole
            return
        if plateau[i + 3] == plateau[i + 6] == symbole and plateau[i] == " ":
            plateau[i] = symbole
            return
        if plateau[i] == plateau[i + 6] == symbole and plateau[i + 3] == " ":
            plateau[i + 3] = symbole
            return

    # Vérif des diagonales
    if plateau[0] == plateau[4] == symbole and plateau[8] == " ":
        plateau[8] = symbole
        return
    if plateau[4] == plateau[8] == symbole and plateau[0] == " ":
        plateau[0] = symbole
        return
    if plateau[2] == plateau[4] == symbole and plateau[6] == " ":
        plateau[6] = symbole
        return
    if plateau[4] == plateau[6] == symbole and plateau[2] == " ":
        plateau[2] = symbole
        return
    if plateau[2] == plateau[6] == symbole and plateau[4] == " ":
        plateau[4] = symbole
        return
    
    ########################### Priorité 2: Bloquer le joueur ###################################
    for i in range(3):
        # Vérif les lignes
        if plateau[i * 3] == plateau[i * 3 + 1] == "X" and plateau[i * 3 + 2] == " ":
            plateau[i * 3 + 2] = symbole
            return
        if plateau[i * 3] == plateau[i * 3 + 2] == "X" and plateau[i * 3 + 1] == " ":
            plateau[i * 3 + 1] = symbole
            return
        if plateau[i * 3 + 1] == plateau[i * 3 + 2] == "X" and plateau[i * 3] == " ":
            plateau[i * 3] = symbole
            return
        
        # Vérif les colonnes
        if plateau[i] == plateau[i + 3] == "X" and plateau[i + 6] == " ":
            plateau[i + 6] = symbole
            return
        if plateau[i + 3] == plateau[i + 6] == "X" and plateau[i] == " ":
            plateau[i] = symbole
            return
        if plateau[i] == plateau[i + 6] == "X" and plateau[i + 3] == " ":
            plateau[i + 3] = symbole
            return

    #Vérif les diagonales 
    if plateau[0] == plateau[4] == "X" and plateau[8] == " ":
        plateau[8] = symbole
        return
    if plateau[4] == plateau[8] == "X" and plateau[0] == " ":
        plateau[0] = symbole
        return
    if plateau[2] == plateau[4] == "X" and plateau[6] == " ":
        plateau[6] = symbole
        return
    if plateau[4] == plateau[6] == "X" and plateau[2] == " ":
        plateau[2] = symbole
        return
    if plateau[2] == plateau[6] == "X" and plateau[4] == " ":
        plateau[4] = symbole
        return


########################## Priorité 3: Joue dans une case libre #############################
    if plateau[4] == " ":
        plateau[4] = symbole
    else:
        casesDispos = [i for i in range(9) if plateau[i] == " "]  # Trouve les indices des cases libres
        if casesDispos:  # Vérifie s'il y a encore des cases libres
            choix = random.choice(casesDispos)  # Choisit une case libre au hasard
            plateau[choix] = symbole

################################## Dynamique du jeux ###########################################
def jouer():
    affich_plateau(plateau, initial=True)
    while True:
        for i in range(2):
            if joueurs[i] == "IA":
                print("C'est au tour de l'IA")
                symbole = "O" if i == 1 else "X"
                IA(plateau, symbole) 
            else:
                joueur = joueurs[i]
                print("C'est au tour de ", joueur.upper())
                case = int(input("Dans quelle case (de 1 à 9) désirez-vous placer votre symbole ? : "))
                while case < 1 or case > 9 or plateau[case - 1] != " ":
                    if plateau[case - 1] != " ":
                        print("Cette case est déjà occupée.")
                    else:
                        print("Saisir un nombre entre 1 et 9 correspondant à une case libre !")
                    case = int(input("Dans quelle case (de 1 à 9) désirez-vous placer votre symbole ? : "))
                symbole = "X" if i == 0 else "O"
                plateau[case - 1] = symbole
            affich_plateau(plateau)
            if verifieGagnant(plateau, symbole):
                if joueurs[i] == "IA":
                    print("Désolé, l'IA a gagné !")
                else:
                    print("Félicitations !", joueurs[i].upper(), "a gagné !")
                return
            if plateauComplet(plateau):
                print("Match nul!")
                return

jouer()