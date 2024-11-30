def cesar_chiffrement(message, decalage):
    """
    Chiffre un message en utilisant le chiffrement de César avec un décalage donné.
    
    :param message: Le message à chiffrer (str).
    :param decalage: Le décalage pour le chiffrement (int).
    :return: Le message chiffré (str).
    """
    resultat = ""
    for caractere in message:
        if caractere.isalpha():  # Vérifie si le caractère est une lettre
            # Définir la base pour les majuscules et les minuscules
            base = ord('A') if caractere.isupper() else ord('a')
            # Calculer la nouvelle position avec dépassement
            nouvelle_position = (ord(caractere) - base + decalage) % 26 + base
            resultat += chr(nouvelle_position)  # Convertir en caractère
        else:
            resultat += caractere  # Laisser inchangé si ce n'est pas une lettre
    return resultat

message = "Salut, Jules César !"
decalage = 3
message_chiffre = cesar_chiffrement(message, decalage)
print(f"Message chiffré : {message_chiffre}")