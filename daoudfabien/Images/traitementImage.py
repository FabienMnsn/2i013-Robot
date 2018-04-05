from PIL import Image


# ouverture du fichier image


img = Image.open("image5.jpg")
MARGE = 5
# affichage des caractéristiques de l'image

print(img.format,img.size, img.mode)
cpt_r = 0
cpt_g = 0

for x in range(img.size[0]):
    for y in range(img.size[1]):
        r,g,b = img.getpixel((x,y))
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

img.show()
img.close()


