from robot2I013 import *
import math

class strategieRot90:

    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        self.angle_prec,x = self.robot.get_motor_position()
        
    def update(self,direction):
        ### effectue une rotation à droite de 90 degres

        quart_cercle = (2 * math.pi * (self.robot.WHEEL_DIAMETER/2.0))/4.0

        if direction == 'D' :
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,200)
		    self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,-200)
        
        elif direction == 'G' :
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,-200)
		    self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,200)

        angle_actuel,y = self.robot.get_motor_position()

        dist = ((angle_actuel - self.angle_prec)/360.0) * math.pi * (self.robot.WHEEL_DIAMETER/2.0) * 2
        
        if dist > quart_cercle:
            self.robot.stop()
            self.stop = True
           
