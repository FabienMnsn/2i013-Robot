from PIL import Image


# ouverture du fichier image




img = Image.open("Image.jpg")

# affichage des caractéristiques de l'image

print(img.format,img.size, img.mode)

# affichage de l'image

img.show()

# fermeture du fichier image

img.close()
