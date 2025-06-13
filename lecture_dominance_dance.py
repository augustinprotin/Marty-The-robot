from MartyClass import MartyTheRobot
from app import *
import time

def lecture_dominance(mon_marty):

    file = open("dominance.dance", "r")
    lines = file.readlines()
    file.close()

    # verif fichier sequentiel
    if not lines[0].startswith("SEQ 3"):
        print("Fichier invalide")
        return 0

    #lecture lignes choregraphie
    for line in lines[1:]:
        print(line)
        distance = int(line[0])  
        direction = line[1]  

        #deplacement a droite 
        if direction == "R":
            for i in range(2*distance):
                mon_marty.goingRight()

        #deplacement a gauche
        elif direction == "L":
            for i in range(2*distance):
                mon_marty.goingLeft()

        #deplacement en avant
        elif direction == "U":
            for i in range(4*distance):
                mon_marty.goingForward()

        #deplacement en arriere
        elif direction == "B":
            for i in range(4*distance):
                mon_marty.goingBackward()

def ecriture_dominance(fichier):
    fichier = open(fichier, "w")
    fichier.write("SEQ 3\n")
    while(True):
        direction = input("choisissez une direction : ").strip().lower()
        distance = (input("choisissez un nombre de pas compris entre 1 et 3 : ")).strip()
        while(direction not in ["droite", "gauche", "avant", "arriere"] ):
            print("veuillez taper une direction existante : ")
            direction = input("choisissez une direction : ").strip().lower()
        if(direction == "droite"):
            fichier.write(distance+"R\n")
        elif(direction == "gauche"):
            fichier.write(distance+"L\n")
        elif(direction == "avant"):
            fichier.write(distance+"U\n")
        elif(direction == "arriere"):
            fichier.write(distance+"B\n")

        continuer = input("\nVoulez-vous détecter une autre couleur ? (o/n) : ")
        if continuer.lower() != 'o':
            fichier.close()
            print("Fin du programme.")
            break



