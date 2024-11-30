nom = str("stylo")
prix_unitaire = float(5)
quantité_en_stock = int(10)
print("l'article", nom, "coute", str(prix_unitaire),"euros", "et il en reste", str(quantité_en_stock), "en stock")

user = int(input("Combien de stylos désirez-vous?"))
maj_quantité = quantité_en_stock - user
print("Il reste maintenant", maj_quantité, "en stock")

prix_unitaire = float(5 + (5 * 10 /100))
print("l'article", nom, "coute maintenant", str(prix_unitaire),"euros", "et il en reste", str(maj_quantité), "en stock")

