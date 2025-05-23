from martypy import Marty
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import MartyClass
import capteur_batterie

class MaFenetre(QMainWindow):
    def __init__(self):
        super().__init__()



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
        self.ajouter_bouton("tourner-droite", "images/tourner-droite.png", 230, 510)
        self.ajouter_bouton("tourner-gauche", "images/tourner-gauche.png", 30, 510)
        self.ajouter_bouton("emotions", "images/emotions.png", 1350, 710)
        self.ajouter_bouton("lecture danse", "images/lecture danse.png", 1400, 600)
        self.ajouter_bouton("lecture feels", "images/lecture feels.png", 1300, 600)
        self.ajouter_bouton("batterie", "images/batterie.png", 1400, 0)

        #creation de la textbox
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("ip de marty")
        self.textbox.setGeometry(50, 30, 200, 30)

        #creation du bouton valider
        self.bouton = QPushButton("Valider", self)
        self.bouton.setGeometry(100, 80, 100, 30)
        self.bouton.clicked.connect(self.connecterALIp)

        self.texte_saisi = ""  # variable pour stocker le texte



    def connecterALIp(self):
        self.texte_saisi = self.textbox.text()
        try :
            print(f"IP testé : {self.texte_saisi}")
            self.my_marty = MartyClass.MartyTheRobot("wifi", str(self.texte_saisi))
            self.my_marty.GetMarty().disco_color("blue")
            #my_marty = Marty("wifi", "192.168.0.101")

        except Exception as e:
            print(f"Erreur attrapée : {e}")
        
    def ajouter_bouton(self, nom, chemin, x,y):
        bouton = QPushButton(self)
        bouton.setIcon(QIcon(chemin))
        bouton.setIconSize(QSize(100, 100))
        bouton.setGeometry(x, y, 100, 100)
        #bouton.setStyleSheet("border: none;")  # Supprime le cadre du bouton

        bouton.clicked.connect(lambda checked, n=nom: self.reagir_au_clic(n))

        self.boutons[nom] = bouton

    def reagir_au_clic(self, nom):
        print(f"✅ Clic sur le bouton : {nom}")
        if(nom == "fleche-haut"):
            print(f"il est censé avancer")
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
            capteur_batterie()

