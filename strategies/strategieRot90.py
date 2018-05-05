#imports

#from robot_gopy.robot2I013 import *
from robot_sim.robot2 import *

#code

class strategieRot90():

    def __init__(self,robot):
        self.stop = False
        self.robot = robot
        self.dir_robot = robot.direction
        self.dir_arrivee = rotation2D(self.dir_robot,90)

    def update(self):
        if self.stop == False :
            if calcul_angle2D(self.dir_robot,self.dir_arrivee) == 0 :
                self.stop = True
    
            new_dir = rotation2D(self.dir_robot,5) # 5 degres a chaque tour
            self.robot.direction = new_dir
            print(self.robot.direction)
            

            
            
            
        
        
        
    """def __init__(self,robot):
        self.rot = 0
        self.stop = False
        self.robot = robot
        self.vitessed = -50
        self.vitesseg = 50
        self.prec = self.robot.get_motor_position()[0]
        #self.suiv = self.robot.get_motor_position()[0]
        
    def update(self):
        self.prec = self.robot.get_motor_position()[0]
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,-200)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,200)
        self.suiv = self.robot.get_motor_position()[0]
        self.rot += self.suiv - self.prec
        #print(self.rot)
        if self.rot >= 105:
            self.stop = True
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        if self.rot >= 75:
            self.vitessed = -30
            self.vitesseg = 30"""
