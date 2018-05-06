#imports

#from robot_gopy.robot2I013 import *
from robot_sim.robot2 import *
from robot_sim.utilitaires_geometrie import *
#code

class strategieRot90():

    def __init__(self,robot):
        self.stop = False
        self.robot = robot
        self.dir_robot = robot.direction
        #self.dir_depart = robot.direction
        self.dir_arrivee = rotation2D(self.dir_robot,90)

    """def update(self):
        angle = calcul_angle2D(self.robot.direction,self.dir_arrivee)
        #print("1)",angle)
        if angle > 1:
            new_dir = rotation2D(self.robot.direction,5)
            self.robot.direction = new_dir
            #self.robot.calcul_coords()
            #print("%.2f, %.2f"%(self.robot.direction[0], self.robot.direction[1]))
        elif angle < -1:
            new_dir = rotation2D(self.robot.direction,5)
            self.robot.direction = new_dir
            
        elif angle > -1 and angle < 1:
            #print("2)",angle, self.stop)
            self.stop = True
        self.robot.calcul_coords()"""


    def update(self):
        new_dir = rotation2D(self.robot.direction,90)
        self.robot.direction = new_dir
        print("%.0f, %.0f"%(self.robot.direction[0], self.robot.direction[1]))
        self.robot.calcul_coords()



        """   
        if self.stop == False :
            angle = calcul_angle2D(self.dir_robot,self.dir_arrivee)
            print(self.dir_arrivee,"|",self.dir_robot,"|",angle,"°")
            if angle == 0:
                self.stop = True
                print("fin de la strat")
            else:
                #print('direction depart :',self.dir_depart,"direction arrivee", self.dir_arrivee)
                #angle = calcul_angle2D(self.dir_robot,self.dir_depart)
                #print('angle entre le robot et l arrivee',angle)
                #print("NEW DIR")
                new_dir = rotation2D(self.dir_robot,90) # 1 degres a chaque tour
                self.robot.direction = new_dir
                #print(self.robot.direction)
                #print(self.robot.direction)
            self.robot.calcul_coords()
            """
    """def update(self):
        if self.stop == False:
            if ((self.robot.WHEEL_CIRCUMFERENCE/360)*self.robot.roue_droite) > (self.robot.WHEEL_BASE_CIRCUMFERENCE/4):
                self.stop = True
            else:
                self.robot.set_motor_dps(1,-30)
                self.robot.set_motor_dps(2,30)
                self.robot.direction = rotation2D(self.robot.direction, 5)
                print(self.robot.direction, self.robot.roue_droite)"""
            
            
            
            
        
        
        
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
