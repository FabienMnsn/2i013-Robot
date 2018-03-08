class Strategy():
    def __init__(self):
        True
    def dessine_carre(self,taille):
        avancer=0
        #(nb_pas) = avancer de nb_pas
        #(-1) = tourner de 90 degres dans le sens anti-horaire
        i=0
        L = []
        while i<4 :
            L.append(taille)
            L.append(-1)
            i = i+1

        return L
            
        
        
