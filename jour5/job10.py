L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
produit = 1

for valeur in L:
    if 25 <= valeur <= 90:  
        produit *= valeur  

print("Produit des valeurs dans l'intervalle [25, 90] :", produit)