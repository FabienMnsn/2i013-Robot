#classe robot cote model
import robot2I013

class robotmd():

    def __init__(self, position, coords, direction, dimension, vitesse):
        """
        un robot au point de vu modele, est donc definit par:
            sa position(x,y,z)
            sa dimension(l,w,h)
            ses sommets (x1,y1, x2,y2, x3,y3, x4,y4)
            sa direction([dx,dy])
            ses traits physiques
            et par un accesseur a sa partie physique rphy
        """

        self.rgo = robot2I013
        self.pos = rgo.get_motor_position()
        self.coords = coords #sommets
        self.dir = direction
        self.dim = dimension
        self.vit = vitesse

    def rotation_bis(self, teta):
        """Effectue une rotation du robot (sur lui-même) de teta°"""
        angle = math.radians(teta)
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = self.coords

        ctx0 = (x0 - self.position[0]) * math.cos(angle) - (y0 - self.position[1]) * math.sin(angle) + self.position[0]
        cty0 = (x0 - self.position[0]) * math.sin(angle) + (y0 - self.position[1]) * math.cos(angle) + self.position[1]

        ctx1 = (x1 - self.position[0]) * math.cos(angle) - (y1 - self.position[1]) * math.sin(angle) + self.position[0]
        cty1 = (x1 - self.position[0]) * math.sin(angle) + (y1 - self.position[1]) * math.cos(angle) + self.position[1]

        ctx2 = (x2 - self.position[0]) * math.cos(angle) - (y2 - self.position[1]) * math.sin(angle) + self.position[0]
        cty2 = (x2 - self.position[0]) * math.sin(angle) + (y2 - self.position[1]) * math.cos(angle) + self.position[1]

        ctx3 = (x3 - self.position[0]) * math.cos(angle) - (y3 - self.position[1]) * math.sin(angle) + self.position[0]
        cty3 = (x3 - self.position[0]) * math.sin(angle) + (y3 - self.position[1]) * math.cos(angle) + self.position[1]

        newcoords = [((ctx0), (cty0)),
                     ((ctx1), (cty1)),
                     ((ctx2), (cty2)),
                     ((ctx3), (cty3))]

        self.setCoords(newcoords)  # maj coords des 4 points du robot
        # print("coords=",self.coords)
        self.calcdir()  # maj direction du robot

    """-----------------------GETTTER-------------------------"""

    def getPosition(self):
        return self.position

    def getDirection(self):
        return self.direction

    def getDimension(self):
        return self.dimension

    def getVitesse(self):
        return self.vitesse

    """-----------------------SETTER-------------------------"""

    def __setPosition(self, position):
        self.position = position

    def __setDirection(self, direction):
        self.direction = direction

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def setCoords(self, coords):
        self.coords = coords

    """-----------------------SAVER-------------------------"""

    def toSaveF(self, f):
        """Ecrit les coordonnees du robot dans le fichier ouvert passe en argument, avec ';' comme separation"""
        f.write('Robot;' + str(self.position) + ';' + str(self.direction) + ';' + str(self.dimension) + ';' + str(
            self.vitesse) + ';\n')
