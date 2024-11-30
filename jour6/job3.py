def tapis_diagonal(n):
    """
    Affiche un tapis de taille (n+1) x (n+1) traversé par une diagonale inversée.

    La diagonale est représentée par un espace ' ' et le reste du tapis par des '#'.
    
    :param n: La taille du tapis (n+1 lignes et n+1 colonnes).
    """
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j == n:  # Condition pour la diagonale inversée
                print(' ', end='')
            else:
                print('#', end='')
        print()  # Nouvelle ligne après chaque ligne du tapis

# Exemple d'utilisation
tapis_diagonal(10)