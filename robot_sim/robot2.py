#imports

import random
import math
from robot_sim.teterobot import *
from robot_sim.capteur import *
from basiques.arene import *

#code

class Robot:
    """
        Classe caractérisé par:
        Sa Position: triplet(x, y, z)
        Les coordonnees de ses 4 angles (xy0, xy1, xy2, xy3)
        Sa direction: triplet(a, b)
        Sa dimension(final): triplet(longueur, largeur, hauteur)
        Sa vitesse: entier
        sa tete: Class TeteRobot
    """

    WHEEL_BASE_WIDTH         = 117  # distance (mm) de la roue gauche a la roue droite.
    WHEEL_DIAMETER           = 66.5 #  diametre de la roue (mm)
    WHEEL_BASE_CIRCUMFERENCE = WHEEL_BASE_WIDTH * math.pi # perimetre du cercle de rotation (mm)
    WHEEL_CIRCUMFERENCE      = WHEEL_DIAMETER   * math.pi # perimetre de la roue (mm)
    MOTOR_LEFT               = 1
    MOTOR_RIGHT              = 2
    
    def __init__(self, position, coords, direction, dimension, vitesse, arene):
        self.position = position
        self.coords = coords
        self.direction = direction
        self.dimension = dimension
        self.vitesse = vitesse
        self.tete= Creation_TeteRobot()
        self.roue_gauche = 0
        self.roue_droite = 0 # angle des roues
        self.dps_roue_droite = 0
        self.dps_roue_gauche = 0 # vitesse de chacune des roues
        self.arene = arene
        self.max = -1



    def set_motor_limits(self,port,dps):
        self.max = dps
        
    def offset_motor_encoder(self, port, offset):
        """
        Fixe l'offset des moteurs (en degres) (permet par exemple de reinitialiser a 0 l'etat 
        du moteur gauche avec offset_motor_encode(self.MOTOR_LEFT,self.read_encoders()[0])
        
        :port: un des deux moteurs MOTOR_LEFT ou MOTOR_RIGHT (ou les deux avec +)
        :offset: l'offset de decalage en degre.

        Zero the encoder by offsetting it by the current position
        """
        if port == 1:
            self.roue_gauche -= offset
        elif port == 2:
            self.roue_droite -= offset
        elif port == 3:
            self.roue_gauche -= offset
            self.roue_droite -= offset
        else:
            print('Erreur : port > 3')
            return -1
            
            
    def set_motor_dps(self,port,dps):
        
        x, y, z = self.position
        xdir, ydir = self.direction
        #larg, long, haut = self.dimension
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = self.coords
            
        vitesse = dps/360 * self.WHEEL_CIRCUMFERENCE
        print("vitesse", vitesse)

        norm_dir_tmp = math.sqrt(math.pow(xdir, 2) + math.pow(ydir, 2))
        print("norm_dir:", norm_dir_tmp)
        dir_tmp = (xdir / norm_dir_tmp, ydir / norm_dir_tmp)
        print("dir_tmp", dir_tmp)
        
        v0 = (dir_tmp[0]*vitesse)
        v1 = (dir_tmp[1]*vitesse)

        if port == 1:
            self.dps_roue_gauche = dps
            self.roue_gauche += dps
        elif port == 2:
            self.dps_roue_droite = dps
            self.roue_droite += dps
        elif port == 3:
            self.dps_roue_gauche = dps
            self.dps_roue_droite = dps
            self.roue_gauche += dps
            self.roue_droite += dps
        else:
            print('Erreur : port > 3')
            return -1
        
        x += v0
        y += v1
            

        x0 += v0
        y0 += v1
        x1 += v0
        y1 += v1
        x2 += v0
        y2 += v1
        x3 += v0
        y3 += v1
        
        self.__setPosition((x, y, z))
        self.setCoords(((x0,y0),(x1,y1),(x2,y2),(x3,y3)))
        #print("dir=",self.direction,"    centre=",self.position,"    coords=",self.coords)

    def get_motor_position(self):
        return self.roue_gauche,self.roue_droite
        
    def get_distance(self):
        capteur = Capteur(self.arene,self)
        dist = capteur.detecter_distance()*10

        if dist > 8000 :
            return 8190
        return dist
    
    def stop(self):
        self.set_motor_dps(3,0)

    def set_motor_position(self,port,position):
        if port == 1:
            self.roue_gauche = position
        elif port == 2:
            self.roue_droite = position
        elif port == 3:
            self.roue_gauche = position
            self.roue_droite = position
        else:
            print('Erreur : port > 3')
            return -1
        
    def retourne_angle(self,x,y,xx,yy) :
        """ retourne un angle teta en radian selon une direction initale d'un
            vecteur u(x,y) et une les coordonées du vecteur de la prochaine
            direction d'un vecteur v(xx,yy) en paramètres """

        sgn = (x*yy)+(xx*y)
        u = sqrt((x*x)+(y*y)) #norme de u
        v = sqrt((xx*xx)+(yy*yy)) #norme de v
        
        tmp = ((x*xx)+(y*yy))/(u+v)
        teta = acos(tmp)

        if(sgn < 0):
            return -1*teta
        return teta


    def rotation_bis(self,teta):
        """Effectue une rotation du robot (sur lui-même) de teta°"""
        angle = math.radians(teta)
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = self.coords
        
        ctx0 = (x0-self.position[0])*math.cos(angle) - (y0-self.position[1])*math.sin(angle) + self.position[0]
        cty0 = (x0-self.position[0])*math.sin(angle) + (y0-self.position[1])*math.cos(angle) + self.position[1]

        ctx1 = (x1-self.position[0])*math.cos(angle) - (y1-self.position[1])*math.sin(angle) + self.position[0]
        cty1 = (x1-self.position[0])*math.sin(angle) + (y1-self.position[1])*math.cos(angle) + self.position[1]
    
        ctx2 = (x2-self.position[0])*math.cos(angle) - (y2-self.position[1])*math.sin(angle) + self.position[0]
        cty2 = (x2-self.position[0])*math.sin(angle) + (y2-self.position[1])*math.cos(angle) + self.position[1]
    
        ctx3 = (x3-self.position[0])*math.cos(angle) - (y3-self.position[1])*math.sin(angle) + self.position[0]
        cty3 = (x3-self.position[0])*math.sin(angle) + (y3-self.position[1])*math.cos(angle) + self.position[1]

        newcoords = [ ((ctx0), (cty0)),
                      ((ctx1), (cty1)),
                      ((ctx2), (cty2)),
                      ((ctx3), (cty3))]
        
        self.setCoords(newcoords)   #maj coords des 4 points du robot
        #print("coords=",self.coords)
        self.tete.rotation(teta)
        self.calcdir()              #maj direction du robot
        

    def calcdir(self):
        """ Calcule la direction du robot (correspond a l'avant du robot) et retourne cette derniere sous la forme : (x, y) """
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = self.coords

        dirxy1 = (self.position[0], self.position[1])
        dirxy2 = ( ((x0 + x1)/2), ((y0+y1)/2) )
        newdir = ( (dirxy2[0]-dirxy1[0]), (dirxy2[1]-dirxy1[1]) )
        self.__setDirection(newdir)

    def moyenne_dist(self):
	#retourne la moyenne des distances obtenues par le capteur de distance en mm
        somme=0 
        for i in range(0,5):
            somme+=self.get_distance()
        return somme/5
    
    def servo_rotate(self, position):
        self.tete.rotation(position)

    def toString(self):
        return "ROBOT[Corps]|position: {0}, direction: {1}, dimension{2}, vitesse: {3}".format(self.getPosition(),self.getDirection(),self.getDimension(),self.getVitesse())+"\n"+self.tete.toString()

    def safficher(self):
                """Methode d'affichage d'un robot au format :
                Robot[position, direction, taille, vitesse]
                """
                return "ROBOT([Corps] position: {0}, direction: {1}, dimension{2}, vitesse: {3}".format(self.getPosition(),self.getDirection(),self.getDimension(),self.getVitesse())#||| "+self.tete.safficher()+")"
                

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
        f.write('Robot;' + str(self.position) + ';' +  str(self.direction) + ';' + str(self.dimension) + ';' + str(self.vitesse) + ';\n')


def Creation_Robot():
        """creation d'un Robot avec une position aleatoire"""

        x = 60
        y = 60
        z = 1   #un robot est posé sur le sol

        larg = 30
        long = 50
        haut = 15

        dirxy1 = (x, y)
        dirxy2 = (((x-larg/2)+(x+larg/2))/2, ((y+long/2)+(y+long/2))/2 )
        newdir = ( round(dirxy2[0]-dirxy1[0]), round(dirxy2[1]-dirxy1[1]) )
        vitesse = 1

        #arene = Arene(500,500,0,[],[]).generateur_arene()
        a=Creation_Arene()
        
        coords = ((x-larg/2, y+long/2), (x+larg/2, y+long/2), (x+larg/2, y-long/2), (x-larg/2, y-long/2))
        return Robot((x,y,z), coords, newdir, (larg,long,haut), vitesse, a)
        

        

