def arrondi_et_trier(liste):
    # Étape 1 : Arrondir les nombres
    liste_arrondie = []
    for nombre in liste:
        # Extraire la partie entière et la partie décimale
        entier = int(str(nombre).split('.')[0])  # Partie entière avant le point
        decimal = nombre - entier  # Partie décimale

        # Comparer la partie décimale
        if decimal < 0.5:
            liste_arrondie += [entier]  # Arrondir vers le bas
        else:
            liste_arrondie += [entier + 1]  # Arrondir vers le haut

    # Étape 2 : Trier la liste dans l'ordre croissant (tri par sélection)
    for i in range(len(liste_arrondie)):
        min_index = i
        for j in range(i + 1, len(liste_arrondie)):
            if liste_arrondie[j] < liste_arrondie[min_index]:
                min_index = j
        # Échanger les éléments
        liste_arrondie[i], liste_arrondie[min_index] = liste_arrondie[min_index], liste_arrondie[i]

    return liste_arrondie

# Exemple d'utilisation
liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(arrondi_et_trier(liste))