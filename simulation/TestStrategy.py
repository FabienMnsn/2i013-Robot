from structures.robot import *
from Strategy import *
from structures.capteur import *
from structures.arene import *
import time

class TestStrategy():
    def __init__(self,strategy):
        self.strategy = strategy

            
    def Test2(self,arene,liste):
        i = 0
        robot = arene.liste_robot[0]
        capteur = Capteur(arene)
        distance = capteur.detecter_distance()
        if len(liste) == 0:
            return
        elif  liste[i] != 0 :
            
            if liste[i] == -1:
                robot.rotation_bis(-90)
                liste.pop(i)
            elif liste[i] > 0 :
                if distance > 3 :
                    robot.move_bis(arene)
                    liste[i] = liste[i] -1
                else :
                    print("Arret de la strategie : Présence d'un mur")
                    return False
                if liste[i] == 0:
                    liste.pop(i)
            elif liste[i] == 0:
                liste.pop(i)

        return liste

    def Test_avance_objectif(self,arene,liste):
        robot = arene.liste_robot[0]

        if len(liste) == 0:
            return

        else:
            i,j = liste[0]
            if i == 'x' :
                robot.move_bis(arene)
                liste.pop(0)
            elif i == 'r':
                robot.rotation_bis(-90)
                liste.pop(0)
            elif i == 'y' :
                robot.move_bis(arene)
                liste.pop(0)

        return liste



















        
                
            
