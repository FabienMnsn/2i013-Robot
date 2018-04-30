#imports

import pyglet
from pyglet.gl import *
from basiques.cube import *

#code

class VueCube:
    def __init__(self, cube):
        if isinstance(cube, Cube):

            self.batch = pyglet.graphics.Batch()
            
            colorf1 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf2 = ('c3f', (0.65, 0.65, 0.65,) * 4)
            colorf3 = ('c3f', (0.6, 0.6, 0.6,) * 4)
            colorf4 = ('c3f', (0.55, 0.55, 0.55,) * 4)
            colorf5 = ('c3f', (0.5, 0.5, 0.5,) * 4)
            colorf6 = ('c3f', (0.45, 0.45, 0.45,) * 4)
            # faces
            # f1
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z + cube.haut/2)),
                           colorf1)
            # f2
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z - cube.haut/2)),
                           colorf2)
            # f3
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z - cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z - cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z - cube.haut/2)),
                           colorf3)
            # f4
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z - cube.haut/2)),
                           colorf4)
            # f5
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (cube.x + cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z - cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x + cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z - cube.haut/2)),
                           colorf5)
            # f6
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (cube.x - cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z - cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y - cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z + cube.haut/2,
                        cube.x - cube.larg/2,
                        cube.y + cube.long/2,
                        cube.z - cube.haut/2)),
                           colorf6)
