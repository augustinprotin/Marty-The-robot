import keyboard

#import MartyClass
#from martypy import Marty
#import sys
#from PyQt6.QtWidgets import *
#from PyQt6.QtGui import *
#from PyQt6.QtCore import *
from app import *
#from calibrage import *

#----------------- classe fenetre
#a telecharger :
# pip install PyQt6
# pip install PyQt6-tools






if __name__ == '__main__':

    #ne pas oublier de se connecet au wifi "wifibotlab" !


    appli = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(appli.exec())

    # Fonction de contrôle clavier
