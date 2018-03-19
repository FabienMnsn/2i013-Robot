from robot2I013 import *
import math

class strategieToutDroit70:
    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        
    """def stop(self):
        self.robot.stop()
        return True""""

    def update(self):
        stop=False
        angle_prec = self.robot.read_encoder()
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,120)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,120)
        angle_actuel = self.robot.read_encoder()
        dist = (angle_actuel - angle_prec) * math.pi * (self.robot.WHEEL_DIAMETER/2.0)
        
        if dist > 70 :
            self.stop = True
            
