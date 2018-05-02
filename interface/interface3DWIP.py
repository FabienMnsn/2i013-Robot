#imports

import pyglet
import math

from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay

from basiques.cube import *

from robot_sim.robot2 import *
from robot_sim.vuecube import *
from robot_sim.vuerobot import *
from robot_sim.vuebalise import *
from robot_sim.vuesol import *

#code class fenetre

class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # attributs qui serviront pour la simu
        self.frame_rate = 1 / 600.0
        fps_display = FPSDisplay(self)
        fps_display.label.font_size = 20

        self.set_minimum_size(100, 100)  # securite

        # variables
        self.attributVueSol = None
        self.attributVueRobot = None
        self.listVueCube = []
        self.listVueBalise = []
        
        self.eyeX = 0
        self.eyeY = 80
        self.eyeZ = 400

        self.lookatX = 0
        self.lookatY = 0
        self.lookatZ = 0

        self.upX = 0
        self.upY = 1
        self.upZ = 0
        
        # methodes et variables de champ fenetre
        glClearColor(0.09, 0.6, 0.8, 1)

        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    xRotation = yRotation = zRotation = 22.5

    def addVueCube(self, objet):
        self.listVueCube.append(VueCube(objet))
    
    def addVueBalise(self, objet):
        self.listVueBalise.append(VueBalise(objet))

    def addVueRobot(self, objet):
        self.attributVueRobot = VueRobot(objet)

    def addVueSol(self, objet):
        self.attributVueSol = VueSol(objet)
    # definition de la methode de dessin des vues sur la fenetre
    def on_draw(self):
        # type: () -> object
        # Push Matrix onto stack
        #glEnable(GL_TEXTURE_2D) 
        glPushMatrix()
        self.clear()

        for i in self.listVueCube:
            i.batch.draw()

        for j in self.listVueBalise:
            j.batch.draw()
            
        if (self.attributVueRobot != None):
            self.attributVueRobot.batch.draw()
            
        if (self.attributVueSol != None):
            self.attributVueSol.batch.draw()

        # Pop Matrix off stack
        glPopMatrix()

    def on_resize(self, w, h):

        # set the Viewport
        glViewport(0, 0, w, h)
        # width gere "l'applatissement" horizontale du cube, height le vertical
        # using Projection mode
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspectRatio = w / h
        gluPerspective(50, aspectRatio, 1, 4000)
        
        gluLookAt(
            self.eyeX, self.eyeY, self.eyeZ,  # eye
            self.lookatX, self.lookatY, self.lookatZ,  # lookAt
            self.upX, self.upY, self.upZ)  # up
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def on_key_press(self, symbol, modifiers):
        
        if symbol == key.LEFT:
            glRotatef(self.yRotation, 0, 1, 0)
            
        elif symbol == key.RIGHT:
            glRotatef(-self.yRotation, 0, 1, 0)

        elif symbol == key.SPACE:
            print(self.eyeX, self.eyeY, self.eyeZ, "|", self.upX, self.upY, self.upZ)
        
        elif symbol == key.P:
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, 0, self.INDTRSLT)
                self.listcube[i].pz += self.INDTRSLT
                i += 1
        elif symbol == key.M:
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, 0, -self.INDTRSLT)
                self.listcube[i].pz -= self.INDTRSLT
                i += 1

        # action screenshot
        elif symbol == key.V:

            pyglet.image.get_buffer_manager().get_color_buffer().save('screen.png')

            
if __name__ == "__main__":
    newwindow = Window(720, 480, "Arene Virtuelle", resizable=False)
    #la taille de la fenetre est importante pour le screenshot et le traitement d'image potentiels bugs...
    #C = Cube(0,0,0,400,300,20,1)

    newwindow.addcube(0, 0, 0, 10000, 0, 20000,3) #SOL
    #newwindow.addcube(0, 0, 0, 400, 300, 20,1)
    #newwindow.addcube(200, 0, 200, 20, 300, 400,4)
    #newwindow.addcube(200, 0, 600, 20, 300, 400,1)
    newwindow.addcube(0, 25, 50, 50, 50, 50, 2) #robot
    newwindow.addbalise(0, 50, 0, 100, "f")  # pour les mur de face en z
    newwindow.addbalise(-100, 50, 200, 100, "c")
    
    pyglet.clock.schedule_interval(newwindow.update, newwindow.frame_rate)
    pyglet.app.run()

# ps: lien utile: http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/graphics.html

