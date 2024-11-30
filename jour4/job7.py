def programmation(langage: str):
    langage = langage.lower()  # Convertir en minuscules pour eviter la casse 
    if langage == "javascript":
        print("tu es un développeur web")
    elif langage == "python":
        print("tu es un développeur IA")
    elif langage == "java":
        print("tu es un développeur logiciel")
    elif langage == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("un jour, je serai le meilleur développeur...")
    
programmation("Java")