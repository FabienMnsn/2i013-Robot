from pyglet.gl import *
from pyglet.window import key
from interface3D.model import Model
from interface3D.camera import Camera
from interface3D.hud import Hud
from strategie.simulation import Simulation
from strategie.strat70 import Strat70
from strategie.stratCarre70 import StratCarre70
from strategie.stratRotD90 import StratRotD90
from robots.rconverter import RConverter
import math

class Window(pyglet.window.Window):

    def Projection(self): glMatrixMode(GL_PROJECTION); glLoadIdentity()
    def Model(self): glMatrixMode(GL_MODELVIEW); glLoadIdentity()
    def set3D(self): self.Projection(); gluOrtho2D(0,self.width,0,self.height); self.Model()
    def set3D(self): self.Projection(); gluPerspective(70,self.width/self.height,1,100000); self.Model()

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.set_minimum_size(750,750)
        self.keys = key.KeyStateHandler()
        self.push_handlers(self.keys)
        pyglet.clock.schedule(self.on_update)
        self.camlock=False
        self.set_exclusive_mouse(self.camlock)
        self.model = Model()
        self.hud = Hud(self)
        self.camera=Camera(self,position=(-5000,-100,-5000))
        self.simul=None
    
    def on_key_press(self, KEY, MOD):
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.SPACE:
            self.camlock = not self.camlock
            self.set_exclusive_mouse(self.camlock)
        elif KEY == key.P:
            if self.simul != None:
                self.simul.arene.robot.setVitesse(self.simul.arene.robot.getVitesse()+10)
                print(self.simul.arene.robot.toString())
        elif KEY == key.M:
            if self.simul != None:
                self.simul.arene.robot.setVitesse(self.simul.arene.robot.getVitesse()-10)
                print(self.simul.arene.robot.toString())
        elif KEY == key.ENTER:
            if self.simul != None: 
                self.simul.run()
        elif KEY == key.NUM_1:
            if self.simul != None: 
                self.simul.strategie=Strat70(self.simul.arene.robot)
        elif KEY == key.NUM_2:
            if self.simul != None: 
                self.simul.strategie=StratRotD90(self.simul.arene.robot)    
        elif KEY == key.NUM_3:
            if self.simul != None: 
                self.simul.strategie=StratCarre70(self.simul.arene.robot)  
            
    def on_update(self, delta_time):
        self.camera.update(delta_time)
        if self.simul != None:
            self.simul.update(delta_time)
        
    def on_draw(self):
        self.clear()
        self.set3D()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.camera.draw()
        self.model.draw()
        self.hud.draw()
        return pyglet.event.EVENT_HANDLED

    def set_simul(self, simul):
        self.simul=simul

if __name__ == '__main__' :
    window = Window(height=1000,width=1200,caption="[Robot 2I013] - 3D View") #fullscreen=True)
    glClearColor(0.5,0.7,1,1)
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_CULL_FACE)
    window.model.addCube((0,0,-1),(1000,1000,1000),"img/cube_side.png")
    pyglet.app.run()
    
