from robots.rconverter import RConverter as Robot
from strategie.simulation import Simulation
from strategie.strat70 import Strat70
from strategie.stratToutDroit import StratToutDroit
from strategie.stratCarre70 import StratCarre70
from strategie.stratRotD import StratRotD
import time

class q1_1():

    def __init__(self,robot):
        self.cpt=3
        self.stp=False
        self.robot=robot
        self.stratToutDroit=StratToutDroit(self.robot,100)
        self.stratRot=StratRotD(self.robot,60)
        
    def update(self):
        while(self.cpt>0):
            self.stratToutDroit.update()
            if self.stratToutDroit.stop():
                self.stratRot.update()
                if self.stratRot.stop():
                    self.cpt=self.cpt-1
                    self.stratToutDroit=StratToutDroit(self.robot,100)
                    self.stratRot=StratRotD(self.robot,60)
        self.stp=True     
        
    def stop(self):
        return self.stp

#En mm
POS=(0,0,0)
DIR=90
V=0

r=Robot(POS,DIR,V)

stratTriangle=q1_1(r)

simul=Simulation(stratTriangle, None)

simul.run()

