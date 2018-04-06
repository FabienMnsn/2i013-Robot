#imports

from PIL import Image
import time
import operator

#code

img = Image.open("ImageCopie.jpg")
MARGE = 40 
TAUX = 20 #en pourcent
TAUX_CONVERTED = TAUX*255/100 #conversion pourcent en valeur pixel
print(TAUX_CONVERTED)
# affichage des caractéristiques de l'image

#print(img.format,img.size, img.mode)
cptR = 0
cptG = 0
cptB = 0
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
        elif(liste_couleur[0][0] == "g" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED / 5):
            #print("dominante vert")
            img.putpixel((x,y),(0,255,0))
            cptG += 1
        elif(liste_couleur[0][0] == "b" and liste_couleur[0][1] > liste_couleur[1][1] + TAUX_CONVERTED):
            #print("dominante bleu")
            img.putpixel((x,y),(0,0,255))
            cptB += 1
            
print(cptR, cptG, cptB)
"""                
        maximum = max(r, g, b)
        if(maximum == r and maximum > 180):
            img.putpixel((x,y),(255,0,0))
        elif(maximum == g and maximum > 128):
            img.putpixel((x,y),(0,255,0))
        elif(maximum == b and maximum > 128):
            img.putpixel((x,y),(0,0,255))
           
# affichage de l'image

#img.show()

# pixel de test (Vert) haut droit -> x+20, y
# pixel de test (Rouge) bas gauche -> x, y+20
# piexel de test (Bleu) bas droit -> x+20, y+20

for x in range(img.size[0]-MARGE):
    for y in range(img.size[1]-MARGE):
        
        r_hd,g_hd,b_hd = img.getpixel( (x+MARGE, y ) )
        r_bd,g_bd,b_bd = img.getpixel( (x+MARGE, y+MARGE) )
        r_bg,g_bg,b_bg = img.getpixel( (x, y+MARGE) )
        
        test1 = ( r_bg,g_bg,b_bg ) == (255,0,0) # test pixel rouge
        test2 = ( r_hd,g_hd,b_hd ) == (0,255,0) # test pixel vert
        test3 = ( r_bd,g_bd,b_bd ) == (0,0,255) # test pixel bleu

        if test1 and test2 and test3 :
            print("Balise trouvee : ",( (x+MARGE)/2, (y+MARGE)/2 ) )

        
# fermeture du fichier image
"""
img.show()
img.close()


