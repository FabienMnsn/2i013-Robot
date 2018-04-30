#imports

import pyglet
from pyglet.gl import *
from basiques.balise import *

#code

class VueBalise:
    def __init__(self, balise):
        if isinstance(balise, Balise):

            self.batch = pyglet.graphics.Batch()
            
            h=objet.l
            l=objet.l * 1.5

            # jaune
            yellow = ('c3f', (0.9, 0.9, 0,) * 4)
            # vert
            green = ('c3f', (0, 0.9, 0,) * 4)
            # rouge
            red = ('c3f', (0.9, 0, 0,) * 4)
            # bleu
            blue = ('c3f', (0, 0, 0.9,) * 4)

            #carre jaune
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x - l/2,
                        objet.y + h/2,
                        objet.z,
                        objet.x,
                        objet.y + h/2,
                        objet.z,
                        objet.x,
                        objet.y,
                        objet.z,
                        objet.x - l/2,
                        objet.y,
                        objet.z)),
                           yellow)
            #carre vert
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x,
                        objet.y + h/2,
                        objet.z,
                        objet.x + l/2,
                        objet.y + h/2,
                        objet.z,
                        objet.x + l/2,
                        objet.y,
                        objet.z,
                        objet.x,
                        objet.y,
                        objet.z)),
                           green)
            #carre bleu
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x,
                        objet.y,
                        objet.z,
                        objet.x + l/2,
                        objet.y,
                        objet.z,
                        objet.x + l/2,
                        objet.y - h/2,
                        objet.z,
                        objet.x,
                        objet.y - h/2,
                        objet.z)),
                           blue)
            #carre rouge
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x - l/2,
                        objet.y,
                        objet.z,
                        objet.x,
                        objet.y,
                        objet.z,
                        objet.x,
                        objet.y - h/2,
                        objet.z,
                        objet.x - l/2,
                        objet.y - h/2,
                        objet.z)),
                           red)
