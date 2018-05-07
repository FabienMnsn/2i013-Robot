import strat10
import stratRot120
import robot2I013

class StratTriangle():
    
    def __init__(self,robot):
        self.distance=0
        self.cpt=0
        self.stp=False
        self.robot=robot
        self.S10=strat10.Strat10(robot)
        self.SRot=stratRot120.StratRot120(robot)
        
    def update(self):
        if not self.S10.stop():
            self.S10.update()
        else:
            if not self.SRot.stop():
                self.SRot.update()
            else:
                self.S10=strat10.Strat10(self.robot)
                self.cpt+=1
                self.SRot=stratRot120.StratRot120(self.robot)
        if self.cpt == 3:
            self.stp=True
            
    def stop(self):
        return self.stp
