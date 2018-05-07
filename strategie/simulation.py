from strategie.strat70 import Strat70
from strategie.stratToutDroit import StratToutDroit
from strategie.stratCarre70 import StratCarre70
from strategie.stratRotD import StratRotD

class Simulation():

        def __init__(self,strategie, arene):
                self.strategie = strategie
                self.arene=arene
                self.time=0

        def run(self):
                while not self.strategie.stop():
                        self.strategie.update()
                print("Stoping")

        def update(self, delta_time):
                if self.strategie != None:
                        if(self.time<1):
                                self.time+=delta_time
                        else:
                                self.time=0
                                if not self.strategie.stop():
                                        self.strategie.update()
                                else:
                                        self.strategie=None
                else:
                        self.arene.robot.move()
	        
