from pyglet.gl import *
from pyglet.window import key
from interface3D.model import Model
from interface3D.camera import Camera
from interface3D.hud import Hud
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
        self.camera=Camera(self)
    
    def on_key_press(self, KEY, MOD):
        if KEY == key.ESCAPE:
            self.close()
        elif KEY == key.SPACE:
            self.camlock = not self.camlock
            self.set_exclusive_mouse(self.camlock)
            
    def on_update(self, delta_time):
        self.camera.update(delta_time)
        
    def on_draw(self):
        self.clear()
        self.set3D()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.camera.draw()
        self.model.draw()
        self.hud.draw()
        return pyglet.event.EVENT_HANDLED

if __name__ == '__main__' :
    window = Window(height=1000,width=1200,caption="[Robot 2I013] - 3D View") #fullscreen=True)
    glClearColor(0.5,0.7,1,1)
    glEnable(GL_DEPTH_TEST)
    #glEnable(GL_CULL_FACE)
    window.model.addCube((0,0,-1),(1000,1000,1000),"img/cube_side.png")
    pyglet.app.run()
    
