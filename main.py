import keyboard
import MartyClass
from martypy import Marty
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from app import *
#from calibrage import *

#----------------- classe fenetre
#a telecharger :
# pip install PyQt6
# pip install PyQt6-tools

if __name__ == '__main__':

    #ne pas oublier de se connecet au wifi "wifibotlab" !

    my_marty = MartyClass.MartyTheRobot("wifi", "192.168.0.100")
    my_marty.GetMarty().stand_straight(200)
    yes = True
    while(yes == True):
        if keyboard.is_pressed('l'):
            yes = False

        elif keyboard.is_pressed('z'):
            my_marty.goingForward()

        elif keyboard.is_pressed('s'):
            my_marty.goingBackward()

        elif keyboard.is_pressed('d'):
            my_marty.goingRight()

        elif keyboard.is_pressed('q'):
            my_marty.goingLeft()

        elif keyboard.is_pressed('c'):
            my_marty.celebration()

        elif keyboard.is_pressed('1'):
            my_marty.looking('angry')

        elif keyboard.is_pressed('2'):
            my_marty.looking('normal')

        elif keyboard.is_pressed('3'):
            my_marty.looking('wide')

        elif keyboard.is_pressed('4'):
            my_marty.looking('wiggle')
    '''my_marty = Marty("wifi", "192.168.0.101")'''
    appli = QApplication(sys.argv)
    fenetre = MaFenetre()
    fenetre.show()
    sys.exit(appli.exec())
    my_marty.kick()