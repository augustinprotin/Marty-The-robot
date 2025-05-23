import keyboard
import MartyClass

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