from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay


class Cube:
    def __init__(self, sx, sy, sz, l, h, p, setcolor):
        #initialisation des coordonnees de l objet
        self.px = sx
        self.py = sy
        self.pz = sz
        #initialisation des dimensions de l objet
        self.cl=l
        self.ch=h
        self.cp=p

        self.type=setcolor

        self.batch = pyglet.graphics.Batch()

        # ne pas confondre ces valeurs de coordonnees qui correspondent
        # aux coordonnes pour calculer les positions des sommets
        # et les coordonnees du centre du mur qui seront utilisees plus loin
        x, y, z = self.px, self.py, self.pz
        lm, hm, pm = self.cl / 2, self.ch / 2, self.cp / 2

        #setcolor murs
        if(setcolor==1):
            colorf1 = ('c3f', (0.6, 0.6, 0.6,) * 4)
            colorf2 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf3 = ('c3f', (0.7, 0.7, 0.7,) * 4)
            colorf4 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf5 = ('c3f', (0.5, 0.5, 0.5,) * 4)
            colorf6 = ('c3f', (0.5, 0.5, 0.5,) * 4)
        """
        #setcolor cubes
        if(setcolor==2):
            colorf1 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf2 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf3 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf4 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf5 = ('c3f', (0.8, 0.8, 0.8,) * 4)
            colorf6 = ('c3f', (0.8, 0.8, 0.8,) * 4)
        """
        #setcolor robot
        if (setcolor == 3):
            colorf1 = ('c3f', (0.4, 0., 0.3,) * 4)
            colorf2 = ('c3f', (0.5, 0., 0.4,) * 4)
            colorf3 = ('c3f', (0.5, 0., 0.4,) * 4)
            colorf4 = ('c3f', (0.6, 0., 0.5,) * 4)
            colorf5 = ('c3f', (0.6, 0., 0.5,) * 4)
            colorf6 = ('c3f', (0.5, 0., 0.4,) * 4)

        #setcolor Sol
        if (setcolor == 4):
            colorf1 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf2 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf3 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf4 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf5 = ('c3f', (0.4, 0.4, 0.4,) * 4)
            colorf6 = ('c3f', (0.4, 0.4, 0.4,) * 4)

        # creation des faces
        
        # f1
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z + pm, x - lm, y - hm, z + pm, x - lm, y + hm, z + pm, x + lm, y + hm, z + pm)),
                       colorf1)
        # face avant
        
        # f2
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z + pm, x - lm, y - hm, z + pm, x - lm, y - hm, z - pm, x + lm, y - hm, z - pm)),
                       colorf2)
        # face dessous
        
        # f3
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z - pm, x - lm, y - hm, z - pm, x - lm, y + hm, z - pm, x + lm, y + hm, z - pm)),
                       colorf3)
        # face arriere
        
        # f4
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y + hm, z + pm, x - lm, y + hm, z + pm, x - lm, y + hm, z - pm, x + lm, y + hm, z - pm)),
                       colorf4)
        # face dessus
        
        # f5
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x + lm, y - hm, z - pm, x + lm, y - hm, z + pm, x + lm, y + hm, z + pm, x + lm, y + hm, z - pm)),
                       colorf5)
        # face cote droit
        
        #(x + lm, y - hm, z - pm, x + lm, y + hm, z + pm, x + lm, y + hm, z + pm, x + lm, y + hm, z - pm))
        
        # f6
        self.batch.add(4, GL_QUADS, None, (
        'v3f', (x - lm, y - hm, z - pm, x - lm, y - hm, z + pm, x - lm, y + hm, z + pm, x - lm, y + hm, z - pm)),
                       colorf6)
        # face cote gauche
        
    def draw(self):
        self.batch.draw()

    def update_object(self):
        if self.type==3:
            self.pz+=10



# creation d'une fenetre
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        #attributs qui serviront pour la simu
        self.frame_rate = 1/600.0
        fps_display= FPSDisplay(self)
        fps_display.label.font_size=20

        self.set_minimum_size(100, 100)  # securite

        # methodes et variables propres
        self.listcube = list()
        #self.listrobot = list()
        self.w = args[0]
        self.h = args[1]
        self.INDROT = 10

        # methodes et variables de champ fenetre
        glClearColor(0.7, 0.2, 0.5, 1)

        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    xRotation = yRotation = zRotation = 30

    #methodes pour le rafraichissement de l affichage du robot
    def update(self, dt):
        for e in self.listcube:
            e.update_object()


    def addcube(self, x, y, z, h, l, p, setcolor):
        self.listcube.append(Cube(x, y, z, h, l, p, setcolor))
        self.on_draw()

    # definition de la methode de dessin des vues sur la fenetre
    def on_draw(self):
        # type: () -> object
        # Push Matrix onto stack
        glPushMatrix()

        glRotatef(self.xRotation, 1, 0, 0)  # gere les rotations
        glRotatef(self.yRotation, 0, 1, 0)

        self.clear()
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
        for o in self.listcube:
            if o.type == 3:
                #glTranslatef(o.px, o.py, o.pz-(o.cp/2))
                gluLookAt(
                    o.px, o.py, o.pz,  # eye
                    200.0, 0.0, 200.0, # lookAt
                    0.0, 1.0, 0.0)  # up

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        # while it<len(self.listcube):
        # glTranslatef(self.listcube[0].px, self.listcube[0].py, -500)
        # it+=1
        # (x,y,z) x gere la position horizontale de la camera, y gere sa position verticale, et z gere le zoom

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.xRotation -= self.INDROT
        elif symbol == key.DOWN:
            self.xRotation += self.INDROT
        elif symbol == key.LEFT:
            self.yRotation -= self.INDROT
        elif symbol == key.RIGHT:
            self.yRotation += self.INDROT
        elif symbol == key.Q:  # vers la gauche
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(-10, 0, 0)
                self.listcube[i].px -= 10
                i += 1
        elif symbol == key.D:  # vers la droite
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(10, 0, 0)
                self.listcube[i].px += 10
                i += 1
        elif symbol == key.Z:  # vers le haut
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, 10, 0)
                self.listcube[i].py += 10
                i += 1
        elif symbol == key.S:  # vers le bas
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, -10, 0)
                self.listcube[i].py -= 10
                i += 1
        elif symbol == key.P:
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, 0, 10)
                self.listcube[i].pz += 10
                i += 1
        elif symbol == key.M:
            self.clear()
            i = 0
            while i < len(self.listcube):
                glTranslatef(0, 0, -10)
                self.listcube[i].pz -= 10
                i += 1
        

# securite pour que le script ne se lance pas n importe quand
if __name__ == "__main__":
    newwindow = Window(1280, 720, "Arena", resizable=False)
    #newwindow.addcube(0, 200, 0, 400, 400, 20,1)
    #newwindow.addcube(200, 200, 200, 20, 400, 400,4)
    #newwindow.addcube(200, 200, 600, 20, 400, 400,1)
    #newwindow.addcube(0, 25, 200, 50, 50, 50, 3)

    pyglet.clock.schedule_interval(newwindow.update, newwindow.frame_rate)
    pyglet.app.run()


# ps: lien utile: http://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/graphics.html
