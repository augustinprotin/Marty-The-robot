from martypy import Marty
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

my_marty = Marty("wifi", "192.168.0.101")

# Dictionnaire pour stocker les seuils de réflexion associés à chaque couleur
seuils_couleurs = {}

def calibrage(couleur_a_calibrer):
    input(f"\nPlace Marty sur la zone '{couleur_a_calibrer}' et appuie sur Entree pour calibrer...")
    valeur = my_marty.get_ground_sensor_reading("left")
    print(f"Valeur détectée pour '{couleur_a_calibrer}' : {valeur}")
    seuils_couleurs[couleur_a_calibrer] = valeur

def detecter_couleur(val_mes):
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


if __name__ == '__main__':
    couleurs = ["noir", "bleu fonce", "bleu clair", "rouge", "rose", "jaune", "vert"]  
    # Calibration
    for couleur in couleurs:
        calibrage(couleur)

    print("\nCalibration terminée")

<<<<<<< HEAD
    # Détection en boucle
    while True:
        input("\nPlace Marty sur une zone et appuie sur Entrée pour détecter la couleur...")
        valeur_actuelle = my_marty.get_ground_sensor_reading("left")
        couleur_detectee = detecter_couleur(valeur_actuelle)
        print(f"Valeur mesurée : {valeur_actuelle}")
        print(f"Couleur détectée : {couleur_detectee}")

        continuer = input("\nVoulez-vous détecter une autre couleur ? (o/n) : ")
        if continuer.lower() != 'o':
            print("Fin du programme.")
            break
=======
    my_marty = Marty("wifi", "192.168.0.101")
    app = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(app.exec())
    my_marty.kick()


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
        bouton.setStyleSheet("border: none;")  # Supprime le cadre du bouton

        bouton.clicked.connect(lambda checked, n=nom: self.reagir_au_clic(n))

        self.boutons[nom] = bouton

    def reagir_au_clic(self, nom):
        print(f"✅ Clic sur le bouton : {nom}")
>>>>>>> 5b0072854fd64b0697d40d9679e50eb30c94eb32
