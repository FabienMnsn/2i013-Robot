
# import

from tkinter import *
from structures.arene import *
from basiques.cube import *
from basiques.mur import *
from basiques.sol import *
from structures.capteur import *
from TestStrategy import *
import random
import time

# code
    

# _________________________CREATION DU ARENE DE BASE ~> PAS TRES PROPRE__________________________

a1 = Creation_Arene()

strat = Strategy()
test = TestStrategy(strat)
a1.liste_strat=strat.dessine_carre(50)
# ___________________________________GENERATEUR DE MUR___________________________________



def gen_aleatoire():
    a1.generateur_arene()
    rafraichir(a1)

# ___________________________________GESTION DES CLICS (G & D)___________________________________

# fonction detection du clic gauche (ajout d'un obstacle de type cube)
def clicgauche(event):
    if a1.possede_sol():
        X = event.x
        Y = event.y
        c1 = Creation_Cube_xy(X, Y, a1)
        if a1.ajouter_cube(c1):
            dessiner_cube(c1, a1)
        else:
            canvas_console.delete(ALL)
            canvas_console.create_text(250, 15, text="Error : object 'Cube' outside arena ", fill="black", width=500,justify='center')
            print("Error : object 'Cube' outside arena ")
    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250, 15, text="Ajoutez un sol avant de poser des blocs !", fill="black", width=500,justify='center')
        print("Ajoutez un sol avant de poser des blocs !")


# fonction detection du clic droit (ajout d'un mur)
def clicdroit(event):
    if a1.possede_sol():
        X = event.x
        Y = event.y
        m1 = Creation_Mur_xy(X, Y, a1)
        if a1.ajouter_cube(m1):
            dessiner_mur(m1, a1)
        else:
            canvas_console.delete(ALL)
            canvas_console.create_text(250, 15, text="Error : object 'Mur' outside arena ", fill="black", width=500, justify='center')
            print("Error : object 'Mur' outside arena ")
    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250, 15, text="Ajoutez un sol avant de poser des blocs !", fill="black", width=500,justify='center')
        print("Ajoutez un sol avant de poser des blocs !")


# ___________________________________AJOUT D'UN SOL VIA LE BOUTON___________________________________

def ajout_sol():
    global s1
    if not a1.possede_sol():
        s1 = Creation_Sol(a1)
        if a1.ajouter_cube(s1):
            dessiner_sol(s1)
    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250,15, text="Il y a déjà un sol !", fill="black", width=500, justify='center')
        print("Il y a déjà un sol !")


#___________________________________AJOUT D'UN ROBOT VIA LE BOUTON___________________________________

def ajout_robot():

    if len(a1.liste_robot) == 0 and a1.possede_sol():
        robot=Creation_Robot(a1)
        a1.ajouter_robot(robot)
        dessiner_robot(robot)

    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250, 15, text="Il y a déjà un robot OU pas de sol !", fill="black", width=500, justify='center')




# ___________________________________FENETRE PRINCIPALE___________________________________

fenetre = Tk()
fenetre.geometry("600x700")
fenetre.title("Robot 2i013 Alpha 3.1")
fenetre.resizable(width=True, height=True)
# affichage d'un texte dans la fenetre principale
label = Label(fenetre, text="Clic gauche ~> ajout d'un cube Clic droit  ~> ajout d'un mur").pack()


# ___________________________________FRAME & CANEVAS___________________________________

# creation frame1 -> conteneur
frame1 = LabelFrame(fenetre, text="Carré gris = Arene 500 x 500px", borderwidth=2, relief=GROOVE)
frame1.pack(side=TOP, padx=5, pady=5)

#creation frame2 ~> conteneur message erreur
frame2 = LabelFrame(fenetre, text="Informations", borderwidth=2, relief=GROOVE)
frame2.pack(side=TOP, padx=5, pady=5)

# creation d'un canvas principal (toile ou tableau) dans la fenetre
canvas1 = Canvas(frame1, width=a1.lx, height=a1.ly)
canvas1.bind('<Button-1>', clicgauche)
canvas1.bind('<Button-3>', clicdroit)
canvas1.pack()

#creation canvas secondaire pour affichage messages erreur
canvas_console = Canvas(frame2, width=500, height=30)
canvas_console.pack()


#_________________________________TOUCHES CLAVIER_________________________________


def clavier(event):
    """fonction d'interaction clavier"""
    robot = a1.liste_robot[0]
    long, larg, haut = robot.dimension
    capteur = Capteur(a1)
    touche=event.keysym
    distance_obstacle = capteur.detecter_distance()
    distance_arret_urgence = 6
    #print(touche)
    
    
    
    if touche=='Up':
        #distance_obstacle = capteur.detecter_distance()
        #print("Distance au prochain obstacle : ",distance_obstacle)
        if(distance_obstacle <= distance_arret_urgence and distance_obstacle != -1):
            affichage_distance_canvas(distance_obstacle, distance_arret_urgence)
        else:
            affichage_distance_canvas(distance_obstacle, distance_arret_urgence)
            a1.liste_robot[0].setVitesse(2)
            robot.move_bis()
        rafraichir(a1)
    
    if touche =='Left':
        affichage_distance_canvas(distance_obstacle, distance_arret_urgence)
        a1.liste_robot[0].rotation_bis(-10)
        rafraichir(a1)
        #bouton_rotation_G()
        
    if touche =='Right':
        affichage_distance_canvas(distance_obstacle, distance_arret_urgence)
        a1.liste_robot[0].rotation_bis(10)
        rafraichir(a1)
        #bouton_rotation_D()
        
    if touche=='Down':
        affichage_distance_canvas(distance_obstacle, distance_arret_urgence)
        a1.liste_robot[0].setVitesse(-2)
        a1.liste_robot[0].move_bis()
        rafraichir(a1)
        
    if touche =='q':
        affichage_distance_canvas(distance_obstacle, distance_arret_urgence)
        robot.tete.rotation(-1)
        rafraichir(a1)
        
    if touche =='d':
        affichage_distance_canvas(distance_obstacle, distance_arret_urgence)
        robot.tete.rotation(1)
        rafraichir(a1)

    if touche =='z':
        robot.tete.setOrientation(robot.direction)
        rafraichir(a1)

    if touche == 'b':
        #print(strat.dessine_carre(70))
        a1.liste_robot[0].setVitesse(2)
        test.Test2(a1.liste_robot[0],a1.liste_strat)
        rafraichir(a1)
        
    #canvas1.coords(robot_rectangle,x, y, x + larg, y + long)

canvas1.bind_all('<Key>', clavier)


# ___________________________________NETTOYAGE DU CANEVAS___________________________________

def effacer():
    """efface tout le canvas"""
    canvas1.delete(ALL) 
    canvas_console.delete(ALL)
    while len(a1.liste_cube) > 0:
        a1.liste_cube.pop(-1)
    while len(a1.liste_robot) > 0:
        a1.liste_robot.pop(-1)


# ___________________________________LES BOUTONS___________________________________

# creation d'un bouton de fermeture de la fenetre
bouton1 = Button(fenetre, text="Quitter", command=fenetre.destroy).pack(side=RIGHT)

# creation d'un bouton de nettoyage du canvas
bouton2 = Button(fenetre, text="Effacer tout", command=effacer).pack(side=LEFT)

# creation d'un bouton qui ajoute un sol à l'arene
bouton3 = Button(fenetre, text="Nouveau Sol", command=ajout_sol).pack(side=LEFT)

# creation d'un bouton qui affiche l'état de l'arene
bouton4 = Button(fenetre, text="Etat Arene", command=a1.afficher).pack(side=LEFT)

# creation bouton qui genere des murs tout autour de l'arene ainsi que des obstacles
bouton5 = Button(fenetre, text="Generation Salle(WIP)", command=gen_aleatoire).pack(side=LEFT)

#creation d'un bouton qui ajoute un robot à l'arene
bouton6 = Button(fenetre, text= "Ajout Robot", command=ajout_robot).pack(side=LEFT)



# ___________________________________FONCTIONS DRAW___________________________________

def rafraichir(arene):

    canvas1.delete(ALL) 
    i = 0
    for c in arene.liste_cube:
        if isinstance(c, Sol):
            dessiner_sol(c)
        if isinstance(c, Mur):
            dessiner_mur(c,arene)
        elif isinstance(c, Cube):
            dessiner_cube(c,arene)
            
    if(len(arene.liste_robot) == 1):
        #print(arene.liste_robot[0].tete.orientation)
        dessiner_robot(arene.liste_robot[0])
        #print("R.rafrai.",arene.liste_robot[0].position)
    
def dessiner_cube(cube, arene):
    if isinstance(cube, Cube) and cube.x + cube.larg < arene.lx and cube.y + cube.long < arene.ly:
        canvas1.create_rectangle(cube.x, cube.y, cube.x + cube.larg, cube.y + cube.long, fill="darkgrey")
        canvas1.create_text(cube.x + cube.larg / 2, cube.y + cube.long / 2, text="Cube", fill="darkgrey",
                            activefill="black")


def dessiner_mur(mur, arene):
    if isinstance(mur, Mur) and mur.x + mur.larg < arene.lx and mur.y + mur.long < arene.ly:
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
    #print( dirtetex, dirtetey)
    #print("robot.coords",robot.coords)
    canvas1.create_polygon(robot.coords, fill="blue")
    #canvas1.create_text(x + larg / 2, y + long / 2, text="Robot", fill="blue", activefill="black")

    # creation d'une fleche indiquant la direction du robot
    canvas1.create_line((x0+x1)/2, (y0+y1)/2, ((x0+x1)/2 + dirtetex*3), ((y0+y1)/2 + dirtetey*3), fill="black", arrow='last')
    canvas1.create_oval(milieu_avant_robot_xy[0]-4, milieu_avant_robot_xy[1]-4, milieu_avant_robot_xy[0]+4, milieu_avant_robot_xy[1]+4, fill="red")

def affichage_distance_canvas(distance, limite):
    """si la distance obtenue != -1 alors cette fonction l'affiche. Sinon elle affiche un message d'erreur"""
    if(distance == -1):
        canvas_console.delete(ALL)
        canvas_console.create_text(250,15, text="{Contact dans} scanner_out_of_range m", fill="black", width=500, justify='center')
    elif(distance > 0 and distance <= limite):
        canvas_console.delete(ALL)
        canvas_console.create_text(250,15, text="EMERGENCY BRAKING", fill="black", width=500, justify='center')
    else:
        canvas_console.delete(ALL)
        canvas_console.create_text(250,15, text=('Contact dans',distance,"m"), fill="black", width=500, justify='center')
        

# ___________________________________MAINLOOP___________________________________

fenetre.mainloop()

