from math import acos
from math import sqrt
from ast import literal_eval
from composants.cube import *
from composants.mur import *
from composants.sol import *
from robots.robot import *

class Arene :

    def __init__(self, lx, ly, lz, liste_cube=[], robot=None) :
        self.lx = lx
        self.ly = ly
        self.lz = lz
        self.liste_cube = liste_cube
        self.robot = robot

    def generationA(self):

        if (len(self.liste_cube) == 0):
            s1 = Creation_Sol(self)
            self.addCube(s1)
            
            taille = self.lx  # taille de l'arene
            haut = self.lz - 1
            larg_mur = 300  # largeur des murs de contour

            m1 = Mur(0, 0, 0, taille - 1, larg_mur, haut)
            m2 = Mur(0, 0, 0, larg_mur, taille - 1, haut)
            m3 = Mur(0, taille - larg_mur - 1, 0, taille - 1, larg_mur, haut)
            m4 = Mur(taille - larg_mur - 1, 0, 0, larg_mur, taille - 1, haut)

            self.addCube(m1)
            self.addCube(m2)
            self.addCube(m3)
            self.addCube(m4)

            #generation de cubes aleatoires
            nb_obstacles = 5
            i = 0
            long_min = 500
            long_max = 3000
            larg_min = 500
            larg_max = 3000
            haut_min = 500
            haut_max = int((self.lz - 1)/2)
            while i < nb_obstacles:
                lx = random.randint(long_min, long_max)
                ly = random.randint(larg_min, larg_max)
                lz = random.randint(haut_min, haut_max)
                x = random.randint(larg_mur, taille - lx - 1)
                y = random.randint(larg_mur, taille - ly - 1)

                if ((x-lx/2>self.lx+Robot.DIMENSIONS[0])/2 or x+lx/2<(self.lx-Robot.DIMENSIONS[0])/2) and (y-ly/2>(self.ly+Robot.DIMENSIONS[1])/2 or y+ly/2<(self.ly-Robot.DIMENSIONS[1])/2):
                    c = Cube(x, y, 1, lx, ly, lz)
                    self.addCube(c)
                    i = i + 1

    def addCube(self,cube) :
        bx = 0<=cube.x and cube.x <= self.lx
        by = 0<=cube.y and cube.y <= self.ly
        bz = 0<=cube.z and cube.z <= self.lz

        L = 0<=cube.x + cube.lx and cube.x + cube.lx <= self.lx
        l = 0<=cube.y + cube.ly and cube.y + cube.ly <= self.ly
        h = 0<=cube.z + cube.lz and cube.z + cube.lz <= self.lx
        
        if bx and by and bz and L and l and h:
            self.liste_cube.append(cube)
            return True
        return False

    def delCube(self,x,y,z) :
        i = 0
        while i<len(self.liste_cube) :
            c = self.liste_cube[i]
            if c.x == x and c.y == y and c.z == z :
                del self.liste_cube[i]
                return True
            else :
                i= i+1
        return False

    def addRobot(self,robot) :
        x,y,z = robot.getPos()
        lx,ly,lz = robot.DIMENSIONS
        
        c1 = 0<x-lx/2 and x+lx/2 < self.lx
        c2 = 0<y-ly/2 and y+ly/2 < self.ly
        c3 = 0<z and z+lz < self.lz
        
        if c1 and c2 and c3:
            self.robot=robot
            return True
        return False


    def hasSol(self):
        if len(self.liste_cube) == 0:
            return False
        else:
            for i in self.liste_cube:
                if isinstance(i, Sol):
                    return True
            return False

    def toString(self):
        s="Arene: Dim [{0},{1},{2}]\n".format(self.lx,self.ly,self.lz)
        s+="Composants [\n"
        for i in self.liste_cube:
            s+=i.toString()
        s+="]\n"
        s+="Robot [\n"
        if(self.robot!=None):
            s+=self.robot.toString()
        s+="]\n"
        s+="}\n"
        return s
    
def Creation_Arene() :
    """ Test d'une creation d'Arene vide"""
    liste_cube = [] #liste vide pour créer une arène vide
    lx = 500
    ly = 500
    lz = 500 # valeurs limites de l'arène

    arene = Arene(lx,ly,lz,liste_cube)

    return arene
     
