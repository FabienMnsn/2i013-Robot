from structures.robot import *
from Strategy import *
import time

class TestStrategy():
    def __init__(self,strategy):
        self.strategy = strategy
        
    def Test(self,robot):
        i = 0
        liste = self.strategy.dessine_carre(50)
        while i < len(liste):
            if liste[i] > 0:
                y=0
                while y < liste[i]:
                    #time.sleep(1)
                    robot.move_bis()
                    y = y +1
            else :
                #time.sleep(1)
                robot.rotation_bis(-90)
            i = i +1
        

    def Test2(self,robot,liste):
        i = 0

        if len(liste) == 0:
            return
        elif  liste[i] != 0 :
            
            if liste[i] == -1:
                robot.rotation_bis(-90)
                liste.pop(i)
            elif liste[i] > 0 :
                robot.move_bis()
                liste[i] = liste[i] -1
                if liste[i] == 0:
                    liste.pop(i)
            elif liste[i] == 0:
                liste.pop(i)

        return liste
                
            
