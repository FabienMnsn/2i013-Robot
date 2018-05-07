from PIL import Image


def trouver_carre(image):
    img = Image.open(image)

    # affichage des caractéristiques de l'image
    print (img.format,img.size, img.mode)

    largeur = img.size[0]
    hauteur = img.size[1]

    img.show()

    c1l = 0
    c1h = 0
    c2l = 0
    c2h = 0

    for i in range (0,largeur):
        for j in range (0,hauteur):
            tup = img.getpixel((i,j))
            if tup[0] <= 10 and tup[1] >= 190 and tup[2] <= 10:
                if c1h == 0:
                    c1l = i
                    c1h = j
                    print("Coin inferieur gauche trouve aux coordonnees :",i,j)
                c2l = i
                c2h = j
                
    print("Coin superieur droit  trouve aux coordonnees :",c2l,c2h)
    print("Centre du carre aux coordonnees :",c1l+(c2l-c1l)//2,c1h+(c2h-c1h)//2)

    img.close()
    

#tests de la fonction
trouver_carre("solovert-1.jpg")
trouver_carre("solovert-2.jpg")
