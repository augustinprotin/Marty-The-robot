from martypy import Marty
from PyQt6.QtWidgets import QMessageBox
from app import *


def capteur_batterie(fenetre):
    try:
        battery_remain = fenetre.getMartyFromWindow().get_battery_remaining()
    except Exception as e:
        QMessageBox.information(fenetre, "Batterie", f"Marty n est pas connecté\nErreur attrapée : {e}")
    else:
        QMessageBox.information(fenetre, "Batterie", f"Il reste {battery_remain}% de batterie")