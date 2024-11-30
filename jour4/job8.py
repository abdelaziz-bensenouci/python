def periode(type: str, saison: str):
    if type.lower() == "fruits" and saison.lower() == "hiver":
        print("orange, mandarine et kiwi")
    elif type.lower() == "fruits" and saison.lower() == "été":
        print("Poire, fraise, cassis")
    elif type.lower() == "légume" and saison.lower() == "hiver":
        print("carotte, topinambour, endive")
    elif type.lower() == "légume" and saison.lower() == "été":
        print("artichaut, aubergine,navet")

periode("fruits", "hiver")
periode("fruits", "été")
periode("légume", "hiver")
periode("légume", "été")