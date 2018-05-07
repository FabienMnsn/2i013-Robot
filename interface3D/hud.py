from pyglet import clock, font
from pyglet.gl import *

class Hud():

    def __init__(self,window):
        self.fps = clock.ClockDisplay()
        self.helv = font.load('Helvetica', 12.0)
        self.text = font.Text(self.helv, "This text does not scale", \
                              x=0, y=0, color=(1, 1, 1, 0.5))

    def draw(self):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.text.draw()
