def distance_phare(marches, hauteur_cm):
    """
    Calcule la distance totale parcourue par un gardien de phare en une semaine
    pour aller aux toilettes.

    :param marches: Nombre de marches du phare (int).
    :param hauteur_cm: Hauteur de chaque marche en centimètres (float).
    :return: None (imprime la distance totale en mètres).
    """
    # Nombre de déplacements par jour (5 allers-retours, donc 10 montées/descentes)
    deplacements_par_jour = 5 * 2
    # Distance parcourue pour une montée ou une descente (en cm)
    distance_par_course = marches * hauteur_cm
    # Distance totale par jour (en cm)
    distance_par_jour = deplacements_par_jour * distance_par_course
    # Distance totale sur une semaine (7 jours, converti en mètres)
    distance_semaine = (distance_par_jour * 7) / 100  # Convertir cm en m
    
    # Affichage du résultat formaté
    print(f"Pour {marches} marches de {hauteur_cm} cm, le gardien parcourt {distance_semaine:.2f} m par semaine.")

# Exemple d'utilisation
distance_phare(20, 15)