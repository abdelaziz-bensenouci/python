def tri_bulles(L):
    n = 0  # Compte manuel pour simuler len(L)
    for t in L:
        n += 1  # On compte la longueur de la liste

    # Algorithme du tri à bulles
    for i in range(n):
        for j in range(0, n - i - 1):  # Parcours de la liste
            if L[j] > L[j + 1]:  # Si l'élément courant est plus grand
                L[j], L[j + 1] = L[j + 1], L[j]  # On échange

    return L

# Exemple d'utilisation
ma_liste = [7, 11, 42, 39, 2]
print(tri_bulles(ma_liste))