#import
#from tkinter import *
#from new_inter import *

#code
class Simulation:
    def __init__(self,strategie):
        self.strategie=strategie

    def run(self):
        cpt=0
        #interface = Interface()
        while self.strategie.stop==False:
            self.strategie.update()
            #test = self.strategie.robot
            #print(self.strategie.robot.safficher())
            #interface.rafraichir(test)
            cpt+=1
            
        print("Arret")
        self.strategie.robot.stop()
        
