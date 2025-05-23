from martypy import Marty

my_marty = Marty("wifi", "192.168.0.107")

def capteur_batterie():
    battery_remain = my_marty.get_battery_remaining()
    print("Il reste " ,  battery_remain ,  " '%' de batterie" )

if __name__ == '__main__':
    capteur_batterie()