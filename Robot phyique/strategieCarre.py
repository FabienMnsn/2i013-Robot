from robot2I013 import *
import math

class strategieCarre:
    #ceci est une strategie qui réalise un carré de 70cm de coté
    #A TESTER EN VRAI !
    def __init__(self,robot):
        self.robot = robot
        self.stop = False
        self.cpt_exec=0

    #gestion de l'arret de la strategie plus facile avec une variable stop
    """def stop(self):
        self.robot.stop()
        return True""""

    def update(self):
        self.stop= False
        angle_prec = self.robot.read_encoder()
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,120)
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,120)
        angle_actuel = self.robot.read_encoder()
        dist = (angle_actuel - angle_prec) * math.pi * (self.robot.WHEEL_DIAMETER/2.0)
        
        if dist >= 60 and dist < 70 :
            #test pour ralentir sur les 10 derniers centimetres/unité de mesure
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT + self.robot.MOTOR_LEFT,60)
        elif dist >= 70:
            #compteur pour les 4 côtés du carré: quand cpt_exec = 4, la strat est terminée
            self.cpt_exec += 1
            self.robot.stop()
            #reinitialiser les offsets des moteurs? ~> pour pouvoir tourner sans bug (voir demain si ça marche xD)
            offset_motor_encode(self.robot.MOTOR_LEFT + self.robot.MOTOR_RIGHT,self.read_encoders()[0])
            #faire tourner le moteur gauche dans un sens (-360) ~> valeur à changer ?
            set_motor_position(self.robot.MOTOR_LEFT, -360)
            #faire tourner le moteur droit dans le sens opposé => rotation du robot par rapport à son centre
            set_motor_position(self.robot.MOTOR_RIGHT, 360)
            #on "réactive" les moteurs en marche avant
            self.robot.set_motor_dps(self.robot.MOTOR_RIGHT + self.robot.MOTOR_LEFT,120)
        elif cpt_exec == 4:
            self.robot.stop()
            self.stop = True
        elif cpt_exec > 4:
            print ("le compteur de cote à depassé la valeur max 4 : pb?")
        
