#ici la strategie pour que notre robot aille tout droit
import math

class stratdroit():
    def __init__(self, robot):
        self.robi = robot
        self.stop = False
        self.robi.rgo.set_motor_position(self, 3, 0, 0, 0)
        self.robi.rgo.offset_motor_encoder(self, 3, 0)
        self.deb = self.robi.rgo.get_motor_position()
        self.max = 50


    def update(self):
        if(self.robi.rgo.get_motor_position()<deb+self.max):
                self.robi.rgo.set_motor_dps(self, 3, 40)
        else self.stop=True




