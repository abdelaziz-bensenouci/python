liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

def suppression(liste):
    liste_unique = []  

    for element in liste:
        present = False
        for unique in liste_unique:
            if element == unique:
                present = True
                break
        if not present:
            liste_unique += [element]  

    return liste_unique

print(suppression(liste))