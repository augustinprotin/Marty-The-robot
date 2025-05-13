from martypy import Marty
import keyboard

def celebration():
    my_marty.celebrate(4000)
    my_marty.dance()
    my_marty.circle_dance()
    my_marty.wave('left')

def goingLeft():
    my_marty.stand_straight(200)
    my_marty.sidestep("left", 2, 50)


def goingRight():
    my_marty.stand_straight(200)
    my_marty.sidestep("right", 2, 50)

def goingForward():
    #for i in range(0, 2):
        my_marty.walk(2, 'auto', 0, 20, 1500, True)
        my_marty.stand_straight(200)


def goingBackward():
    my_marty.stand_straight(200)
    my_marty.walk(2, 'auto', 0, -20)

def turnRight():
    for i in range(0, 5):
        my_marty.stand_straight(200)
        my_marty.walk(2, 'auto', 5, 5)

def turnLeft():
    my_marty.stand_straight(200)
    for i in range(0, 5):
        my_marty.walk(2, 'auto', -5, 5)

def looking(emotion):
    if(emotion == 'angry'):
        my_marty.eyes('angry', 800)

    if (emotion == 'normal'):
        my_marty.eyes('normal', 800)

    if (emotion == 'wide'):
        my_marty.eyes((40) , 800)

    if (emotion == 'wiggle'):
        my_marty.eyes('wiggle', 800)


if __name__ == '__main__':

    #ne pas oublier de se connecet au wifi "wifibotlab" !

    my_marty = Marty("wifi", "192.168.0.101")
    my_marty.stand_straight(200)
    #goingLeft()
    #goingForward()
    #goingRight()
    #goingBackward()
    #turnRight()
    #turnLeft()
    looking('angry')
    my_marty.disco_color('blue')
    #goingForward()
    yes = True
    while(yes == True):
        if keyboard.is_pressed('l'):
            yes = False

        elif keyboard.is_pressed('z'):
            goingForward()

        elif keyboard.is_pressed('s'):
            goingBackward()

        elif keyboard.is_pressed('d'):
            goingRight()

        elif keyboard.is_pressed('q'):
            goingLeft()

        elif keyboard.is_pressed('c'):
            celebration()