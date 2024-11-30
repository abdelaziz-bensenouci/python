import tkinter as tk
import random

class JeuNombreMystere:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu du Nombre Mystère")
        self.root.geometry("500x400")  
        self.root.resizable(False, False)  
        self.nombreAdecouvrir = random.randint(1, 10)
        self.compteur = 3
        
        
        self.label_message = tk.Label(root, text="Devine le nombre mystère entre 1 et 10 !", font=("Arial", 16))
        self.label_message2 = tk.Label(root, text="Tu as 3 chances", font=("Arial", 16))
        self.label_message.pack(pady=20)
        self.label_message2.pack(pady=20)
        
        
        self.entry_nombre = tk.Entry(root, font=("Arial", 14), justify="center", width=10)
        self.entry_nombre.pack(pady=10)
        
        
        self.bouton_valider = tk.Button(root, text="Valider", font=("Arial", 14), command=self.verifier_nombre)
        self.bouton_valider.pack(pady=10)
        
        
        self.label_feedback = tk.Label(root, text="", font=("Arial", 20))
        self.label_feedback.pack(pady=20)
    
    def verifier_nombre(self):
        try:
            nbr = int(self.entry_nombre.get())  
            if nbr < 1 or nbr > 10:
                self.label_feedback.config(text="Entrez un nombre entre 1 et 10.", fg="red")
                return
            
            if nbr == self.nombreAdecouvrir:
                self.label_feedback.config(text="Bravo ! C'est gagné !", fg="green")
                self.bouton_valider.config(state="disabled")
            else:
                self.compteur -= 1
                if self.compteur == 0:
                    self.label_feedback.config(text=f"C'est perdu ! Le bon nombre était {self.nombreAdecouvrir}.", fg="red")
                    self.bouton_valider.config(state="disabled")
                else:
                    if nbr < self.nombreAdecouvrir:
                        self.label_feedback.config(text="C'est plus !", fg="blue")
                    else:
                        self.label_feedback.config(text="C'est moins !", fg="blue")
        except ValueError:
            self.label_feedback.config(text="Veuillez entrer un nombre valide.", fg="red")

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = JeuNombreMystere(root)
    root.mainloop()