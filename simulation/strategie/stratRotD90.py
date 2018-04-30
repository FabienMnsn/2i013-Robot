import API.robot2I013

class StratRotD90():
    
    def __init__(self,robot):
        self.rot=0
        self.opt=(robot.WHEEL_BASE_CIRCUMFERENCE/robot.WHEEL_CIRCUMFERENCE*1.0)*360
        self.stp=False
        self.robot=robot
        self.vitessed=-50
        self.vitesseg=50
        self.prec=self.robot.get_motor_position()[0]
        self.suiv=self.robot.get_motor_position()[0]
        
    def update(self):
        self.prec=self.robot.get_motor_position()[0]
        self.robot.rotate(self.opt/100)
        self.suiv=self.robot.get_motor_position()[0]
        self.rot+=abs(self.suiv-self.prec)
        if self.rot >= self.opt:
            self.stp=True
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        if self.rot >= self.opt*0.75:
            self.robot.set_motor_dps(3,30)
        
    def stop(self):
        return self.stp
