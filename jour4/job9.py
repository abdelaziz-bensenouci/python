def moyenne(note1: int, note2: int, note3: int):
    return (note1 + note2 + note3) / 3

note1 = int(input("Entrez la premiere notes : "))
note2 = int(input("Entrez la deuxieme notes : "))
note3 = int(input("Entrez la troisième notes : "))
moyenne_etudiant = moyenne(note1, note2, note3)

if moyenne_etudiant == 20 or moyenne_etudiant >= 15:
    print("Très bon élève")
elif moyenne_etudiant == 14 or moyenne_etudiant >= 11:
    print("Bon élève")
elif moyenne_etudiant == 10 or moyenne_etudiant >= 8:
    print("Élève moyen")
elif moyenne_etudiant == 7 or moyenne_etudiant >= 0:
    print("Élève devant faire des efforts")

print(moyenne_etudiant)