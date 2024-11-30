import random

nombreAdecouvrir = random.randint(1, 10)
print("Tu as 3 chances pour découvir le nombre mystère")
nbr = int(input("Propose un premier nombre entre 0 et 10 : "))
compteur = 2


while nbr != nombreAdecouvrir:
    if nbr < nombreAdecouvrir:
        compteur -= 1
        print("C'est plus")
    elif nbr > nombreAdecouvrir:
        compteur -= 1
        print("C'est moins")
    
    nbr = int(input("Propose un autre nombre entre 0 et 10 : "))
    if compteur == 0 and nbr != nombreAdecouvrir:
        print("=====================================================")     
        print("================ C'est perdu ! ======================")
        print("=====================================================")     

        print("Tu as utilisé toutes tes chances")
        print("Le bon nombre était :", nombreAdecouvrir)
        exit()
print("=====================================================")     
print("================ C'est gagné ! ======================")
print("=====================================================")     

print("Le bon nombre était :", nombreAdecouvrir)