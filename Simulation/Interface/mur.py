from pyglet.gl import *
from pyglet.window import key

class Mur:
	def __init__(self, sx,sy,sz, l,h,p):
		self.px=sx
		self.py=sy
		self.pz=sz

		self.batch = pyglet.graphics.Batch()

		#ne pas confondre ces valeurs de coordonnees qui correspondent
		#aux coordonnes pour calculer les positions des sommets
		#et les coordonnees du centre du mur qui seront utilisees plus loin
		x,y,z = l/2, h/2, p/2

		colorf1=('c3f', (0.4,0.2,0.6, )*4)				
		colorf2=('c3f', (0.5,0.2,0.0, )*4)		
		colorf3=('c3f', (0.4,0.2,0.6, )*4)		
		colorf4=('c3f', (0.5,0.2,0.0, )*4)				
		colorf6=('c3f', (0.5,0.2,0.5, )*4)		

		#creation des faces

		#f1		
		self.batch.add(4, GL_QUADS, None,('v3f', (x,-y,z, -x,-y,z, -x,y,z, x,y,z)), colorf1) #face avant
	
		#f2
		self.batch.add(4, GL_QUADS, None,('v3f', (x,-y,z, -x,-y,z, -x,-y,-z, x,-y,-z)), colorf2) #face dessous
	
		#f3	
		self.batch.add(4, GL_QUADS, None,('v3f', (x,-y,-z, -x,-y,-z , -x,y,-z, x,y,-z)), colorf3) #face arriere
	
		#f4	
		self.batch.add(4, GL_QUADS, None,('v3f', (x,y,z, -x,y,z, -x,y,-z, x,y,-z)), colorf4) #face dessus
	
		#f5	
		self.batch.add(4, GL_QUADS, None,('v3f', (x,-y,-z, x,-y,z, x,y,z, x,y,-z)), colorf6) #face cote droit
	
		#f6
		self.batch.add(4, GL_QUADS, None,('v3f', (-x,-y,-z, -x,-y,z, -x,y,z, -x,y,-z)), colorf6) #face cote gauche
		

	def draw(self):
		self.batch.draw()

#creation d'une fenetre
class Window(pyglet.window.Window):
	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		self.set_minimum_size(100,100) #securite
		
		#methodes et variables propres
		self.listcube = list()
		self.w = args[0]
		self.h = args[1]

		#methodes et variables de champ
		glClearColor(0.7,0.2,0.5,1)
        glEnable(GL_DEPTH_TEST) 
        xRotation=yRotation=30

	def addmur(self, x,y,z, h,l,p):
		self.listcube.append(Mur(x,y,z, h,l,p))
		self.on_draw()

	#definition de la methode de dessin des vues sur la fenetre
	def on_draw(self):
		# Push Matrix onto stack
		glPushMatrix()

		glRotatef(self.xRotation, 1, 0, 0) # gere les rotations
		glRotatef(self.yRotation, 0, 1, 0)

		self.clear()
		i=0
		while i<len(self.listcube):
			self.listcube[i].draw()
			i+=1

		#Pop Matrix off stack
		glPopMatrix()

	def on_resize(self, w, h):

		# set the Viewport
		glViewport(0,0,w,h)
		# width gere "l'applatissement" horizontale du cube, height le vertical
		# using Projection mode
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()

		aspectRatio = w / h
		gluPerspective(40, aspectRatio, 1, 1000) #premier argument gere le rapprochement du cube de la camera

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()
		itranslate = 0
		while itranslate<len(self.listcube):
			glTranslatef(self.listcube[itranslate].px, self.listcube[itranslate].py, -800)
			itranslate+=1 
			# (x,y,z) x gere la position horizontale de la camera, y gere sa position verticale, et z gere le zoom

	def on_key_press(self, symbol, modifiers):
		if symbol == key.UP:
			self.xRotation -= 5
		elif symbol == key.DOWN:
			self.xRotation += 5
		elif symbol == key.LEFT:
			self.yRotation -= 5
		elif symbol == key.RIGHT:
			self.yRotation += 5
		elif symbol == key.Q: #vers la gauche
			self.clear()
			i=0
			while i<len(self.listcube):	
				glTranslatef(-10, 0, 0)
				self.listcube[i].px -= 10
				i+=1		
		elif symbol == key.D: #vers la droite
			self.clear()
			i=0
			while i<len(self.listcube):		
				glTranslatef(10, 0, 0)
				self.listcube[i].px += 10
				i+=1
		elif symbol == key.Z: #vers le haut
			self.clear()
			i=0
			while i<len(self.listcube):	
				glTranslatef(0,10,0)
				self.listcube[i].py +=10
				i+=1
		elif symbol == key.S: #vers le bas
			self.clear()
			i=0
			while i<len(self.listcube):	
				glTranslatef(0,-10,0)
				self.listcube[i].py -=10
				i+=1
		elif symbol == key.P:
			self.clear()
			i=0
			while i<len(self.listcube):	
				glTranslatef(0,0,10)
				self.listcube[i].pz +=10
				i+=1	
		elif symbol == key.M:
			self.clear()
			i=0
			while i<len(self.listcube):	
				glTranslatef(0,0,-10)
				self.listcube[i].pz -=10
				i+=1

"""
#securite pour que le script ne se lance pas n importe quand
if __name__ == "__main__":
	newwindow = Window(600,500,"futuremur", resizable = False)
	newwindow.addmur(40,60,0, 400,300,100)
	#newwindow.addmur(25,50,150, 200,200,50)

	pyglet.app.run()
"""