import math
import time
from martypy import Marty

color_reference = {}

def calibrer_couleur(nom_couleur: str, marty, side="left"):
    r = marty.get_color_sensor_value_by_channel(side, "red")
    g = marty.get_color_sensor_value_by_channel(side, "green")
    b = marty.get_color_sensor_value_by_channel(side, "blue")
    color_reference[nom_couleur] = (r, g, b)
    print(f"Couleur '{nom_couleur}' enregistrée avec RGB = ({r}, {g}, {b})")

def reconnaitre_couleur(marty, side="left", seuil=50):
    r = marty.get_color_sensor_value_by_channel(side, "red")
    g = marty.get_color_sensor_value_by_channel(side, "green")
    b = marty.get_color_sensor_value_by_channel(side, "blue")
    couleur_actuelle = (r, g, b)

    couleur_proche = "inconnue"
    distance_min = float("inf")

    for nom, ref_rgb in color_reference.items():
        dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(couleur_actuelle, ref_rgb)))
        if dist < distance_min and dist < seuil:
            distance_min = dist
            couleur_proche = nom

    print(f"Couleur détectée : {couleur_proche} (RGB = {couleur_actuelle})")
    return couleur_proche


def main():
    print("Connexion à Marty...")
    marty = Marty("wifi", "192.168.0.102")
    marty.enable_motors()

    time.sleep(1)
    print("Connexion établie.")

    print("\n=== Phase de calibrage des couleurs ===")
    while True:
        nom = input("Nom de la couleur à calibrer (ou tape 'fin' pour terminer) : ")
        if nom.lower() == "fin":
            break
        calibrer_couleur(nom, marty)
    
    while True:
        print("\nChoisis une option :")
        print("1. Reconnaître la couleur actuelle")
        print("2. Afficher les couleurs enregistrées")
        print("3. Quitter")
        choix = input("Ton choix : ")

        if choix == "1":
            reconnaitre_couleur(marty)
        elif choix == "2":
            print("Couleurs enregistrées :")
            for nom, rgb in color_reference.items():
                print(f"  {nom} : {rgb}")
        elif choix == "3":
            print("Fin du programme.")
            break
        else:
            print("Option invalide.")

if __name__ == "__main__":
    main()
