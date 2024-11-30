def my_sort(liste):
    """
    Trie une liste en échangeant uniquement des éléments adjacents jusqu'à obtention
    d'une liste triée dans l'ordre croissant.

    :param liste: Liste d'entiers à trier.
    :return: La liste triée et le nombre total de coups nécessaires.
    """
    n = len(liste)  # Taille de la liste
    coups = 0       # Compteur pour le nombre de coups nécessaires

    # Indique si un échange a eu lieu (utile pour arrêter si la liste est déjà triée)
    echange = True

    # Continue le tri tant qu'il y a des échanges
    while echange:
        echange = False  # Aucun échange au début de chaque passe
        for i in range(n - 1):
            # Comparer l'élément courant avec le suivant
            if liste[i] > liste[i + 1]:
                # Si la condition est remplie, échanger les deux éléments
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                coups += 1  # Incrémenter le compteur de coups
                echange = True  # Un échange a eu lieu, donc on continue
    # Afficher le nombre total de coups
    print(f"Nombre total de coups : {coups}")
    return liste

# Exemple d'utilisation
liste_non_triee = [5, 3, 8, 6, 2]
liste_triee = my_sort(liste_non_triee)
print(f"Liste triée : {liste_triee}")