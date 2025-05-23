from martypy import Marty
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


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
        self.ajouter_bouton("fleche-haut", "images/fleche-haut.png", 130, 100+410)
        self.ajouter_bouton("fleche-bas", "images/fleche-bas.png", 130, 300+410)
        self.ajouter_bouton("fleche-gauche", "images/fleche-gauche.png", 30, 200+410)
        self.ajouter_bouton("fleche-droite", "images/fleche-droite.png", 230, 200+410)
        self.ajouter_bouton("calibrage", "images/calibrage.png", 30, 300+410)
        self.ajouter_bouton("tourner-droite", "images/tourner-droite.png", 230, 100+410)
        self.ajouter_bouton("tourner-gauche", "images/tourner-gauche.png", 30, 100+410)
        self.ajouter_bouton("emotions", "images/emotions.png", 1350, 710)
        self.ajouter_bouton("lecture danse", "images/lecture danse.png", 1400, 600)
        self.ajouter_bouton("lecture feels", "images/lecture feels.png", 1300, 600)

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
            my_marty = Marty("wifi", "192.168.0.101")
            print(f"IP testé : {self.texte_saisi}")
        
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