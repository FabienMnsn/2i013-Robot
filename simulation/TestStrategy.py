from structures.robot import *
from Strategy import *
import time

class TestStrategy():
    def __init__(self,strategy):
        self.strategy = strategy

            
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
                
            
