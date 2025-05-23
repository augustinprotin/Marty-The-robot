from martypy import Marty



# Dictionnaire pour stocker les seuils de réflexion associés à chaque couleur
seuils_couleurs = {}

def calibrage(couleur_a_calibrer):
    input(f"\nPlace Marty sur la zone '{couleur_a_calibrer}' et appuie sur Entree pour calibrer...")
    valeur = my_marty.get_ground_sensor_reading("left")
    print(f"Valeur détectée pour '{couleur_a_calibrer}' : {valeur}")
    seuils_couleurs[couleur_a_calibrer] = valeur

def detecter_couleur(val_mes):
    if 0 <= val_mes <= 20:
        return "noir"
    elif 21 <= val_mes <= 27:
        return "bleu foncé"
    elif 28 <= val_mes <= 40:
        return "vert"
    elif 42 <= val_mes <= 65:
        return "bleu clair"
    elif 66 <= val_mes <= 90:
        return "rouge"
    elif 91 <= val_mes <= 110:
        return "rose"
    elif 170 <= val_mes <= 200:
        return "jaune"


if __name__ == '__main__':
    couleurs = ["noir", "bleu fonce", "bleu clair", "rouge", "rose", "jaune", "vert"]  
    # Calibration
    for couleur in couleurs:
        calibrage(couleur)

    print("\nCalibration terminée")

    # Détection en boucle
    while True:
        input("\nPlace Marty sur une zone et appuie sur Entrée pour détecter la couleur...")
        valeur_actuelle = my_marty.get_ground_sensor_reading("left")
        couleur_detectee = detecter_couleur(valeur_actuelle)
        print(f"Valeur mesurée : {valeur_actuelle}")
        print(f"Couleur détectée : {couleur_detectee}")

        continuer = input("\nVoulez-vous détecter une autre couleur ? (o/n) : ")
        if continuer.lower() != 'o':
            print("Fin du programme.")
            break
