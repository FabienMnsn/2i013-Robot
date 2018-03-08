#-*- coding: utf-8 -*-

import pyglet
from Tkinter import *
#from interfaceGraphique import rafraichir
from interface.featuresGL import *
from structures.robot import *
from basiques.cube import *
from structures.arene import *
from basiques.cube import *
from basiques.mur import *
from basiques.sol import *
from structures.capteur import *

from save.saveJson import *
from save.csvToJson import *
import random
import time

#methodes dessin 2D -------

def dessiner_robot(robot):
    x, y, z = robot.position
    (x0,y0), (x1,y1), (x2,y2), (x3,y3) = robot.coords
    milieu_avant_robot_xy = (((x0 + x1)/2), ((y0+y1)/2))
    long, larg, haut = robot.dimension
    dirx, diry = robot.direction
    dirtetex, dirtetey = robot.tete.orientation
    #print( dirtetex, dirtetey)
    #print("robot.coords",robot.coords)
    canvas1.create_polygon(robot.coords, fill="blue")
    #canvas1.create_text(x + larg / 2, y + long / 2, text="Robot", fill="blue", activefill="black")

    # creation d'une fleche indiquant la direction du robot
    canvas1.create_line((x0+x1)/2, (y0+y1)/2, ((x0+x1)/2 + dirtetex*3), ((y0+y1)/2 + dirtetey*3), fill="black", arrow='last')
    canvas1.create_oval(milieu_avant_robot_xy[0]-4, milieu_avant_robot_xy[1]-4, milieu_avant_robot_xy[0]+4, milieu_avant_robot_xy[1]+4, fill="red")

def dessiner_sol(s1):
    canvas1.create_rectangle(s1.x, s1.y, s1.x + s1.larg, s1.y + s1.long, fill="grey")
    canvas1.create_text(s1.x + s1.larg / 2, s1.y + s1.long / 2, text="Sol", fill="grey", activefill="Black")


def rafraichir(arene):
    canvas1.delete(ALL)

    i = arene.liste_cube[0]
    dessiner_sol(i)

    if (len(arene.liste_robot) == 1):
        # print(arene.liste_robot[0].tete.orientation)
        dessiner_robot(arene.liste_robot[0])
        # print("R.rafrai.",arene.liste_robot[0].position)

    for c in arene.liste_cube:
        # if isinstance(c, Sol):
        # dessiner_sol(c)
        if isinstance(c, Mur):
            dessiner_mur(c, arene)
        elif isinstance(c, Cube):
            dessiner_cube(c, arene)

def dessiner_cube(cube, arene):
    if isinstance(cube, Cube) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        canvas1.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="darkgrey")
        canvas1.create_text(cube.x + cube.larg / 2, cube.y + cube.long / 2, text="Cube", fill="darkgrey",
                            activefill="black")

def dessiner_mur(mur, arene):
    if isinstance(mur, Mur) and mur.x + mur.larg < arene.lx and mur.y + mur.long < arene.ly:
        canvas1.create_rectangle(mur.x, mur.y, mur.x + mur.larg, mur.y + mur.long, fill="yellow")
        canvas1.create_text(mur.x + mur.larg / 2, mur.y + mur.long / 2, text="Mur", fill="yellow", activefill="Black")


def rafraichir(arene):
    canvas1.delete(ALL)

    i = arene.liste_cube[0]
    dessiner_sol(i)

    if (len(arene.liste_robot) == 1):
        # print(arene.liste_robot[0].tete.orientation)
        dessiner_robot(arene.liste_robot[0])
        # print("R.rafrai.",arene.liste_robot[0].position)

    for c in arene.liste_cube:
        # if isinstance(c, Sol):
        # dessiner_sol(c)
        if isinstance(c, Mur):
            dessiner_mur(c, arene)
        elif isinstance(c, Cube):
            dessiner_cube(c, arene)

# script deplacement robot ------
if __name__ == "__main__":
    # creation arene + robot
    arena = Creation_Arene()
    sol = Creation_Sol(arena)

    # iRobot = Robot((50,50,0),(0,0,0,0), (50,100), (20,20,20),1)
    iRobot = Creation_Robot(arena)
    iRobot.toString()
    arena.ajouter_robot(iRobot)
    arena.ajouter_cube(sol)

    #entree clavier du mode d affichage
    mode = ""
    while(mode!="stop"):
        mode = raw_input("Veuillez rentrer le mode d'affichage:")

        # affichage
        # dans le terminal
        if mode == "-t":
            print(arena.liste_robot[0].toString())
            fx, fy, fz = iRobot.getPosition()
            sleep=0.2
            fy=fy+50
            fx=fx-50
            while(True):
                tx, ty, tz = arena.liste_robot[0].getPosition()
                while(ty<fy):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    time.sleep(sleep)
                    arena.afficher()
                iRobot.rotation_bis(90)
                while(tx>fx):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    time.sleep(sleep)
                    arena.afficher()
                fx = fx+50
                fy = fy-50
                iRobot.rotation_bis(90)
                while(ty>fy):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    time.sleep(sleep)
                    arena.afficher()
                iRobot.rotation_bis(90)
                while(tx<fx):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    time.sleep(sleep)
                    arena.afficher()
                break

        #dans une fenetre
        if mode =="-3D":
            aWindow = Window(500,500,"new world", resizable=False)
            rx,ry,rz = iRobot.getPosition()
            rl, rw, rh = iRobot.getDimension()
            aWindow.addcube(rx, ry, rz, rl, rw, rh, 2)

            pyglet.app.run()

        #dans fenetre 2D tkinter
        if mode == "-2D":
            fenetre = Tk()
            fenetre.geometry("500x500")
            fenetre.title("new world")
            fenetre.resizable(width=True, height=True)
            # --- VUES ---
            # creation frame1 -> conteneur
            frame1 = LabelFrame(fenetre, text="Carré gris = Arene 500 x 500px", borderwidth=2, relief=GROOVE)
            frame1.pack(side=TOP, padx=5, pady=5)

            # creation frame2 ~> conteneur message erreur
            frame2 = LabelFrame(fenetre, text="Informations", borderwidth=2, relief=GROOVE)
            frame2.pack(side=TOP, padx=5, pady=5)

            # creation d'un canvas principal (toile ou tableau) dans la fenetre
            canvas1 = Canvas(frame1, width=arena.lx, height=arena.ly)
            canvas1.pack()

            # creation canvas secondaire pour affichage messages erreur
            canvas_console = Canvas(frame2, width=500, height=30)
            canvas_console.pack()


            dessiner_robot(iRobot)

            fx, fy, fz = iRobot.getPosition()
            fy = fy + 50
            fx = fx - 50
            while(True):
                sleep=1
                tx, ty, tz = arena.liste_robot[0].getPosition()
                while (ty < fy):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    #time.sleep(sleep)
                    rafraichir(arena)
                    print(arena.liste_robot[0].toString())
                iRobot.rotation_bis(90)
                while (tx > fx):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    #time.sleep(sleep)
                    rafraichir(arena)
                    print(arena.liste_robot[0].toString())

                fx = fx + 50
                fy = fy - 50
                iRobot.rotation_bis(90)
                while (ty > fy):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    #time.sleep(sleep)
                    rafraichir(arena)
                    print(arena.liste_robot[0].toString())

                iRobot.rotation_bis(90)
                while (tx < fx):
                    tx, ty, tz = arena.liste_robot[0].getPosition()
                    arena.liste_robot[0].move_bis()
                    #time.sleep(sleep)
                    rafraichir(arena)
                    print(arena.liste_robot[0].toString())

                break
                fenetre.mainloop()

        # deplacement robot
