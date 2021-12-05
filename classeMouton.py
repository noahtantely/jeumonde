from random import randint
import random


class Mouton:
    def __init__(self, position_x, position_y, mondeMouton):
        self.position_x = position_x
        self.position_y = position_y
        self.gain_nourriture = 4 #entier : gain d'énergie par consommation d'un carré d'herbe
        self.taux_reproduction = 4 #entier : pourcentage de chance de reproduction d'un mouton
        self.mondeMouton = mondeMouton
        self.energie = randint(1, 2*self.gain_nourriture)

    def __repr__(self):
        return 'Mouton, x :'  + str(self.position_x) + ', y :' + str(self.position_y)

    def variationEnergie(self):
        if self.mondeMouton.carte[self.position_y][self.position_x][0] == -1:
            self.energie += self.gain_nourriture
        elif self.energie != 0:
            self.energie -= 1

    def getcarte(self):
        print(self.mondeMouton.carte)

    def deplacement(self):
        var_ligne = randint(-1,1)
        if var_ligne == 0:
            var_col = random.choice([-1,1])
        else:
            var_col = randint(-1,1)
        self.position_x = (self.position_x + var_col) % self.dimension #colonnes numérotées de 0 à dimension - 1
        self.position_y = (self.position_y + var_ligne) % self.dimension #lignes numérotées de 0 à dimension - 1
        #programmer mouton ne se déplace pas à tous les coups
    
    def place_mouton(self): # PAS OK
        try:
            self.mondeMouton.carte[self.position_y][self.position_x].append('Mouton')
        except:
            print(self.mondeMouton.carte)