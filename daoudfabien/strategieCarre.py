from robot2I013 import *
import math


class strategieCarre:
    #ceci est une strategie qui realise un carre de 70cm de cote
    #A TESTER EN VRAI !
    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        self.cpt_exec=0
        self.angle_prec,x = self.robot.get_motor_position()
        
    def update(self):
        self.stop = False
        
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,120)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,120)
        angle_actuel,y = self.robot.get_motor_position()
        dist = ((angle_actuel - self.angle_prec)/360.0) * math.pi * (self.robot.WHEEL_DIAMETER/2.0) * 2
        
        if dist >= 60 and dist < 70 :
            #test pour ralentir sur les 10 derniers centimetres/unite de mesure
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT + self.robot.MOTOR_LEFT,60)
        elif dist >= 70:
                #compteur pour les 4 cotes du carre: quand cpt_exec = 4, la strat est terminee
            self.cpt_exec += 1
            self.robot.stop()
            #self.robot.offset_motor_encoder(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT,0)
            #faire tourner le moteur gauche dans un sens (-360) ~> valeur a changer ?
            #self.robot.set_motor_position(self.robot.MOTOR_LEFT, -360)
            
            """
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,60)
            manque un truc pour compter le nb de rotations jusqua 90
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT,60)
            """

            self.robot.set_motor_position(self.robot.MOTOR_RIGHT, 360)
            #on "reactive" les moteurs en marche avant
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT + self.robot.MOTOR_LEFT,120)
        elif self.cpt_exec == 4:
            self.stop = True
            self.robot.stop()
        elif self.cpt_exec > 4:
            print ("le compteur de cote a depasse la valeur max 4 : pb?")
            self.stop = True
            self.robot.stop()
        

