hauteur = int(input("Entrer une hauteur: "))
espace = 0
espace2 = hauteur
print(" " * (espace2 + 1) + "/" + "\ ")
for i in range(0, hauteur):
    espace = espace + 2 
    espace2 = espace2 - 1
    print(" " * espace2, "/" + (" " * espace) + "\ ")

    
print("/" + "_" * (hauteur * 2 + 2) + "\ ")


