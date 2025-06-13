import math

import keyboard
from martypy import Marty
from PyQt6.QtWidgets import QMessageBox



class MartyTheRobot:
    def __init__(self, modeConnexion, IpAddress):
        self.my_marty = Marty(modeConnexion, IpAddress)
        self.seuils_couleurs = {}


    def celebration(self):
        self.my_marty.celebrate(4000)
        self.my_marty.dance()
        self.my_marty.circle_dance()
        self.my_marty.wave('left')

    def goingLeft(self):
        self.my_marty.stand_straight(200)
        self.my_marty.sidestep("left", 2, 50)

    def goingRight(self):
        self.my_marty.stand_straight(200)
        self.my_marty.sidestep("right", 2, 45)

    def goingForward(self):
        # for i in range(0, 2):
        self.my_marty.walk(2, 'auto', 0, 20, 1500, True)
        self.my_marty.stand_straight(200)

    def goingBackward(self):
        self.my_marty.stand_straight(200)
        self.my_marty.walk(2, 'auto', 0, -20)

    def turnRight(self):
        for i in range(0, 5):
            self.my_marty.stand_straight(200)
            self.my_marty.walk(2, 'auto', 5, 5)

    def turnLeft(self):
        self.my_marty.stand_straight(200)
        for i in range(0, 5):
            self.my_marty.walk(2, 'auto', -5, 5)

    def looking(self, emotion):
        if (emotion == 'angry'):
            self.my_marty.disco_color('red')
            self.my_marty.eyes('angry', 800)

        if (emotion == 'normal'):
            self.my_marty.disco_color('white')
            self.my_marty.eyes('normal', 800)

        if (emotion == 'wide'):
            self.my_marty.disco_color('green')
            self.my_marty.eyes((40), 800)

        if (emotion == 'wiggle'):
            self.my_marty.disco_color('blue')
            self.my_marty.eyes('wiggle', 800)

    '''def calibrage(self, couleur_a_calibrer, fenetre ):
        #pb au moment de l'affichage de la texte box
        QMessageBox.information(fenetre, "Calibration", f"Place Marty sur la zone '{couleur_a_calibrer}' et clique sur OK.")
        #QMessageBox.information(fenetre, f"\nPlace Marty sur la zone '{couleur_a_calibrer}'")
        print("le message aurait du s'afficher")
        valeur = self.my_marty.get_ground_sensor_reading("left")
        print(f"Valeur détectée pour '{couleur_a_calibrer}' : {valeur}")
        self.seuils_couleurs[couleur_a_calibrer] = valeur'''

    def calibrage(self, couleur_a_calibrer, fenetre, side="left"):
        QMessageBox.information(fenetre, "Couleur ?", f"Placer Marty sur : {couleur_a_calibrer}")
        r = self.my_marty.get_color_sensor_value_by_channel(side, "red")
        g = self.my_marty.get_color_sensor_value_by_channel(side, "green")
        b = self.my_marty.get_color_sensor_value_by_channel(side, "blue")
        self.seuils_couleurs[couleur_a_calibrer] = (r, g, b)
        QMessageBox.information(fenetre, "Couleur !", f"Couleur '{couleur_a_calibrer}' enregistrée avec RGB = ({r}, {g}, {b})")

    def reconnaitre_couleur(self, fenetre,side="left", seuil=50):
        r = self.my_marty.get_color_sensor_value_by_channel(side, "red")
        g = self.my_marty.get_color_sensor_value_by_channel(side, "green")
        b = self.my_marty.get_color_sensor_value_by_channel(side, "blue")
        couleur_actuelle = (r, g, b)

        
        self.my_marty.disco_color(couleur_actuelle) #on change la couleur des yeux
        print (r,g,b)


        couleur_proche = "inconnue"
        distance_min = float("inf")

        for nom, ref_rgb in self.seuils_couleurs.items():
            dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(couleur_actuelle, ref_rgb)))
            if dist < distance_min and dist < seuil:
                distance_min = dist
                couleur_proche = nom

        QMessageBox.information(fenetre, "Quelle Couleur ?", f"Couleur détectée : {couleur_proche} (RGB = {couleur_actuelle})")
        return couleur_proche

    def GetMarty(self):
        return self.my_marty


