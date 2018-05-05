#imports

import random
import math
from robot_sim.teterobot import *
from robot_sim.capteur import *
from robot_sim.utilitaires_geometrie import *
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
        self.coords = coords # liste des 8 sommets du pave representant le robot pour l'instant il n'y en a que 4 => 2D 
        self.direction = direction
        self.dimension = dimension
        self.vitesse = vitesse
        self.tete= Creation_TeteRobot(self)
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
        (x0,y0,z0),(x1,y1,z1),(x2,y2,z2),(x3,y3,z3), (x4,y4,z4),(x5,y5,z5),(x6,y6,z6),(x7,y7,z7)= self.coords
            
        vitesse = dps/360 * self.WHEEL_CIRCUMFERENCE
        #print("vitesse", vitesse)

        norm_dir_tmp = math.sqrt(math.pow(xdir, 2) + math.pow(ydir, 2))
        #print("norm_dir:", norm_dir_tmp)
        dir_tmp = (xdir / norm_dir_tmp, ydir / norm_dir_tmp)
        #print("dir_tmp", dir_tmp)
        
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
        z += v1
            

        x0 += v0
        z0 += v1
        x1 += v0
        z1 += v1
        x2 += v0
        z2 += v1
        x3 += v0
        z3 += v1

        x4 += v0
        z4 += v1
        x5 += v0
        z5 += v1
        x6 += v0
        z6 += v1
        x7 += v0
        z7 += v1
        
        self.setPosition((x, y, z))
        self.setCoords(((x0,y0,z0),(x1,y1,z1),(x2,y2,z2),(x3,y3,z3), (x4,y4,z4),(x5,y5,z5),(x6,y6,z6),(x7,y7,z7)))
        #print("dir=",self.direction,"    centre=",self.position,"    coords=",self.coords)


    def get_motor_position(self):
        return self.roue_gauche,self.roue_droite

        
    def get_distance(self):
        capteur = Capteur(self.arene,self)
        dist = capteur.detecter_distance()*10

        if dist > 8000 :
            return 8190
        return dist


    def moyenne_dist(self):
	#retourne la moyenne des distances obtenues par le capteur de distance en mm
        somme=0 
        for i in range(0,5):
            somme+=self.get_distance()
        return somme/5

    
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
        self.__setAndNormaliseDirection(newdir)

        
    def calcul_coords(self):
        """cette fonction calcul les coordonnees (en fct de la position du robot qui appel la methode) des 8 sommet du pave droit qui represente le robot en 3D"""
        
        #on ramene la position du robot en 0 pour calculer les 8 coords des sommets
        coords = (-self.dimension[0]/2, 0, +self.dimension[2]/2, # base
                  +self.dimension[0]/2, 0, +self.dimension[2]/2, # base
                  +self.dimension[0]/2, 0, -self.dimension[2]/2, # base
                  -self.dimension[0]/2, 0, -self.dimension[2]/2, # base
                  -self.dimension[0]/2, self.dimension[1], +self.dimension[2]/2, # haut
                  +self.dimension[0]/2, self.dimension[1], +self.dimension[2]/2, # haut
                  +self.dimension[0]/2, self.dimension[1], -self.dimension[2]/2, # haut
                  -self.dimension[0]/2, self.dimension[1], -self.dimension[2]/2,)# haut
        #on calcul la difference d'angle entre la direction du robot et un vecteur arbitraire representant le nord ici l'axe z (profondeur)
        #comme le robot ne se deplace pas sur 3 axe on peut travailler en 2D (x,y)
        angle = calcul_angle2D( (self.direction), (0,1) ) #(0, 1) = le nord arbitraire
        angle1 = calcul_angle2D( (self.direction), (1,0) )
        print("angles:[",angle,"][",angle1,"]")
        #calcul des rotation de 'angle' degres sur chaque coordonnees
        if (angle == 90 and angle1 == 0):
            angle = -angle
            print("angles:[",angle,"][",angle1,"]")
        s0 = rotation2D( (coords[0], coords[2]), angle) #s0 = sommet correspondant au premier point de coords tourne de angle degres
        s1 = rotation2D( (coords[3], coords[5]), angle)
        s2 = rotation2D( (coords[6], coords[8]), angle)
        s3 = rotation2D( (coords[9], coords[11]), angle)
        s4 = rotation2D( (coords[12], coords[14]), angle)
        s5 = rotation2D( (coords[15], coords[17]), angle)
        s6 = rotation2D( (coords[18], coords[20]), angle)
        s7 = rotation2D( (coords[21], coords[23]), angle)

        #tous les (s0,s1,...,s7) sont des tuples de type (x,z)
        #on remplace chaque valeur de x et z (sans toucher a y qui est la hauteur du robot et qui ne change pas)
        #par sa valeur apres rotation contenue dans les (s0,s1,...,s7)
        #on profite de cette assignation pour redeplacer le robot a sa position initiale
        new_coords = ( (s0[0]+self.position[0], 0, s0[1]+self.position[2]),
                       (s1[0]+self.position[0], 0, s1[1]+self.position[2]),
                       (s2[0]+self.position[0], 0, s2[1]+self.position[2]),
                       (s3[0]+self.position[0], 0, s3[1]+self.position[2]),
                       (s4[0]+self.position[0], self.dimension[1], s4[1]+self.position[2]),
                       (s5[0]+self.position[0], self.dimension[1], s5[1]+self.position[2]),
                       (s6[0]+self.position[0], self.dimension[1], s6[1]+self.position[2]),
                       (s7[0]+self.position[0], self.dimension[1], s7[1]+self.position[2]),)
        
        #pour finir on remplace les coords (en attribut du robot) par celle fraichement calculees (new_coords)
        self.coords = new_coords


    def servo_rotate(self, position):
        """tourne la tete du robot a la position 'position'"""
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
    def setPosition(self, position):
        self.position = position


    def setAndNormaliseDirection(self, direction):
        norme_direction = math.sqrt(math.pow(direction[0], 2) + math.pow(direction[1], 2))
        if (norme_direction != 0):
            new_direction = (direction[0]/norme_direction, direction[1]/norme_direction)
            self.direction = new_direction
        else:
            self.direction = direction


    def setVitesse(self, vitesse):
        self.vitesse = vitesse


    def setCoords(self, coords):
        self.coords = coords
        
    
    """-----------------------SAVER-------------------------"""
    def toSaveF(self, f):
        """Ecrit les coordonnees du robot dans le fichier ouvert passe en argument, avec ';' comme separation"""
        f.write('Robot;' + str(self.position) + ';' +  str(self.direction) + ';' + str(self.dimension) + ';' + str(self.vitesse) + ';\n')




def calcul_coords(x,y,z, larg,long,haut, direX,direY):
    """cette fonction calcul les coordonnees des 8 sommet du pave droit
        de centre (x,y,z)
        de dimension (larg,long,haut)
        et de direction(direX,direY)"""
    
    #on ramene la position du robot en 0 pour calculer les 8 coords des sommets
    coords = (-larg/2, 0, +haut/2, # base
              +larg/2, 0, +haut/2, # base
              +larg/2, 0, -haut/2, # base
              -larg/2, 0, -haut/2, # base
              -larg/2, long, +haut/2, # haut
              +larg/2, long, +haut/2, # haut
              +larg/2, long, -haut/2, # haut
              -larg/2, long, -haut/2,)# haut
    #on calcul la difference d'angle entre la direction du robot et un vecteur arbitraire representant le nord ici l'axe z (profondeur)
    #comme le robot ne se deplace pas sur 3 axe on peut travailler en 2D (x,y)
    angle = calcul_angle2D( (direX,direY), (0,1) ) #(0, 1) = le nord arbitraire

    #calcul des rotation de 'angle' degres sur chaque coordonnees
    s0 = rotation2D( (coords[0], coords[2]), angle) #s0 = sommet correspondant au premier point de coords tourne de angle degres
    s1 = rotation2D( (coords[3], coords[5]), angle)
    s2 = rotation2D( (coords[6], coords[8]), angle)
    s3 = rotation2D( (coords[9], coords[11]), angle)
    s4 = rotation2D( (coords[12], coords[14]), angle)
    s5 = rotation2D( (coords[15], coords[17]), angle)
    s6 = rotation2D( (coords[18], coords[20]), angle)
    s7 = rotation2D( (coords[21], coords[23]), angle)

    #tous les (s0,s1,...,s7) sont des tuples de type (x,z)
    #on remplace chaque valeur de x et z (sans toucher a y qui est la hauteur du robot et qui ne change pas)
    #par sa valeur apres rotation contenue dans les (s0,s1,...,s7)
    #on profite de cette assignation pour redeplacer le robot a sa position initiale
    new_coords = ( (s0[0]+x, 0, s0[1]+z),
                   (s1[0]+x, 0, s1[1]+z),
                   (s2[0]+x, 0, s2[1]+z),
                   (s3[0]+x, 0, s3[1]+z),
                   (s4[0]+x, long, s4[1]+z),
                   (s5[0]+x, long, s5[1]+z),
                   (s6[0]+x, long, s6[1]+z),
                   (s7[0]+x, long, s7[1]+z))
    return new_coords

def Creation_Robot():
    """creation d'un Robot avec une position aleatoire"""

    x = 0
    y = 0
    z = 0 #un robot est posé sur le sol

    larg = 140
    long = 120
    haut = 250
    
    vitesse = 1
         
    newdir = (1,1)

    a=Creation_Arene()
    
    #coords = ((x-larg/2, y+long/2), (x+larg/2, y+long/2), (x+larg/2, y-long/2), (x-larg/2, y-long/2))

    #coords = calcul_coords(x,y,z, larg,long,haut, newdir[0],newdir[1])
    print(coords)
    return Robot((x,y,z), coords, newdir, (larg,long,haut), vitesse, a)


def Creation_Robot(x,z, dirX,dirZ):
    """creation d'un Robot avec une direction et une position definie"""

    y = 0 #un robot est posé sur le sol

    larg = 140
    long = 120
    haut = 250
    
    vitesse = 1
    
    a=Creation_Arene()
    
    coords = calcul_coords(x,y,z, larg,long,haut, dirX,dirZ)
    #print(coords)
    return Robot((x,y,z), coords, (dirX,dirZ), (larg,long,haut), vitesse, a)

        

