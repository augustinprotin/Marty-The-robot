from martypy import Marty

if __name__ == '__main__':

    #ne pas oublier de se connecet au wifi "wifibotlab" !

    my_marty = Marty("wifi", "192.168.0.101")
    my_marty.kick()