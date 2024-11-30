# Demander les longueurs des côtés du triangle
a = float(input("Entrez la longueur du premier côté (a): "))
b = float(input("Entrez la longueur du deuxième côté (b): "))
c = float(input("Entrez la longueur du troisième côté (c): "))

# Vérifier si un triangle peut être formé (Inégalités triangulaires)
if a + b > c and a + c > b and b + c > a:
    # Vérification si le triangle est rectangle
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Le triangle est rectangle.")
    
    # Vérification si le triangle est équilatéral
    if a == b == c:
        print("Le triangle est équilatéral.")
    
    # Vérification si le triangle est isocèle
    elif a == b or b == c or a == c:
        print("Le triangle est isocèle.")
    
    # Si ce n'est ni rectangle, ni équilatéral, ni isocèle, c'est un triangle quelconque
    else:
        print("Le triangle est quelconque.")
else:
    print("Les longueurs fournies ne peuvent pas former un triangle.")