from martypy import Marty

my_marty = Marty("wifi", "192.168.0.107")

def capteur_obstacle():
    if my_marty.foot_obstacle_sensed('left'):
        print("Obstacle détecté devant le pied gauche !")
    if my_marty.foot_obstacle_sensed('right'):
        print("Obstacle détecté devant le pied droit !")

if __name__ == '__main__':
    capteur_obstacle()