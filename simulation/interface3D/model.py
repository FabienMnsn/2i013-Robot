from pyglet.gl import *
from pyglet.window import key
import math
from composants.cube import Cube
from composants.mur import Mur
from composants.sol import Sol
from composants.arene import Arene

class Model:

    def get_tex(self,file):
        tex = pyglet.image.load(file).texture
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
        return pyglet.graphics.TextureGroup(tex)
    
    def __init__(self):
        self.batch = pyglet.graphics.Batch()

    def setArene(self,arene):
        self.arene=arene
        for c in arene.liste_cube:
            if isinstance(c, Mur):
                self.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),color=(1,1,1))
            elif isinstance(c, Sol):
                self.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),color=(192/255,192/255,192/255))
            elif isinstance(c, Cube):
                self.addCube((c.x,c.z,c.y),(c.lx,c.lz,c.ly),texture_file="interface3D/img/cube_side.png")
        if arene.robot != None:
            self.addRobot((arene.robot.getPos()),(arene.robot.DIMENSIONS))

    def addCube(self,coords,size,texture_file=None,color=(1,1,1,)):
        view=None
        
        if texture_file != None:
            view = self.get_tex(texture_file)
            view_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))
        else:
            view_coords= ('c3f',color*4)

        x,y,z = coords
        X,Y,Z = x+size[0], y+size[1], z+size[2]

        self.batch.add(4,GL_QUADS,view,('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),view_coords) # back
        self.batch.add(4,GL_QUADS,view,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),view_coords) # front
        
        self.batch.add(4,GL_QUADS,view,('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),view_coords) # left
        self.batch.add(4,GL_QUADS,view,('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),view_coords) # right
        
        self.batch.add(4,GL_QUADS,view,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),view_coords) # bottom
        self.batch.add(4,GL_QUADS,view,('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),view_coords) # top

    def addRobot(self,coords=(0,0,0), size=(150,250,150)):

        x,y,z = coords[0]-size[0]/2,coords[2],coords[1]-size[1]/2
        X,Y,Z = x+size[0], y+size[2], z+size[1]

        #view = self.get_tex("interface3D/img/robot.png")
        view_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))

        view=None 
        view_coords= ('c3f',(0,0,0)*4)
            
        self.rbac = self.batch.add(4,GL_QUADS,view,('v3f/dynamic',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),view_coords) # back
        self.rfro = self.batch.add(4,GL_QUADS,view,('v3f/dynamic',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),view_coords) # front
        
        self.rlef = self.batch.add(4,GL_QUADS,view,('v3f/dynamic',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),view_coords) # left
        self.rrig = self.batch.add(4,GL_QUADS,view,('v3f/dynamic',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),view_coords) # right
        
        self.rbot = self.batch.add(4,GL_QUADS,view,('v3f/dynamic',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),view_coords) # bottom
        self.rtop = self.batch.add(4,GL_QUADS,view,('v3f/dynamic',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),view_coords) # top

    def draw(self):
        self.batch.draw()
    
