'''This will be the main python script file'''

from random import randint
import random
class Monde:
    def __init__(self,dimension, duree_repousse, ):
        self.__dimension = dimension
        self.__duree_repousse = duree_repousse
        #self.carte = [[0 for i in range(dimension)] for i in range(dimension)]
        self.carte = [[] for i in range(self.__dimension)]
        for k in self.carte:
            for j in range(dimension):
                herbe_ou_pas = randint(1,2) #1 chance sur 2 que la case soit herbue au départ
                if herbe_ou_pas == 1: #1 correspond à mettre de l'herbe
                    k.append([-1]) #CASE SOUS FORME D'UNE LISTE POUR ACCUEILLIR VALEUR ET MOUTONS
                else: #ajoute entier aléatoire entre 0 et duree_repousse
                    k.append([randint(0,self.__duree_repousse)])

    def herbePousse(self):
        for j in self.carte:
            for i in j:
                if i >= self.__duree_repousse:
                    i = -1 #-1 représente herbe sur la case

    def herbeMangee(self,i,j):
        self.carte[i][j] = 0

    def nbHerbe(self):
        compte = 0
        for i in self.carte:
            for j in i:
                if j == -1:
                    compte += 1
        return compte

    def CoefCarte(self, i, j):
        return self.carte[i][j]

    def getCarte(self):
        return self.carte

class Mouton:
    def __init__(self, position_x, position_y, carte):
        self.position_x = position_x
        self.position_y = position_y
        self.gain_nourriture = 4 #entier : gain d'énergie par consommation d'un carré d'herbe
        self.taux_reproduction = 4 #entier : pourcentage de chance de reproduction d'un mouton
        self.carte = carte
        self.energie = randint(1, 2*self.gain_nourriture)

    def variationEnergie(self):
        if self.carte[self.position_y][self.position_x][0] == -1:
            self.energie += self.gain_nourriture
        elif self.energie != 0:
            self.energie -= 1
    
    def deplacement(self):
        var_ligne = randint(-1,1)
        if var_ligne == 0:
            var_col = random.choice([-1,1])
        else:
            var_col = randint(-1,1)
        self.position_x = (self.position_x + var_col) % self.dimension #colonnes numérotées de 0 à dimension - 1
        self.position_y = (self.position_y + var_ligne) % self.dimension #lignes numérotées de 0 à dimension - 1
        #programmer mouton ne se déplace pas à tous les coups
    
    def place_mouton(self):
        self.carte[self.position_y][self.position_x].append(1)

class Simulation:
    def __init__(self,nombre_moutons, fin_du_monde, monde, dimension):
        self.nombre_moutons = nombre_moutons
        self.fin_du_monde = fin_du_monde
        self.monde = monde #héritance de classe etrangere
        self.horloge = 0
        self.dimension = dimension #héritance d'attribut de classe etrangere
        self.moutons = [Mouton(randint(0,self.dimension), randint(0,self.dimension), monde.carte) for i in range(nombre_moutons)]
        self.resultats_herbe = []
        self.resultats_moutons = []

    def simMouton(self):
        self.horloge += 1
        self.monde.herbePousse()

monde1 = Monde(5,30)
mouton1 = Mouton(2,1,monde1.carte)
mouton1.place_mouton()
print(monde1.carte)