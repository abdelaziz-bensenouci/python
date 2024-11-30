def time_to_text(minutes: int):
    heures = minutes // 60  
    minutes_restantes = minutes % 60  
    print(heures, "heure et", minutes_restantes, "minutes")

time_to_text(150)