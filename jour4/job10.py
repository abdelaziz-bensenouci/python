def nbr(nombre: int):
    if nombre > 0 and isinstance(nombre, int):
        if nombre % 2 == 0:
            print(nombre, " est un nombre pair")
        else:
            print(nombre, " est un nombre impair")
    else:
        print("Veuillez saisir un nombre entier positif")

nbr(7)