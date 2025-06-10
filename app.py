from martypy import Marty
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import MartyClass
from capteur_batterie import *
from capteur_obstacle import *
import time

class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()

        self.my_marty = None

        self.setWindowTitle("Application controle de Marty")
        # 🔽 Changer l’icône ici
        self.setWindowIcon(QIcon("images/icone.png"))  # ou .ico selon ton OS
        # 🔽 Appliquer une resolution
        self.resize(1920, 1080)
        # 🔽 Dictionnaire d images
        self.boutons = {}
        # Créer plusieurs images avec leur nom
        self.ajouter_bouton("fleche-haut", "images/fleche-haut.png", 130, 510)
        self.ajouter_bouton("fleche-bas", "images/fleche-bas.png", 130, 710)
        self.ajouter_bouton("fleche-gauche", "images/fleche-gauche.png", 30, 610)
        self.ajouter_bouton("fleche-droite", "images/fleche-droite.png", 230, 610)
        self.ajouter_bouton("calibrage", "images/calibrage.png", 30, 710)
        self.ajouter_bouton("obstacle", "images/obstacle.png", 230, 710)
        self.ajouter_bouton("tourner-droite", "images/tourner-droite.png", 230, 510)
        self.ajouter_bouton("tourner-gauche", "images/tourner-gauche.png", 30, 510)
        self.ajouter_bouton("emotions", "images/emotions.png", 1350, 710)
        self.ajouter_bouton("lecture danse", "images/lecture danse.png", 1400, 600)
        self.ajouter_bouton("lecture feels", "images/lecture feels.png", 1300, 600)
        self.ajouter_bouton("batterie", "images/batterie.png", 1400, 0)
        self.ajouter_bouton("down", "images/down.png", 1300, 0)

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
    
    from PyQt5.QtCore import QEventLoop, QTimer

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
            self.image_label.setGeometry(400, 100, pixmap.width(), pixmap.height())
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
                self.afficher_image_marty(2)
                self.my_marty.goingForward()
                self.afficher_image_marty(1)

            elif(nom == "fleche-bas" ):
                self.afficher_image_marty(2)
                self.my_marty.goingBackward()
                self.afficher_image_marty(1)

            elif(nom == "fleche-gauche" ):
                self.afficher_image_marty(2)
                self.my_marty.goingLeft()
                self.afficher_image_marty(1)

            elif(nom == "fleche-droite"):
                self.afficher_image_marty(2)
                sleep
                self.my_marty.goingRight()
                self.afficher_image_marty(1)

            elif (nom == "tourner-gauche"):
                self.afficher_image_marty(2)
                self.my_marty.turnLeft()
                self.afficher_image_marty(1)

            elif (nom == "tourner-droite"):
                self.afficher_image_marty(2)
                self.my_marty.turnRight()
                self.afficher_image_marty(1)

            elif (nom == "emotions"):
                self.my_marty.looking("angry")

            elif (nom == "batterie"):
                print ("appel fonction")
                capteur_batterie(self)

            elif (nom == "obstacle"):
                print ("appel fonction")
                capteur_obstacle(self)

            elif (nom == "lecture danse"):
                self.my_marty.celebration()

            elif (nom == "down"):
                print("on s arrete")
                try :
                    self.my_marty.GetMarty().close()
                except Exception as e :
                    print(e)
                self.afficher_image_marty(0)

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
                self.my_marty.calibrage(couleur)
            print("\nCalibration terminée")
            self.afficher_image_marty(1)

        elif key == 55:
            input("\nPlace Marty sur une zone et appuie sur Entrée pour détecter la couleur...")
            valeur_actuelle = self.my_marty.my_marty.get_ground_sensor_reading("left")
            couleur_detectee = self.detecter_couleur(valeur_actuelle)
            print(f"Valeur mesurée : {valeur_actuelle}")
            print(f"Couleur détectée : {couleur_detectee}")

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
