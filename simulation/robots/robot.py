import math

class Robot():

    DIMENSIONS = (150,250,150)
    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 70  #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    
    def __init__(self, position, direction, vitesse):
        """Position: triplet (x,y,z)
           Direction: angle de direction compris entre 0 et 360
           Vitesse: v = nombre de degrés par itération"""
        self.pos=position
        self.x=position[0]
        self.y=position[1]
        self.z=position[2]
        self.dir=direction
        self.calcVectDir()
        self.v=vitesse
        self.strat=None
        
    """-----------------GET------------------"""   

    def getPos(self):
        return self.pos

    def getDirValue(self):
        return self.dir
     
    def getDirVect(self):
        return self.dx,self.dy

    def getDim(self):
        return DIMENSIONS

    def getVitesse(self):
        return self.v    
 
    """-----------------SET------------------"""

    def setPos(self, position):
        self.pos = position

    def setDir(self, direction):
        self.dir = direction
        self.calcVectDir()
        
    def setVitesse(self, vitesse):
        self.v = vitesse
        
    def setStrat(self, strat):
        self.strat=strat

    """----------------CALCUL----------------"""

    def calcVectDir(self):
        self.dx=round(math.cos(self.dir/360*2*math.pi),10)
        self.dy=round(math.sin(self.dir/360*2*math.pi),10)
        
    """---------------METHODES---------------"""

    def move(self):
        self.x+=(self.v/360*self.WHEEL_CIRCUMFERENCE)*self.dx
        self.y+=(self.v/360*self.WHEEL_CIRCUMFERENCE)*self.dy
        self.pos=(self.x,self.y,self.z)
     
    def rotate(self, angle):
        self.dir+=angle
        self.calcVectDir()
        
    def runStrat(self):
        if(self.strat!=None):
            self.strat.update()
        else:
            print("Pas de stratégie affectée")
            
    """-----------------Print---------------"""

    def toString(self):
        return "Robot Virtuel:\n Position (en mm): {0},\n Direction: {1}° => {2},\n Vitesse (en degrés par itération): {3}\n".format(self.getPos(),round(self.getDirValue()), self.getDirVect(),self.getVitesse())
