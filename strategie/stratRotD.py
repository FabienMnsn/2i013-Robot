from robots.rconverter import RConverter

class StratRotD():
    
    def __init__(self,robot,opt):
        self.rot=0
        self.opt=opt
        self.stp=False
        self.robot=robot
        self.vitesseR=-50
        self.vitesseL=50
        self.robot.set_motor_dps(self.robot.MOTOR_RIGHT,self.vitesseR)
        self.robot.set_motor_dps(self.robot.MOTOR_LEFT,self.vitesseL)
        
    def update(self):
        self.prec=self.robot.get_motor_position()[0]
        self.suiv=self.robot.get_motor_position()[0]
        self.rot+=abs(self.suiv-self.prec)*self.robot.WHEEL_CIRCUMFERENCE/WHEEL_BASE_CIRCUMFERENCE
        if self.rot >= self.opt:
            self.stp=True
            self.robot.set_motor_dps(self.robot.MOTOR_LEFT+self.robot.MOTOR_RIGHT,0)
        if self.rot >= self.opt*0.75:
            self.vitesseR=-30
            self.vitesseL=30
        
    def stop(self):
        return self.stp
