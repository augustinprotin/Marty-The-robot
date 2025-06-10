from MartyClass import MartyTheRobot
from app import *
import time

def lecture_dominance():
    # Créer une instance de MartyTheRobot
    #mon_marty = fenetre.getMartyFromWindow() + mettre fenetre en param d'entrées
    mon_marty = MartyTheRobot("wifi", "192.168.0.101")

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


if __name__ == '__main__':
    lecture_dominance()