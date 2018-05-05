#imports

#from robot_gopy.robot2I013 import *
from robot_sim.robot2 import *

#code

class strategieRot90():

    def __init__(self,robot):
        self.stop = False
        self.robot = robot
        self.dir_robot = robot.direction
        self.dir_depart = robot.direction
        self.dir_arrivee = rotation2D(self.dir_robot,90)

    """def update(self):
        if self.stop == False :
            if calcul_angle2D(self.dir_robot,self.dir_depart) == 0 :
                self.stop = True

            print('direction depart :',self.dir_depart,"direction arrivee", self.dir_arrivee)
            angle = calcul_angle2D(self.dir_robot,self.dir_depart)
            print('angle entre le robot et l arrivee',angle)
            new_dir = rotation2D(self.dir_robot,1) # 1 degres a chaque tour
            self.robot.direction = new_dir
            #print(self.robot.direction)"""
            
    def update(self):
        if self.stop == False:
            if ((self.robot.WHEEL_CIRCUMFERENCE/360)*self.robot.roue_droite) > (self.robot.WHEEL_BASE_CIRCUMFERENCE/4):
                self.stop = True
            else:
                self.robot.set_motor_dps(1,-30)
                self.robot.set_motor_dps(2,30)
                #self.robot.direction = rotation2D(self.robot.direction, 5)
                print(self.robot.direction, self.robot.roue_droite)
            
            
            
            
        
        
        
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
