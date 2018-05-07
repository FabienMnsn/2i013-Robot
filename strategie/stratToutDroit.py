from robots.rconverter import RConverter

class StratToutDroit():

    def __init__(self,robot,objectif):
        self.objectif=objectif
        self.distance=0
        self.stp=False
        self.robot=robot
        self.vitesse=50
        self.robot.setVitesse(self.vitesse)
        
    def update(self):
        self.robot.setVitesse(self.vitesse)
        prec=self.robot.get_motor_position()[0]
        self.robot.move()
        time.sleep(1)
        suiv=self.robot.get_motor_position()[0]
        self.distance+=(suiv-prec)*self.robot.WHEEL_CIRCUMFERENCE*1.0/360.0
        if self.distance > self.objectif-self.robot.WHEEL_CIRCUMFERENCE:
            self.vitesse=20
        if self.distance >= self.objectif:
            self.robot.stop()
            self.stp=True     
        
    def stop(self):
        return self.stp
