import math
from robots.robot import Robot
from API.robot2I013 import Robot2I013
#code

class RConverter:

    MOTOR_LEFT=1
    MOTOR_RIGHT=2
    DIMENSIONS = Robot.DIMENSIONS
    WHEEL_BASE_WIDTH         = Robot.WHEEL_BASE_WIDTH
    WHEEL_DIAMETER           = Robot.WHEEL_DIAMETER
    WHEEL_BASE_CIRCUMFERENCE = Robot.WHEEL_BASE_CIRCUMFERENCE
    WHEEL_CIRCUMFERENCE      = Robot.WHEEL_CIRCUMFERENCE

    def __init__(self, position, direction, vitesse):
        self.r=Robot(position, direction, vitesse)
        self.RW=vitesse
        self.LW=vitesse
        self.RM=0
        self.LM=0
        self.strat=None
        
    """=======================VIRTUEL========================="""
          
    """-----------------------GETTTER-------------------------"""
    
    def getPos(self):
        return self.r.getPos()

    def getDir(self):
        return self.r.getDir()

    def getDim(self):
        return self.r.getDim()

    def getVitesse(self):
        return self.r.vitesse

    """-----------------------SETTER-------------------------"""
    
    def setPos(self, position):
        self.r.setPos(position)

    def setDir(self, direction):
        self.r.setDir(direction)
        
    def setVitesse(self, vitesse):
        self.r.setVitesse(vitesse)
        self.RM=vitesse
        self.RM=vitesse
        
    def setStrat(self, strat):
        self.r.strat = strat
        self.strat = strat
        
    def move(self):
        self.r.move()
        self.RM+=self.RW
        self.LM+=self.LW
        
    def runStrat(self):
        RWinit=self.RW
        LWinit=self.LW
        self.RW=self.RW/100
        self.LW=self.LW/100
        self.r.runStrat()
        self.RW=RWinit
        self.LW=LWinit
        self.strat=self.r.strat
	   
    def rotate(self,teta):
        self.r.rotate(teta)
        RWinit=self.RW
        LWinit=self.LW
        LMold=self.LM
        RMold=self.RM
        rot=0
        if(teta>0):
            self.LW=-100
            self.RW=100
        elif(teta<0):
            self.LW=100
            self.RW=-100
        while(rot<abs(teta)):
            self.LM+=self.LW
            self.RM+=self.RW
            diff=abs(self.RM-RMold)
            RMold=self.RM
            rot+=((diff/360*Robot2I013.WHEEL_DIAMETER)/Robot2I013.WHEEL_BASE_CIRCUMFERENCE)*360
        self.RW=RWinit
        self.LW=LWinit
        
    def toString(self):
        return self.r.toString()+("Robot Reel:\n Roues en position\t({0},{1}) degrés\n à la vitesse\t({2},{3}) dps\n").format(self.LM,self.RM,self.LW,self.RW)

    """========================REEL=========================="""
    
    def set_motor_dps(self, port, dps):
        self.r.setVitesse=dps
        if(port==3):  
            self.RW=dps
            self.LW=dps
        elif (port==2):
            self.RW=dps
        elif (port==1):
            self.LW=dps
            
    def set_motor_limits(self,port,dps):
        assert 1==1
        
    def get_motor_position(self):
        return (self.LM,self.RM)
        
    def set_motor_position(self, port, position):
        if (port==3):
            self.RM=position
            self.LM=position
        elif (port==2):
            self.RM=position
        else: 
            self.LM=position
        

    def offset_motor_encoder(self, port, offset):
        assert 1==1
        
    def get_distance(self):
        assert 1==1
        
    def servo_rotate(self,position):
        assert 1==1
        
    def stop(self):
        self.setVitesse(0)
