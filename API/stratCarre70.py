import strat70
import stratRotD90
import robot2I013

class StratCarre70():
    
    def __init__(self,robot):
        self.distance=0
        self.cpt=0
        self.stp=False
        self.robot=robot
        self.S70=strat70.Strat70(robot)
        self.SRot=stratRotD90.StratRotD90(robot)
        
    def update(self):
        if not self.S70.stop():
            self.S70.update()
        else:
            if not self.SRot.stop():
                self.SRot.update()
            else:
                self.S70=strat70.Strat70(self.robot)
                self.cpt+=1
                self.SRot=stratRotD90.StratRotD90(self.robot)
        if self.cpt == 4:
            self.stp=True
            
    def stop(self):
        return self.stp
