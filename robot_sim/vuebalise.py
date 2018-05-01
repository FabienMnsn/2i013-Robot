#imports

import pyglet
from pyglet.gl import *
from basiques.balise import *

#code

class VueBalise:
    def __init__(self, balise):
        if isinstance(balise, Balise):

            self.batch = pyglet.graphics.Batch()
            
            h=balise.haut
            l=balise.haut * 1.5

            # jaune
            yellow = ('c3f', (0.9, 0.9, 0,) * 4)
            # vert
            green = ('c3f', (0, 0.9, 0,) * 4)
            # rouge
            red = ('c3f', (0.9, 0, 0,) * 4)
            # bleu
            blue = ('c3f', (0, 0, 0.9,) * 4)
            # noir
            white = ('c3f', (1, 1, 1,) * 4)

            #carre jaune
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x - l/2,
                        balise.y + h/2,
                        balise.z,
                        balise.x,
                        balise.y + h/2,
                        balise.z,
                        balise.x,
                        balise.y,
                        balise.z,
                        balise.x - l/2,
                        balise.y,
                        balise.z)),
                           yellow)
            #carre vert
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x,
                        balise.y + h/2,
                        balise.z,
                        balise.x + l/2,
                        balise.y + h/2,
                        balise.z,
                        balise.x + l/2,
                        balise.y,
                        balise.z,
                        balise.x,
                        balise.y,
                        balise.z)),
                           green)
            #carre bleu
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x,
                        balise.y,
                        balise.z,
                        balise.x + l/2,
                        balise.y,
                        balise.z,
                        balise.x + l/2,
                        balise.y - h/2,
                        balise.z,
                        balise.x,
                        balise.y - h/2,
                        balise.z)),
                           blue)
            #carre rouge
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x - l/2,
                        balise.y,
                        balise.z,
                        balise.x,
                        balise.y,
                        balise.z,
                        balise.x,
                        balise.y - h/2,
                        balise.z,
                        balise.x - l/2,
                        balise.y - h/2,
                        balise.z)),
                           red)

            self.batch.add(4, GL_QUADS, None, (
                'v3f', (balise.x - l/2,
                        balise.y + h/2,
                        balise.z - 0.05,
                        balise.x + l/2,
                        balise.y + h/2,
                        balise.z - 0.05,
                        balise.x + l/2,
                        balise.y - h/2,
                        balise.z - 0.05,
                        balise.x - l/2,
                        balise.y - h/2,
                        balise.z - 0.05)),
                           white)
                        
