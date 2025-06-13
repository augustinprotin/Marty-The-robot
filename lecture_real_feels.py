from martypy import Marty


def lecture_feels():

    file = open("real.feels", "r")
    lines = file.readlines()
    file.close()
    couleur = ""
    emotion = ""

    #lecture lignes choregraphie
    try:
        for line in lines:
            if(couleur != "" and emotion != ""):
                choix_emotion(emotion, couleur)

            compteur = 0
            passage_a_lacouleur = False
            couleur = ""
            emotion = ""

            for j in range(len(line)):
                if(line[j] == ";" and compteur == 0):
                    emotion = line[j+1] + line[j+2] + line[j+3]
                    compteur += 1


                elif(passage_a_lacouleur == True):
                    couleur += line[j]

                elif (line[j] == ";" and compteur == 1):
                    passage_a_lacouleur = True

    except:
        print("erreur ")








def choix_emotion(emotion, couleur):
    if (emotion == "ang"):
        my_marty.disco_color(couleur)

        my_marty.eyes('angry', 800)



    if (emotion == "nor"):
        my_marty.disco_color(couleur)

        my_marty.eyes('normal', 800)



    if (emotion == "wid"):
        my_marty.disco_color(couleur)

        my_marty.eyes((40), 800)



    if (emotion == "wig"):
        my_marty.disco_color(couleur)

        my_marty.eyes('wiggle', 800)



    if (emotion == "exc"):
        my_marty.disco_color(couleur)

        my_marty.eyes('excited', 800)




if __name__ == '__main__':
    my_marty = Marty("wifi", "192.168.0.103")
    lecture_feels()

