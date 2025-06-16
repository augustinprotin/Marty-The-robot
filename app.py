from martypy import Marty
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import MartyClass
from capteur_batterie import *
from capteur_obstacle import *
from lecture_real_feels import *
from lecture_dominance_dance import *
import time

class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.my_marty = None

        self.setWindowTitle("Application controle de Marty")
        # 🔽 Changer l’icône ici
        self.setWindowIcon(QIcon("images/icone.png"))  # ou .ico selon ton OS
        # 🔽 Appliquer une resolution
        self.setMinimumSize(1020, 830)
        # 🔽 Dictionnaire d images
        self.boutons = {}
        # Créer plusieurs images avec leur nom
        self.ajouter_bouton("fleche-haut", "images/fleche-haut.png", 130, 510)
        self.ajouter_bouton("fleche-bas", "images/fleche-bas.png", 130, 710)
        self.ajouter_bouton("fleche-gauche", "images/fleche-gauche.png", 30, 610)
        self.ajouter_bouton("fleche-droite", "images/fleche-droite.png", 230, 610)
        self.ajouter_bouton("calibrage", "images/calibrage.png", 30, 710)
        self.ajouter_bouton("obstacle", "images/obstacle.png", 130, 610)
        self.ajouter_bouton("inter", "images/inter.png", 230, 710)
        self.ajouter_bouton("tourner-droite", "images/tourner-droite.png", 230, 510)
        self.ajouter_bouton("tourner-gauche", "images/tourner-gauche.png", 30, 510)
        self.ajouter_bouton("lecture danse", "images/lecture danse.png", 900, 710)
        self.ajouter_bouton("lecture feels", "images/lecture feels.png", 800, 710)
        self.ajouter_bouton("batterie", "images/batterie.png", 900, 10)
        self.ajouter_bouton("down", "images/down.png", 800, 10)
        self.ajouter_bouton("celebration", "images/celebration.png", 800, 610)
        self.ajouter_bouton("ecr_dance", "images/ecriture.png", 900, 610)
        self.ajouter_bouton("angry", "images/en-colere.png", 900, 510)
        self.ajouter_bouton("normal", "images/poker-face.png", 900, 410)
        self.ajouter_bouton("wiggle", "images/clin-doeil.png", 800, 510)
        self.ajouter_bouton("wide", "images/sourrire.png", 800, 410)



        #affiche marty pas connecté
        self.afficher_image_marty()


        #creation de la textbox
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("ip de marty")
        self.textbox.setGeometry(50, 30, 200, 30)

        #creation du bouton valider
        self.bouton = QPushButton("Valider", self)
        self.bouton.setGeometry(100, 80, 100, 30)
        self.bouton.clicked.connect(self.connecterALIp)

        self.texte_saisi = ""  # variable pour stocker le texte

    def afficher_image_marty(self, perdu_connect=0):
        """
        Affiche une image et un texte selon l'état perdu_connect.
        Reste bloquante pendant duree_ms millisecondes.
        """
        try:
            print("clear")
            self.image_label.clear()
        except Exception as e:
            print(e)

        images = {
            0: "images/perdu.png",
            1: "images/heureux.png",
            2: "images/mouvement.png",
            3: "images/couleur.png"
        }

        image_path = images.get(perdu_connect)
        if image_path:
            self.image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setGeometry(350, 100, pixmap.width(), pixmap.height())
            self.image_label.show()
            print(f"affichage du sprite {perdu_connect}")

        # Texte selon la condition
        if perdu_connect == 0:
            texte = "Marty est déconnecté"
        else:
            texte = "Marty est connecté"

        if hasattr(self, 'texte_label'):
            self.texte_label.setText(texte)
            self.texte_label.setGeometry(255, 30, 200, 30)
        else:
            self.texte_label = QLabel(texte, self)
            self.texte_label.setGeometry(255, 30, 200, 30)
            self.texte_label.show()


    def connecterALIp(self):
        self.texte_saisi = self.textbox.text()
        try :
            print(f"IP testé : {self.texte_saisi}")
            self.my_marty = MartyClass.MartyTheRobot("wifi", str(self.texte_saisi))
            self.my_marty.GetMarty().disco_color("blue")
            self.afficher_image_marty(1)
        except Exception as e:
            print(f"Erreur attrapée : {e}")
            self.afficher_image_marty()

    def ajouter_bouton(self, nom, chemin, x,y):
        bouton = QPushButton(self)
        bouton.setIcon(QIcon(chemin))
        bouton.setIconSize(QSize(100, 100))
        bouton.setGeometry(x, y, 100, 100)
        #bouton.setStyleSheet("border: none;")  # Supprime le cadre du bouton

        bouton.clicked.connect(lambda checked, n=nom: self.reagir_au_clic(n))

        self.boutons[nom] = bouton

    def getMartyFromWindow(self):
        return self.my_marty.GetMarty()

    def reagir_au_clic(self, nom):
        try :
            print(f"✅ Clic sur le bouton : {nom}")
            if(nom == "fleche-haut"):
                self.my_marty.goingForward()

            elif(nom == "fleche-bas" ):
                self.my_marty.goingBackward()

            elif(nom == "fleche-gauche" ):
                self.my_marty.goingLeft()

            elif(nom == "fleche-droite"):
                self.my_marty.goingRight()

            elif (nom == "tourner-gauche"):
                self.my_marty.turnLeft()

            elif (nom == "tourner-droite"):
                self.my_marty.turnRight()

            elif (nom == "emotions"):
                self.my_marty.looking("angry")

            elif (nom == "batterie"):
                print ("appel fonction")
                capteur_batterie(self)

            elif (nom == "obstacle"):
                print ("appel fonction")
                capteur_obstacle(self)

            elif (nom == "lecture danse"):
                lecture_dominance(self.my_marty)

            elif (nom == "lecture feels"):
                lecture_feels(self.my_marty.my_marty)




            elif (nom == "down"):
                print("on s arrete")
                try :
                    self.my_marty.GetMarty().close()
                except Exception as e :
                    print(e)
                self.afficher_image_marty(0)


            elif (nom == "calibrage"):
                self.afficher_image_marty(3)
                couleurs = ["noir", "bleu fonce", "bleu clair", "rouge", "rose", "jaune", "vert"]
                # Calibration
                for couleur in couleurs:
                    self.my_marty.calibrage(couleur, self)
                print("\nCalibration terminée")
                self.afficher_image_marty(1)

            elif (nom == "inter"):
                QMessageBox.information(self, "Quelle Couleur ?", "Place Marty sur la zone a détecter...")
                self.my_marty.reconnaitre_couleur(self)

            elif (nom =="ecr_dance"):
                self.ecriture_dominance("danse_file.danse")

            elif (nom == "angry"):
                self.my_marty.looking('angry')

            elif (nom == "wiggle"):
                self.my_marty.looking('wiggle')

            elif (nom == "normal"):
                self.my_marty.looking('normal')

            elif (nom == "wide"):
                self.my_marty.looking('wide')

            elif (nom=="celebration"):
                self.my_marty.celebration()

        except Exception :
            
            self.afficher_image_marty(0)
        #elif (nom == "clavier"):
        #    self.my_marty.check_keyboard(event)

    def getMarty(self):
        return self.my_marty

    def keyPressEvent(self,event: QKeyEvent):
        if self.my_marty is None:
            print("marty est none")
            return

        key = event.key()
        print(key)
        if key == 90:
            print("marty devrait avancer")
            self.my_marty.goingForward()

        elif key == 83:
            self.my_marty.goingBackward()

        elif key == 68:
            self.my_marty.goingRight()

        elif key == 81:
            self.my_marty.goingLeft()

        elif key == 67:
            self.my_marty.celebration()

        elif key == 49:
            self.my_marty.looking('angry')

        elif key == 50:
            self.my_marty.looking('normal')

        elif key == 51:
            self.my_marty.looking('wide')

        elif key == 52:
            self.my_marty.looking('wiggle')


        elif key == 54:
            self.afficher_image_marty(3)
            couleurs = ["noir", "bleu fonce", "bleu clair", "rouge", "rose", "jaune", "vert"]
            # Calibration
            for couleur in couleurs:
                self.my_marty.calibrage(couleur, self)
            print("\nCalibration terminée")
            self.afficher_image_marty(1)

        elif key == 55:
            self.afficher_image_marty(3)
            QMessageBox.information(self, "Couleur ?", "Place Marty sur la zone a détecter...")
            valeur_actuelle = self.my_marty.my_marty.get_ground_sensor_reading("left")
            couleur_detectee = self.detecter_couleur(valeur_actuelle)
            QMessageBox.information(self, "Couleur ?", f"Valeur mesurée : {valeur_actuelle}, on a donc la couleur : {couleur_detectee}")
            self.afficher_image_marty(1)
        
        elif key == 45:
            self.ecriture_dominance("dominance.danse")

        elif key == 56:
            lecture_feels(self.my_marty.my_marty)
            print("oui oui baguette")

        elif key == 57:
            lecture_dominance(self.my_marty)


    def detecter_couleur(self, val_mes):
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

    

    def demander_texte(parent: QWidget, message: str) -> str:
        texte, ok = QInputDialog.getText(parent, "Saisie", message)
        if ok:
            return texte.strip()
        return ""

    def ecriture_dominance(parent: QWidget, fichier_nom: str):
        try:
            with open(fichier_nom, "w") as fichier:
                fichier.write("SEQ 3\n")

                while True:
                    direction = MaFenetre.demander_texte(parent, "Choisissez une direction (droite, gauche, avant, arrière) :").lower()

                    while direction not in ["droite", "gauche", "avant", "arriere"]:
                        QMessageBox.warning(parent, "Erreur", "Veuillez taper une direction valide (droite, gauche, avant, arrière).")
                        direction =  MaFenetre.demander_texte(parent, "Choisissez une direction :").lower()

                    distance =  MaFenetre.demander_texte(parent, "Choisissez un nombre de pas (1 à 3) :")

                    if direction == "droite":
                        fichier.write(distance + "R\n")
                    elif direction == "gauche":
                        fichier.write(distance + "L\n")
                    elif direction == "avant":
                        fichier.write(distance + "U\n")
                    elif direction == "arriere":
                        fichier.write(distance + "B\n")

                    continuer =  MaFenetre.demander_texte(parent, "Voulez-vous écrire autre chose ? (o/n) :").lower()
                    if continuer != 'o':
                        QMessageBox.information(parent, "Terminé", "Fin du programme.")
                        break

        except Exception as e:
            QMessageBox.critical(parent, "Erreur", f"Une erreur est survenue : {str(e)}")