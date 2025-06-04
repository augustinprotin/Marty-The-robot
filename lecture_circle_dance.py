from MartyClass import MartyTheRobot

def lecture_dominance():
    # Créer une instance de MartyTheRobot
    mon_marty = MartyTheRobot("wifi", "192.168.0.107")

    file = open("dominance.dance", "r")
    lines = file.readlines()
    file.close()

    # verif fichier sequentiel
    if not lines[0].strip().startswith("SEQ 3"):
        print("Fichier invalide : 'SEQ 3' manquant.")
        return 0

    #lecture lignes choregraphie
    for line in lines[1:]:
        distance = int(line[0])  
        direction = line[-1]  

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
