import robot2I013

class StratRot120():
    
    def __init__(self,robot):
        self.rot=0
        self.stp=False
        self.robot=robot
        self.vitessed=-30
        self.vitesseg=30
        self.prec=self.robot.get_motor_position()[0]
        self.suiv=self.robot.get_motor_position()[0]
        
    def update(self):
        self.prec=self.robot.get_motor_position()[0]
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,-200)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,200)
        self.suiv=self.robot.get_motor_position()[0]
        self.rot+=self.suiv-self.prec
        print(self.rot)
        if self.rot >= 135:
            self.stp=True
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
            # Le robot tourne de 120°
        
    def stop(self):
        return self.stp
