from pyglet.gl import *
import math
from robots.robot import Robot
from interface3D.model import *

def get_tex(file):
    tex = pyglet.image.load(file).texture
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
    return pyglet.graphics.TextureGroup(tex)

class ViewRobot:
    
    def __init__(self, batch, robot):
        x,y,z = robot.getPos()[0]-robot.DIMENSIONS[0]/2,robot.getPos()[2],robot.getPos()[1]-robot.DIMENSIONS[1]/2
        X,Y,Z = x+robot.DIMENSIONS[0], y+robot.DIMENSIONS[2], z+robot.DIMENSIONS[1]
        """
        angle = robot.getDirValue()
        print("Angle Rotation = ", angle)
        
        rayon = math.sqrt((robot.DIMENSIONS[0]/2)**2+(robot.DIMENSIONS[1]/2)**2)
        print("Rayon = ", rayon)
        newx = rayon*math.cos(angle)
        
        newz = rayon*math.sin(angle)
        
        vectx=newx-robot.DIMENSIONS[0]/2
        vectz=newz-robot.DIMENSIONS[1]/2
        
        x+=vectx
        z+=vectz
        print("New x =", x)
        print("New z =", z)
        """
        view = get_tex("interface3D/img/robot.png")
        viewface = get_tex("interface3D/img/robot_face.png")
        viewback = get_tex("interface3D/img/robot_back.png")
        view_coords = ('t2f',(0,0, 1,0, 1,1, 0,1, ))
        
            
        self.rbac = batch.add(4,GL_QUADS,viewback,('v3f/dynamic',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),view_coords) # back
        self.rfro = batch.add(4,GL_QUADS,viewface,('v3f/dynamic',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),view_coords) # front
        
        self.rlef = batch.add(4,GL_QUADS,view,('v3f/dynamic',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),view_coords) # left
        self.rrig = batch.add(4,GL_QUADS,view,('v3f/dynamic',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),view_coords) # right
        
        self.rbot = batch.add(4,GL_QUADS,view,('v3f/dynamic',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),view_coords) # bottom
        self.rtop = batch.add(4,GL_QUADS,view,('v3f/dynamic',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),view_coords) # top

