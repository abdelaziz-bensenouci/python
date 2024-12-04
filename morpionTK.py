import tkinter as tk
import random

class MorpionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Morpion avec IA")
        self.root.geometry("600x700")  # Définit une taille initiale pour la fenêtre
        
        # Initialisation du plateau
        self.plateau = [[" " for _ in range(3)] for _ in range(3)]
        self.joueur = "X"  # Le joueur humain commence
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        # Création des boutons pour le plateau
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text=" ", font=("Arial", 32), width=6, height=3,
                                   command=lambda x=i, y=j: self.jouer_coup(x, y))
                button.grid(row=i, column=j, padx=10, pady=10)  # Ajoute des marges (espacement)
                self.buttons[i][j] = button
        
        # Label d'état pour afficher les messages
        self.status_label = tk.Label(root, text="Votre tour (X)", font=("Arial", 20))
        self.status_label.grid(row=3, column=0, columnspan=3, pady=20)  # Ajoute de l'espace en bas
    def jouer_coup(self, x, y):
        
        # Vérifie si la case est déjà occupée
        if self.plateau[x][y] != " ":
            return
        # Le joueur humain joue
        self.plateau[x][y] = self.joueur
        self.buttons[x][y].config(text="X", state="disabled")
        
        # Vérifie si le joueur humain a gagné
        if verifie_victoire(self.plateau, "X"):
            self.status_label.config(text="Félicitations, vous avez gagné !")
            self.desactiver_plateau()
            return
        
        # Vérifie si le plateau est plein
        if plateau_plein(self.plateau):
            self.status_label.config(text="Match nul !")
            return
        
        # Tour de l'IA
        self.status_label.config(text="Tour de l'IA (O)...")
        self.root.after(500, self.tour_ia)  # Petite pause pour simuler le tour de l'IA
    
    def tour_ia(self):
        ligne, col = choisir_coup(self.plateau, "O")
        self.plateau[ligne][col] = "O"
        self.buttons[ligne][col].config(text="O", state="disabled")
        
        # Vérifie si l'IA a gagné
        if verifie_victoire(self.plateau, "O"):
            self.status_label.config(text="L'IA a gagné !")
            self.desactiver_plateau()
            return
        
        # Vérifie si le plateau est plein
        if plateau_plein(self.plateau):
            self.status_label.config(text="Match nul !")
            return
        
        # Retour au joueur humain
        self.status_label.config(text="Votre tour (X)")
    
    def desactiver_plateau(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

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

# Lancer l'application Tkinter
if __name__ == "__main__":
    root = tk.Tk()
    app = MorpionApp(root)
    root.mainloop()