def arrondir_notes(notes):
    """
    Arrondit les notes selon les critères :
    - Si la note est inférieure à 40, elle reste inchangée (échec).
    - Si la note est supérieure ou égale à 40 et à moins de 3 points de son prochain
      multiple de 5, elle est arrondie à ce multiple.
    
    :param notes: Liste de notes (list[int]).
    :return: Liste de notes arrondies (list[int]).
    """
    notes_arrondies = []
    for note in notes:
        if note < 40:
            # Pas d'arrondi si la note est un échec
            notes_arrondies.append(note)
        else:
            # Calcul du prochain multiple de 5
            prochain_multiple_5 = ((note // 5) + 1) * 5
            # Si la différence est inférieure à 3, arrondi à ce multiple
            if prochain_multiple_5 - note < 3:
                notes_arrondies.append(prochain_multiple_5)
            else:
                # Sinon, conserver la note originale
                notes_arrondies.append(note)
    return notes_arrondies

# Exemple d'utilisation
notes = [33, 67, 38, 84, 72]
notes_arrondies = arrondir_notes(notes)
print(f"Notes originales : {notes}")
print(f"Notes arrondies  : {notes_arrondies}")