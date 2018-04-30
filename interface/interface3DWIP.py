#imports

import pyglet
import math
from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay
from robot_sim.robot2 import *
from basiques.cube import *

#code

class Cube:
    def __init__(self, objet):
    #def __init__(self, sx, sy, sz, l, h, p, setcolor):
        self.batch = pyglet.graphics.Batch()

        if isinstance(objet, Robot):
            print("creation robot")
            colorf1 = ('c3f', (1., 1., 1.,) * 4)
            colorf2 = ('c3f', (0.95, 0.95, 0.95,) * 4)
            colorf3 = ('c3f', (0.90, 0.90, 0.90,) * 4)
            colorf4 = ('c3f', (0.85, 0.85, 0.85,) * 4)
            colorf5 = ('c3f', (0.80, 0.80, 0.80,) * 4)
            colorf6 = ('c3f', (0.75, 0.75, 0.75,) * 4)

            # creation des faces
            # f1
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2)),
                           colorf1)
            # face avant

            # f2
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2,
                        objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2)),
                           colorf2)
            # face dessous

            # f3
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2,
                        objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2)),
                           colorf3)
            # face arriere

            # f4
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2,
                        objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2)),
                           colorf4)
            # face dessus

            # f5
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2,
                        objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] + objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2)),
                           colorf5)
            # face cote droit

            # f6
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] - objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] + objet.getDimension()[2]/2,
                        objet.getPosition()[0] - objet.getDimension()[0]/2,
                        objet.getPosition()[1] + objet.getDimension()[1]/2,
                        objet.getPosition()[2] - objet.getDimension()[2]/2)),
                           colorf6)
            # face cote gauche
            
        elif isinstance(objet, Mur):
            print("creation mur")
            # initialisation des coordonnees de l objet
            """self.px = sx
            self.py = sy
            self.pz = sz
            # initialisation des dimensions de l objet
            self.cl = l
            self.ch = h
            self.cp = p

            self.type = setcolor

            self.batch = pyglet.graphics.Batch()

            # ne pas confondre ces valeurs de coordonnees qui correspondent
            # aux coordonnes pour calculer les positions des sommets
            # et les coordonnees du centre du mur qui seront utilisees plus loin
            x, y, z = self.px, self.py, self.pz
            lm, hm, pm = self.cl / 2, self.ch / 2, self.cp / 2
            
            # setcolor murs
            if (setcolor == 1):
                colorf1 = ('c3f', (0.6, 0.6, 0.6,) * 4)
                colorf2 = ('c3f', (0.7, 0.7, 0.7,) * 4)
                colorf3 = ('c3f', (0.7, 0.7, 0.7,) * 4)
                colorf4 = ('c3f', (0.8, 0.8, 0.8,) * 4)
                colorf5 = ('c3f', (0.5, 0.5, 0.5,) * 4)
                colorf6 = ('c3f', (0.5, 0.5, 0.5,) * 4)

            # setcolor robot
            if (setcolor == 2):
                colorf1 = ('c3f', (1., 1., 1.,) * 4)
                colorf2 = ('c3f', (0.95, 0.95, 0.95,) * 4)
                colorf3 = ('c3f', (0.90, 0.90, 0.90,) * 4)
                colorf4 = ('c3f', (0.85, 0.85, 0.85,) * 4)
                colorf5 = ('c3f', (0.80, 0.80, 0.80,) * 4)
                colorf6 = ('c3f', (0.75, 0.75, 0.75,) * 4)

            # setcolor Sol
            if (setcolor == 3):
                colorf1 = ('c3f', (0.7, 0.7, 0.7,) * 4)
                colorf2 = ('c3f', (0.7, 0.7, 0.7,) * 4)
                colorf3 = ('c3f', (0.7, 0.7, 0.7,) * 4)
                colorf4 = ('c3f', (0.7, 0.7, 0.7,) * 4)
                colorf5 = ('c3f', (0.7, 0.7, 0.7,) * 4)
                colorf6 = ('c3f', (0.7, 0.7, 0.7,) * 4)

            if (setcolor == 4):  # rouge ~> jaune
                colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0.9, 0.9, 0,) * 4)
            if (setcolor == 5):  # vert
                colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0, 0.9, 0,) * 4)
            if (setcolor == 6):  # bleu ~> rouge
                colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0.9, 0, 0,) * 4)
            if (setcolor == 7):  # jaune ~> bleu
                colorf1 = colorf2 = colorf3 = colorf4 = colorf5 = colorf6 = ('c3f', (0, 0, 0.9,) * 4)
            """
            colorf1 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf2 = ('c3f', (0.65, 0.65, 0.65,) * 4)
            colorf3 = ('c3f', (0.6, 0.6, 0.6,) * 4)
            colorf4 = ('c3f', (0.55, 0.55, 0.55,) * 4)
            colorf5 = ('c3f', (0.5, 0.5, 0.5,) * 4)
            colorf6 = ('c3f', (0.45, 0.45, 0.45,) * 4)

            # creation des faces
            # f1
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x + objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x + objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z + objet.haut/2)),
                           colorf1)
            # face avant

            # f2
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x + objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z - objet.haut/2,
                        objet.x + objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z - objet.haut/2)),
                           colorf2)
            # face dessous

            # f3
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x + objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z - objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z - objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z - objet.haut/2,
                        objet.x + objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z - objet.haut/2)),
                           colorf3)
            # face arriere

            # f4
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x + objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z - objet.haut/2,
                        objet.x + objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z - objet.haut/2)),
                           colorf4)
            # face dessus

            # f5
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x + objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z - objet.haut/2,
                        objet.x + objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x + objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x + objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z - objet.haut/2)),
                           colorf5)
            # face cote droit

            # f6
            self.batch.add(4, GL_QUADS, None, (
                'v3f', (objet.x - objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z - objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y - objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z + objet.haut/2,
                        objet.x - objet.larg/2,
                        objet.y + objet.long/2,
                        objet.z - objet.haut/2)),
                           colorf6)
            # face cote gauche
        elif isinstance(objet, Balise):
            print("creation balise")
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
        else:
            print("Erreur : objet de type inconnu")
    
            
    def draw(self):
        self.batch.draw()

    #def update_object(self):
        #if self.type == 3:
            #self.pz += 10


class Balise:
    def __init__(self, x, y, z, sizeL, orientation):
        self.x = x
        self.y = y
        self.z = z
        self.l = sizeL
        self.face = orientation
        

        """    
            while i <= 7:
                if i == 4:
                    self.cubesbalisel.append(Cube(bpx, bpy + (size / 4), bpz - (size / 4), 2, size / 2, size / 2, i))
                elif i == 5:
                    self.cubesbalisel.append(Cube(bpx, bpy + (size / 4), bpz + (size / 4), 2, size / 2, size / 2, i))
                elif i == 6:
                    self.cubesbalisel.append(Cube(bpx, bpy - (size / 4), bpz - (size / 4), 2, size / 2, size / 2, i))
                elif i == 7:
                    self.cubesbalisel.append(Cube(bpx, bpy - (size / 4), bpz + (size / 4), 2, size / 2, size / 2, i))
                i += 1
        else:
            while i <= 7:
                if i == 4:
                    self.cubesbalisel.append(Cube(bpx - (size / 4), bpy + (size / 4), bpz, size / 2, size / 2, 2, i))
                elif i == 5:
                    self.cubesbalisel.append(Cube(bpx + (size / 4), bpy + (size / 4), bpz, size / 2, size / 2, 2, i))
                elif i == 6:
                    self.cubesbalisel.append(Cube(bpx - (size / 4), bpy - (size / 4), bpz, size / 2, size / 2, 2, i))
                elif i == 7:
                    self.cubesbalisel.append(Cube(bpx + (size / 4), bpy - (size / 4), bpz, size / 2, size / 2, 2, i))
                i += 1
        """
        



# creation d'une fenetre
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # attributs qui serviront pour la simu
        self.frame_rate = 1 / 600.0
        fps_display = FPSDisplay(self)
        fps_display.label.font_size = 20

        self.set_minimum_size(100, 100)  # securite

        # methodes et variables propres

        self.obj_robot = None
        self.listcube = list()
        self.balise = None
        
        # self.listrobot = list()
        self.w = args[0]
        self.h = args[1]
        self.INDROT = 2
        self.INDTRSLT = 20

        #variables de gestion de la vue (glulookat)
        self.eyeX = 0
        self.eyeY = 0
        self.eyeZ = 400

        self.lookatX = 0
        self.lookatY = 0
        self.lookatZ = 0

        self.upX = 0
        self.upY = 1
        self.upZ = 0
        
        # methodes et variables de champ fenetre
        glClearColor(0.7, 0.2, 0.5, 1)

        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    xRotation = yRotation = zRotation = 22.5

    # methodes pour le rafraichissement de l affichage du robot
    #def update(self, dt):
        #for e in self.listcube:
            #e.update_object()

    def addcube(self, objet):
        self.listcube.append(Cube(objet))
        self.on_draw()
    
    def addbalise(self, balise):
        self.balise = Cube(balise)
        #self.listcube = self.listcube + balise.cubesbalisel

    def addrobot(self, robot):
        #maj du robot
        self.obj_robot = Cube(robot)
        
    # definition de la methode de dessin des vues sur la fenetre
    def on_draw(self):
        # type: () -> object
        # Push Matrix onto stack
        glPushMatrix()
        
        self.clear()
        #self.balise.draw()
        self.obj_robot.draw()
        i = 0
        while i < len(self.listcube):
            self.listcube[i].draw()
            i += 1

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
        # premier argument gere le rapprochement du cube de la camera

        # repositionnement de la camera par rapport au robot
        #eyex, eyey, eyez = 0, 70, 70
        #visex, visey, visez = 0, 0, 0
        #for o in self.listcube:
            #if isinstance(o, Robot):
                # glTranslatef(o.px, o.py, o.pz-(o.cp/2))
                #eyex, eyey, eyez = o.px, o.py, o.pz - (o.cp / 2)
                #visex, visey, visez = o.px, o.py, o.pz - o.cl
        """gluLookAt(
            eyex, eyey, eyez,  # eye
            visex, visey, visez,  # lookAt
            0.0, 1.0, 0.0)  # up
        """
        #vue temporaire pour voir larene des le debut
        #eyeX, eyeY, eyeZ = 0, 100, 400
        #lookatX, lookaty, lookatZ = 0, 0, 0
        
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

        elif symbol ==key.SPACE:
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

