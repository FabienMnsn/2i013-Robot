from pyglet.gl import *
from pyglet.window import key
import math
from composants.cube import Cube
from composants.mur import Mur
from composants.sol import Sol
from composants.arene import Arene
from interface3D.viewCube import ViewCube
from interface3D.viewSol import ViewSol
from interface3D.viewMur import ViewMur
from interface3D.viewRobot import ViewRobot

def get_tex(file):
    tex = pyglet.image.load(file).texture
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
    
    return pyglet.graphics.TextureGroup(tex)

class Model:
    
    def __init__(self):
        self.batch = pyglet.graphics.Batch()
        self.arene=None
        self.Vrob=None

    def setArene(self,arene):
        self.arene=arene
        for c in arene.liste_cube:
            if isinstance(c, Mur):
                Vcube=ViewMur(self.batch,c)
                #self.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),color=(1,1,1))
            elif isinstance(c, Sol):
                Vcube=ViewSol(self.batch,c)
                #self.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),color=(192/255,192/255,192/255))
            elif isinstance(c, Cube):
                Vcube=ViewCube(self.batch,c)
                #self.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),texture_file="interface3D/img/cube_side.png")
        if self.arene != None and self.arene.robot != None:
            self.Vrob=ViewRobot(self.batch,self.arene.robot)

    def draw(self):
        self.batch = pyglet.graphics.Batch()
        self.setArene(self.arene)
        self.batch.draw()
    
