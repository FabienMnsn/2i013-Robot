from pyglet.gl import *
import math
from composants.cube import Cube
from interface3D.model import *

def get_tex(file):
    tex = pyglet.image.load(file).texture
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MIN_FILTER,GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D,GL_TEXTURE_MAG_FILTER,GL_NEAREST)
    return pyglet.graphics.TextureGroup(tex)


class ViewSol:

    def __init__(self, batch, cube,texture_file="interface3D/img/floor.png",color=(1,1,1,)):
        view=None
        
        if texture_file != None:
            view = get_tex(texture_file)
            view_coords = ('t2f',(0,0, 10,0, 10,10, 0,10, ))
        else:
            view_coords= ('c3f',color*4)

        x,y,z = cube.x,cube.z,cube.y
        X,Y,Z = x+cube.lx, y+cube.lz, z+cube.ly

        batch.add(4,GL_QUADS,view,('v3f',(X,y,z, x,y,z, x,Y,z, X,Y,z, )),view_coords) # back
        batch.add(4,GL_QUADS,view,('v3f',(x,y,Z, X,y,Z, X,Y,Z, x,Y,Z, )),view_coords) # front
        
        batch.add(4,GL_QUADS,view,('v3f',(x,y,z, x,y,Z, x,Y,Z, x,Y,z, )),view_coords) # left
        batch.add(4,GL_QUADS,view,('v3f',(X,y,Z, X,y,z, X,Y,z, X,Y,Z, )),view_coords) # right
        
        batch.add(4,GL_QUADS,view,('v3f',(x,y,z, X,y,z, X,y,Z, x,y,Z, )),view_coords) # bottom
        batch.add(4,GL_QUADS,view,('v3f',(x,Y,Z, X,Y,Z, X,Y,z, x,Y,z, )),view_coords) # top
