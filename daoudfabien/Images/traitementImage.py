#imports

from PIL import Image
import time
import operator
import random
#code
#resultats des test (jugement a l oeil nu)
"""
test 4 couleurs minimum~> (7/11 images detectees)
test 3 couleusr minimum ~>(11/11 images detectees)
test detection des 4 zones de couleur entiere ou presque ~> (6/11 detectees)
"""
fic0 = "ImageCopie.jpg"
#liste des differentes images pour tester plusieur detetction de couleurs (temporaire)
liste_fic = [
	"2018-03-06 02_51_06.486124",
	"2018-03-06 02_51_13.082451",
	"2018-03-06 02_51_18.273973",
	"2018-03-06 02_51_23.256724",
	"2018-03-06 02_51_28.118059",
	"2018-03-06 02_51_43.625168",
	"2018-03-06 02_51_48.413961",
	"2018-03-06 02_51_54.161908",
	"2018-03-06 02_52_18.483662",
	"Image",
	"ImageCopie"]
	
for i in range(0,len(liste_fic)):
    img = Image.open(liste_fic[i]+".jpg")

    COEF_FENETRE_RECHERCHE = 80 
    TAUX = 20 #en pourcent
    TAUX_CONVERTED = TAUX*255/100 #conversion pourcent en valeur pixel
    print(TAUX_CONVERTED)
    # affichage des caracteristiques de l image

    #print(img.format,img.size, img.mode)
    cptR = 0
    cptG = 0
    cptB = 0
    cptY = 0
    l = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r,g,b = img.getpixel((x,y))
            liste_couleur = [("r",r),("g",g),("b",b)]
            #print("list:",liste_couleur)
            liste_couleur.sort(key=operator.itemgetter(1), reverse=True)#tri de la liste
            #print("trié:",liste_couleur)
            #time.sleep(2)
            #print()
            #if(liste_couleur[0][1] > liste_couleur[1][1] + MARGE_CONVERTED):
            if(liste_couleur[0][0] == "r" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED):
                #print("dominante rouge")
                img.putpixel((x,y),(255,0,0))
                cptR += 1
            elif(liste_couleur[0][0] == "g" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED / 7):
                #print("dominante vert")
                img.putpixel((x,y),(0,255,0))
                cptG += 1
            elif(liste_couleur[0][0] == "b" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED):
                #print("dominante bleu")
                img.putpixel((x,y),(0,0,255))
                cptB += 1
            elif(liste_couleur[0][1] > 210 and
                 (liste_couleur[0][0] == "r" or
                  liste_couleur[0][0] == "g")and
                 liste_couleur[0][1] - liste_couleur[1][1] < TAUX_CONVERTED and
                 liste_couleur[1][1] > liste_couleur[2][1] + TAUX_CONVERTED):
                img.putpixel((x,y),(255,255,0))
                cptY += 1
                
    #affichage nb pxl R, V, B, J            
    print("rouge:",cptR,"vert:",cptG,"bleu:",cptB,"jaune:",cptY)
    
    #mise en commentaire temporaire...
    """
    # pixel de test (Vert) haut droit -> x+20, y
    # pixel de test (Rouge) bas gauche -> x, y+20
    # piexel de test (Bleu) bas droit -> x+20, y+20

    for x in range(img.size[0]-COEF_FENETRE_RECHERCHE):
        for y in range(img.size[1]-COEF_FENETRE_RECHERCHE):
            
            r_hd,g_hd,b_hd = img.getpixel( (x+COEF_FENETRE_RECHERCHE, y ) )
            r_bd,g_bd,b_bd = img.getpixel( (x+COEF_FENETRE_RECHERCHE, y+COEF_FENETRE_RECHERCHE) )
            r_bg,g_bg,b_bg = img.getpixel( (x, y+COEF_FENETRE_RECHERCHE) )
            
            test1 = ( r_bg,g_bg,b_bg ) == (255,0,0) # test pixel rouge
            test2 = ( r_hd,g_hd,b_hd ) == (0,255,0) # test pixel vert
            test3 = ( r_bd,g_bd,b_bd ) == (0,0,255) # test pixel bleu

            if test1 and test2 and test3 :
                #print("Balise trouvee : ",( (x+COEF_FENETRE_RECHERCHE)/2, (y+COEF_FENETRE_RECHERCHE)/2 ) )
                img.putpixel((x,y), (0,0,0))"""

    #DETECTION DE LA BALISE QUI MARCHE :)
    #le carre d'observation est une subdivision entiere de l'image ~> 1/10
    TAILLE_X = img.size[0]//10
    TAILLE_Y = img.size[1]//10
    for x in range(0, img.size[0]-TAILLE_X):
        for y in range(0, img.size[1]-TAILLE_Y):

            r_hg,g_hg,b_hg = img.getpixel( (x+10, y+10) )
            r_hd,g_hd,b_hd = img.getpixel( (x+TAILLE_X-10, y+10 ) )
            r_bd,g_bd,b_bd = img.getpixel( (x+TAILLE_X-10, y+TAILLE_Y-10) )
            r_bg,g_bg,b_bg = img.getpixel( (x+10, y+TAILLE_Y-10) )

            test1 = ( r_hg,g_hg,b_hg ) == (255,255,0) #test pixel jaune
            test2 = ( r_hd,g_hd,b_hd ) == (0,255,0) # test pixel vert
            test3 = ( r_bd,g_bd,b_bd ) == (0,0,255) # test pixel bleu
            test4 = ( r_bg,g_bg,b_bg ) == (255,0,0) # test pixel rouge

            if(test1 and test2 and test3 and test4):
                for j in range(x, x+TAILLE_X):
                    for k in range(y, y+TAILLE_Y):
                        #print("peinture!")
                        img.putpixel((j,k),(0,0,0))
                print("Balise trouvee :",x-TAILLE_X, y-TAILLE_Y)
    
    # fermeture du fichier image
    img.show()
    img.close()
	

#lien utile pour les valeurs RGB des pixels de l'image : https://www.imagecolorpicker.com/

