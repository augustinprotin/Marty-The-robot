from martypy import Marty

def capteur_batterie():
    battery_remain = my_marty.get_battery_remaining()
    try:
        QMessageBox.information(self, "Batterie", "Il reste " ,  battery_remain ,  " '%' de batterie")

    except Exception as e:
        
        QMessageBox.information(self, "Batterie", "Erreur attrapée : {e}")
    
