#imports

import pyglet
import math

from pyglet.gl import *
from pyglet.window import key
from pyglet.window import FPSDisplay

from basiques.cube import *

from strategies.strategieToutDroit70 import *
from strategies.strategieRot90 import *
from strategies.strategieRot_90 import *
from strategies.simulation import *

from images.traitementimage import *
from robot_sim.robot2 import *
from robot_sim.vuecube import *
from robot_sim.vuerobot import *
from robot_sim.vuebalise import *
from robot_sim.vuesol import *
from robot_sim.vuemur import *
from robot_sim.utilitaires_geometrie import *

#code

#___________________________________________CLASS WINDOW___________________________________________
class Window(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)
        # attributs qui serviront pour la simu
        self.frame_rate = 1 / 600.0
        #fps_display = FPSDisplay(self)
        #fps_display.label.font_size = 20
        
        #variable de temps
        self.delta_update = 0.1

        pyglet.clock.schedule_interval(self.on_update, self.delta_update)
        self.time = 0
        self.set_minimum_size(100, 100)  # securite

        # variables d'objet
        self.attributVueSol = None
        self.attributVueRobot = None
        self.listVueCube = []
        self.listVueBalise = []

        #variables de strategie/simulation
        self.strat = None
        
        #variables de camera
        self.eyeX = 0
        self.eyeY = 10
        self.eyeZ = 400

        self.lookatX = 0
        self.lookatY = 80
        self.lookatZ = 0

        self.upX = 0
        self.upY = 1
        self.upZ = 0
        
        self.eye = (0,80,400)
        self.lookat = (0,0,0)
        self.up = (0,1,0)
        
        # methodes et variables de champ fenetre
        glClearColor(0.09, 0.6, 0.8, 1)
        glEnable(GL_DEPTH_TEST)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
    xRotation = yRotation = zRotation = 22.5

#___________________________________________ADDVUE & ADD STRAT___________________________________________
    def addVueCube(self, objet):
        self.listVueCube.append(VueCube(objet))
    
    def addVueBalise(self, objet):
        self.listVueBalise.append(VueBalise(objet))

    def addVueRobot(self, objet):
        self.attributVueRobot = VueRobot(objet)

    def addVueSol(self, objet):
        self.attributVueSol = VueSol(objet)

    def addVueMur(self, objet):
        self.listVueCube.append(VueMur(objet))

    def addVueArene(self, arene):
        if isinstance(arene, Arene):
            for i in arene.liste_cube:
                if isinstance(i, Mur):
                    self.addVueMur(i)
                elif isinstance(i, Sol):
                    self.addVueSol(i)
                elif isinstance(i, Cube):
                    self.addVueCube(i)

    def addStrat(self, strategie):
            self.strat = strategie

#___________________________________________UPDATE___________________________________________
    def on_update(self, dt):
        self.time += dt
        #print(self.time)
        if (self.attributVueRobot != None and self.strat != None and self.strat.stop == False):
            #print("perimetre roue (mm)",self.attributVueRobot.robot.WHEEL_CIRCUMFERENCE)
            #print("cercle rotation (mm)",self.attributVueRobot.robot.WHEEL_BASE_CIRCUMFERENCE)
            self.strat.update()
            self.addVueRobot(self.strat.robot)
            #print("(%.0f, %.0f, %.0f)"%(self.attributVueRobot.robot.position[0],self.attributVueRobot.robot.position[1],self.attributVueRobot.robot.position[2]))
            """print("(%.0f,%.0f,%.0f),(%.0f,%.0f,%.0f)centre=(%.0f, %.0f)"
                  %(self.attributVueRobot.robot.coords[0][0],
                    self.attributVueRobot.robot.coords[0][1],
                    self.attributVueRobot.robot.coords[0][2],
                    self.attributVueRobot.robot.coords[1][0],
                    self.attributVueRobot.robot.coords[1][1],
                    self.attributVueRobot.robot.coords[1][2],
                    self.attributVueRobot.robot.position[0],
                    self.attributVueRobot.robot.position[2]))
                    self.attributVueRobot.robot.coords[2][0],
                    self.attributVueRobot.robot.coords[2][1],
                    self.attributVueRobot.robot.coords[2][2],
                    self.attributVueRobot.robot.coords[3][0],
                    self.attributVueRobot.robot.coords[3][1],
                    self.attributVueRobot.robot.coords[3][2],
                    self.attributVueRobot.robot.coords[4][0],
                    self.attributVueRobot.robot.coords[4][1],
                    self.attributVueRobot.robot.coords[4][2],
                    self.attributVueRobot.robot.coords[5][0],
                    self.attributVueRobot.robot.coords[5][1],
                    self.attributVueRobot.robot.coords[5][2],
                    self.attributVueRobot.robot.coords[6][0],
                    self.attributVueRobot.robot.coords[6][1],
                    self.attributVueRobot.robot.coords[6][2],
                    self.attributVueRobot.robot.coords[7][0],
                    self.attributVueRobot.robot.coords[7][1],
                    self.attributVueRobot.robot.coords[7][2]))
            print(self.attributVueRobot.robot.direction)
            """
            #mise a jour de la camera
            self.eye = ( self.attributVueRobot.robot.position[0],
                         self.attributVueRobot.robot.dimension[1],
                         self.attributVueRobot.robot.position[2])

            self.lookat = ( ((self.attributVueRobot.robot.coords[4][0]+self.attributVueRobot.robot.coords[5][0])/2),
                           self.attributVueRobot.robot.dimension[1]+50,
                            ((self.attributVueRobot.robot.coords[4][2]+self.attributVueRobot.robot.coords[5][2])/2))

            self.up = (0,1,0)

            #DEBUT DE LA PARTIE MAGIQUE
            w,h = self.get_size()
            glViewport(0, 0, w, h)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            aspectRatio = w / h
            gluPerspective(50, aspectRatio, 1, 100000)
            
            gluLookAt(
                self.eye[0], self.eye[1]+40, self.eye[2],  # eye
                self.lookat[0], self.lookat[1], self.lookat[2],  # lookAt
                self.up[0], self.up[1], self.up[2])  # up
            
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            #FIN DE LA PARTIE MAGIQUE xD
        
#___________________________________________DRAW___________________________________________
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

#___________________________________________RESIZE___________________________________________    
    def on_resize(self, w, h):
        
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        aspectRatio = w / h
        gluPerspective(50, aspectRatio, 1, 100000)
        
        gluLookAt(
            self.eye[0], self.eye[1]+40, self.eye[2],  # eye
            self.lookat[0], self.lookat[1], self.lookat[2],  # lookAt
            self.up[0], self.up[1], self.up[2])  # up
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
#___________________________________________KEYBOARD BINDING___________________________________________    
    def on_key_press(self, symbol, modifiers):
        
        vitesse = 30
        #ne sert plus a rien on peut controler le robot directement avec les differentes strategies
        """if symbol == key.Z:
            robot = self.attributVueRobot.robot
            #print(robot.position)
            robot.direction = (0,1)
            robot.set_motor_dps(3,vitesse)
            (x,y,z) = robot.position
            #print(robot.direction)
            robot.calcul_coords() # fonction qui calcule et assigne directement le resultat du calcul a l attribut coords du robot
            #print(robot.coords)
            self.addVueRobot(robot)
            
        elif symbol == key.S:
            robot = self.attributVueRobot.robot
            #print(robot.direction)
            robot.direction = (0,-1)
            robot.set_motor_dps(3,vitesse)
            (x,y,z) = robot.position
            #print(robot.direction)
            robot.calcul_coords() # fonction qui calcule et assigne directement le resultat du calcul a l attribut coords du robot
            self.addVueRobot(robot)

        elif symbol == key.Q:
            robot = self.attributVueRobot.robot
            #print(robot.direction)
            robot.direction = (-1,0)
            robot.set_motor_dps(3,vitesse)
            (x,y,z) = robot.position
            #print(robot.direction)
            robot.calcul_coords() # fonction qui calcule et assigne directement le resultat du calcul a l attribut coords du robot
            self.addVueRobot(robot)
        
        elif symbol == key.D:
            robot = self.attributVueRobot.robot
            #print(robot.direction)
            robot.direction = (1,0)
            robot.set_motor_dps(3,vitesse)
            (x,y,z) = robot.position
            #print(robot.direction)
            robot.calcul_coords() # fonction qui calcule et assigne directement le resultat du calcul a l attribut coords du robot
            self.addVueRobot(robot)"""
#___________________________________________CLOSE & MVT CAMERA___________________________________________
        if symbol == key.RIGHT:
            glRotatef(-self.yRotation, 0, 1, 0)

        elif symbol == key.LEFT:
            glRotatef(self.yRotation, 0, 1, 0)

        elif symbol == key.SPACE: # Pertmet d'arreter le robot
 
            robot = self.attributVueRobot.robot
            stop_robot = stop(robot)
            self.addStrat(stop_robot)
                      
        elif symbol == key.ESCAPE:
            self.close()

#___________________________________________BINDS STRATEGIES___________________________________________
        elif symbol == key.G :
            robot = self.attributVueRobot.robot
            strat70 = strategieToutDroit70(robot)
            self.addStrat(strat70)

        elif symbol == key.F:
            print("debut strategie Rotation90")
            robot = self.attributVueRobot.robot
            strat90 = strategieRot_90(robot)
            self.addStrat(strat90)

            
        elif symbol == key.H:
            print("debut strategie Rotation90")
            robot = self.attributVueRobot.robot
            strat90 = strategieRot90(robot)
            self.addStrat(strat90)

        elif symbol == key.X: # detecte si il y a une balise ou non dans le champ de vision du robot
            pyglet.image.get_buffer_manager().get_color_buffer().save('screen.jpg')
            balise = traitement_image('screen')
            if balise == -1 :
                print('Aucune balise detectee')
            else :
                print('Balise detectee',balise)
                robot = self.attributVueRobot.robot
                robot.direction = (0,-1)
                robot.set_motor_dps(3,vitesse)
                (x,y,z) = robot.position
                robot.rotation_bis(0)
                self.addVueRobot(robot)

            
