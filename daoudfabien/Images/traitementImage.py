from PIL import Image


# ouverture du fichier image


img = Image.open("ImageCopie.jpg")
MARGE = 20
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
        elif(maximum == g and maximum > 180):
            img.putpixel((x,y),(0,255,0))
        elif(maximum == b and maximum > 170):
            img.putpixel((x,y),(0,0,255))
# affichage de l'image

img.show()

# fermeture du fichier image

img.close()
