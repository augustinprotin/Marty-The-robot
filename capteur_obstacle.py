from martypy import Marty
from PyQt6.QtWidgets import QMessageBox
from app import *


def capteur_obstacle(fenetre):
    try:
        left_foot = fenetre.getMartyFromWindow().foot_obstacle_sensed('left')
        right_foot = fenetre.getMartyFromWindow().foot_obstacle_sensed('left')
    except Exception as e:
        QMessageBox.information(fenetre, "obstacle", f"Marty n est pas connecté\nErreur attrapée : {e}")
    else:
        if (left_foot and right_foot):
            QMessageBox.information(fenetre, "obstacle", f"obstacle devant les deux pieds")
        elif (left_foot):
            QMessageBox.information(fenetre, "obstacle", f"obstacle devant le pied gauche")
        elif (right_foot):
            QMessageBox.information(fenetre, "obstacle", f"obstacle devant le pied droit")
        else :
            QMessageBox.information(fenetre, "obstacle", f"pas d'obstacle")