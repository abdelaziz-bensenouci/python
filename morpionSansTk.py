import random

# Fonction pour afficher le plateau
def afficher_plateau(plateau):
    for i in range(3):
        print(f" {plateau[i][0]} | {plateau[i][1]} | {plateau[i][2]} ")
        if i < 2:
            print("---+---+---")

# Vérifie si un joueur a gagné
def verifie_victoire(plateau, joueur):
    # Vérifie les lignes, colonnes et diagonales
    for i in range(3):
        if plateau[i][0] == plateau[i][1] == plateau[i][2] == joueur:
            return True
        if plateau[0][i] == plateau[1][i] == plateau[2][i] == joueur:
            return True
    if plateau[0][0] == plateau[1][1] == plateau[2][2] == joueur:
        return True
    if plateau[0][2] == plateau[1][1] == plateau[2][0] == joueur:
        return True
    return False

# Vérifie si le plateau est plein
def plateau_plein(plateau):
    for row in plateau:
        if " " in row:
            return False
    return True

# Fonction pour choisir un coup pour l'IA
def choisir_coup(plateau, joueur):
    adversaire = "X" if joueur == "O" else "O"
    
    # 1. Vérifie si l'IA peut gagner
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = joueur
                if verifie_victoire(plateau, joueur):
                    return i, j
                plateau[i][j] = " "  # Annuler le coup
    
    # 2. Vérifie si l'adversaire peut gagner et bloque
    for i in range(3):
        for j in range(3):
            if plateau[i][j] == " ":
                plateau[i][j] = adversaire
                if verifie_victoire(plateau, adversaire):
                    return i, j
                plateau[i][j] = " "  # Annuler le coup

    # 3. Si aucun coup gagnant ou bloquant, choisit un coup aléatoire
    choix_possibles = [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == " "]
    return random.choice(choix_possibles)

# Fonction principale du jeu
def jeu_morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]  # Crée un plateau vide
    joueur = "X"  # Le joueur humain commence
    while True:
        afficher_plateau(plateau)
        
        if joueur == "X":  # Tour du joueur humain
            print("Votre tour (X) :")
            ligne = int(input("Entrez le numéro de ligne (0-2) : "))
            col = int(input("Entrez le numéro de colonne (0-2) : "))
            if plateau[ligne][col] != " ":
                print("Cette case est déjà occupée, essayez une autre.")
                continue
            plateau[ligne][col] = "X"
        else:  # Tour de l'IA
            print("Tour de l'IA (O) :")
            ligne, col = choisir_coup(plateau, "O")
            plateau[ligne][col] = "O"
            print(f"L'IA a choisi la case {ligne}, {col}")
        
        if verifie_victoire(plateau, joueur):
            afficher_plateau(plateau)
            if joueur == "O":
                print("L'IA a gagné !")
            else:
                print(f"Félicitations ! {joueur} a gagné !")
            break
        
        if plateau_plein(plateau):
            afficher_plateau(plateau)
            print("Match nul !")
            break
        
        # Changer de joueur
        joueur = "O" if joueur == "X" else "X"

# Lancer le jeu
jeu_morpion()