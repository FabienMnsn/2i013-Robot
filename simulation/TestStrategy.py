from structures.robot import *
from Strategy import *


class TestStrategy():
    def __init__(self,strategy):
        self.strategy = strategy
        
    def Test(self,robot):
        i = 0
        liste = self.strategy.dessine_carre(70)
        while i < len(liste):
            if liste[i] > 0:
                y=0
                while y < liste[i]:
                    robot.move_bis()
                    y = y +1
            else :
                robot.rotation_bis(90)

            i = i +1
        
        
