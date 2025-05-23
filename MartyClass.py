import keyboard
from martypy import Marty
from PyQt6.QtCore import *


class MartyTheRobot:
    def __init__(self, modeConnexion, IpAddress):
        self.my_marty = Marty(modeConnexion, IpAddress)

    def celebration(self):
        self.my_marty.celebrate(4000)
        self.my_marty.dance()
        self.my_marty.circle_dance()
        self.my_marty.wave('left')

    def goingLeft(self):
        self.my_marty.stand_straight(200)
        self.my_marty.sidestep("left", 2, 50)

    def goingRight(self):
        self.my_marty.stand_straight(200)
        self.my_marty.sidestep("right", 2, 50)

    def goingForward(self):
        # for i in range(0, 2):
        self.my_marty.walk(2, 'auto', 0, 20, 1500, True)
        self.my_marty.stand_straight(200)

    def goingBackward(self):
        self.my_marty.stand_straight(200)
        self.my_marty.walk(2, 'auto', 0, -20)

    def turnRight(self):
        for i in range(0, 5):
            self.my_marty.stand_straight(200)
            self.my_marty.walk(2, 'auto', 5, 5)

    def turnLeft(self):
        self.my_marty.stand_straight(200)
        for i in range(0, 5):
            self.my_marty.walk(2, 'auto', -5, 5)

    def looking(self, emotion):
        if (emotion == 'angry'):
            self.my_marty.disco_color('red')
            self.my_marty.eyes('angry', 800)

        if (emotion == 'normal'):
            self.my_marty.disco_color('white')
            self.my_marty.eyes('normal', 800)

        if (emotion == 'wide'):
            self.my_marty.disco_color('green')
            self.my_marty.eyes((40), 800)

        if (emotion == 'wiggle'):
            self.my_marty.disco_color('blue')
            self.my_marty.eyes('wiggle', 800)


    def GetMarty(self):
        return self.my_marty



