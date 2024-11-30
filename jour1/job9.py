montant_initial = float(5000)
taux_rendement = float(10)
nv_montant_initial = montant_initial + 5000
nouveau_taux_rendement = taux_rendement + 2
gain_annuel = nv_montant_initial * (nouveau_taux_rendement / 100)
montant_final_annuel = nv_montant_initial + gain_annuel
print("Cette année vous avez gagné", gain_annuel)
print("Votre nouveau solde est de", montant_final_annuel, "euros")

montant_apres_retrait = montant_final_annuel - (montant_final_annuel * 10 / 100)
print("Suite à votre retrait de 10%, vous avez maintenant", montant_apres_retrait) 

taux_rendement_diminué = nouveau_taux_rendement - 1
print("Votre solde final est de", montant_apres_retrait + (montant_apres_retrait * taux_rendement_diminué / 100), "euros")