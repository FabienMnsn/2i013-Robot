
# import

from tkinter import *
from arene import *
from basiques.cube import *
from basiques.mur import *
from basiques.sol import *
from capteur import *
from TestStrategy import *
import random
import time

# code

class Interface:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.geometry("600x700")
        self.fenetre.title("Robot 2i013 Alpha 3.1")
        self.fenetre.resizable(width=True, height=True)
        # affichage d'un texte dans la fenetre principale
        # creation frame1 -> conteneur
        frame1 = LabelFrame(self.fenetre, text="Carré gris = Arene 500 x 500px", borderwidth=2, relief=GROOVE)
        frame1.pack(side=TOP, padx=5, pady=5)
        # creation d'un canvas principal (toile ou tableau) dans la fenetre
        canvas1 = Canvas(frame1, width=500, height=500)
        canvas1.pack()

        self.fenetre.mainloop()


    def rafraichir(robot):
        canvas1.delete(ALL) 
        i = 0
        for c in robot.arene.liste_cube:
            if isinstance(c, Sol):
                dessiner_sol(c)
            if isinstance(c, Mur):
                dessiner_mur(c)
            elif isinstance(c, Cube):
                dessiner_cube(c)
        dessiner_robot(robot)
    
    def dessiner_cube(cube):
        #if isinstance(cube, Cube) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        canvas1.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="darkgrey")
        canvas1.create_text(cube.x + cube.larg / 2, cube.y + cube.long / 2, text="Cube", fill="darkgrey",activefill="black")


    def dessiner_mur(mur):
        #if isinstance(mur, Mur) and mur.x + mur.larg < arene.lx and mur.y + mur.long < arene.ly:
        canvas1.create_rectangle(mur.x, mur.y, mur.x + mur.larg, mur.y + mur.long, fill="yellow")
        canvas1.create_text(mur.x + mur.larg / 2, mur.y + mur.long / 2, text="Mur", fill="yellow", activefill="Black")


    def dessiner_sol(s1):
        canvas1.create_rectangle(s1.x, s1.y, s1.x + s1.larg, s1.y + s1.long, fill="grey")
        canvas1.create_text(s1.x + s1.larg / 2, s1.y + s1.long / 2, text="Sol", fill="grey", activefill="Black")


    def dessiner_robot(robot):
        x, y, z = robot.position
        (x0,y0), (x1,y1), (x2,y2), (x3,y3) = robot.coords
        milieu_avant_robot_xy = (((x0 + x1)/2), ((y0+y1)/2))
        long, larg, haut = robot.dimension
        dirx, diry = robot.direction
        dirtetex, dirtetey = robot.tete.orientation
        canvas1.create_polygon(robot.coords, fill="blue")
        canvas1.create_line((x0+x1)/2, (y0+y1)/2, ((x0+x1)/2 + dirtetex*3), ((y0+y1)/2 + dirtetey*3), fill="black", arrow='last')
        canvas1.create_oval(milieu_avant_robot_xy[0]-4, milieu_avant_robot_xy[1]-4, milieu_avant_robot_xy[0]+4, milieu_avant_robot_xy[1]+4, fill="red")
