from martypy import Marty
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *




#----------------- classe fenetre
#a telecharger :
# pip install PyQt6
# pip install PyQt6-tools

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
        self.ajouter_bouton("emotions", "images/emotions.png", 1350, 710)
        self.ajouter_bouton("lecture danse", "images/lecture danse.png", 1400, 600)
        self.ajouter_bouton("lecture feels", "images/lecture feels.png", 1300, 600)

        
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


if __name__ == '__main__':
    
    #ne pas oublier de se connecet au wifi "wifibotlab" !

    '''my_marty = Marty("wifi", "192.168.0.101")'''
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec())
    my_marty.kick()