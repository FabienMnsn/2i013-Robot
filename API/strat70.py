import robot2I013

class Strat70():
    
    def __init__(self,robot):
        self.distance=0
        self.stp=False
        self.robot=robot
        self.vitesse=200
        self.prec=self.robot.get_motor_position()[0]
        self.suiv=self.robot.get_motor_position()[0]
        
    def update(self):
        self.prec=self.robot.get_motor_position()[0]
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,self.vitesse)
        self.suiv=self.robot.get_motor_position()[0]
        self.distance+=(self.suiv-self.prec)*self.robot.WHEEL_CIRCUMFERENCE/360.0
        if self.distance > 700-self.robot.WHEEL_CIRCUMFERENCE:
            self.vitesse=100
        if self.distance >= 700:
            self.stp=True
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        
    def stop(self):
        return self.stp
