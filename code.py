'''This will be the main python script file'''

from random import randint
import random
class Monde:
    def __init__(self,dimension, duree_repousse):
        self.dimension = dimension
        self.__duree_repousse = duree_repousse
        #self.carte = [[0 for i in range(dimension)] for i in range(dimension)]
        self.carte = [[] for i in range(self.dimension)]
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
                if i[0] >= self.__duree_repousse:
                    i[0] = -1 # -1 représente une case d'herbe sur la case
    
    def herbeMangee(self,i,j):
        self.carte[i][j][0] = 0

    def nbHerbe(self): #renvoie un ENTIER
        compte = 0
        for i in self.carte:
            for j in i:
                if j[0] == -1:
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
        self.carte = carte #classe Monde
        self.energie = randint(1, 2*self.gain_nourriture)

    def __repr__(self):
        return 'Mouton, x :'  + str(self.position_x) + ', y :' + str(self.position_y)

    def variationEnergie(self):
        if self.carte[self.position_y][self.position_x][0] == -1:
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
        self.position_x = (self.position_x + var_col) % len(self.carte) #colonnes numérotées de 0 à dimension - 1
        self.position_y = (self.position_y + var_ligne) % len(self.carte) #lignes numérotées de 0 à dimension - 1
        #programmer mouton ne se déplace pas à tous les coups
    
    def place_mouton(self): # PAS OK
        try:
            self.carte[self.position_y][self.position_x].append('Mouton')
        except:
            print(self.carte)

class Simulation:
    def __init__(self,nombre_moutons, nombre_moutons_max,fin_du_monde, monde, dimension):
        self.nombre_moutons = nombre_moutons
        self.fin_du_monde = fin_du_monde
        self.monde = monde #héritance de classe etrangere
        self.horloge = 0
        self.dimension = dimension #héritance d'attribut de classe etrangere

        self.moutons = [Mouton(randint(0,self.dimension-1), randint(0,self.dimension-1), self.monde.carte) for i in range(nombre_moutons)]
        self.nombre_moutons_max = nombre_moutons_max
        self.resultats_herbe = []
        self.resultats_moutons = []

    def get_carte(self):
        print(self.monde.carte)
    def getmouton(self):
       print([i for i in self.moutons])

    def simMouton(self):
        for i in self.moutons :
            i.place_mouton()
        while (not(self.moutons)) or self.horloge != self.fin_du_monde or len(self.moutons) > self.nombre_moutons_max :
            self.resultats_moutons.append(len(self.moutons))
            self.horloge += 1
            self.resultats_herbe.append(self.monde.nbHerbe())
            self.monde.herbePousse()
            for i in self.moutons:
                i.variationEnergie()
                '''Mouton meurt si energie nulle / Le retire de la liste des moutons et de la carte'''
                if i.energie == 0:
                    self.moutons.remove(i)
                    del self.monde.carte[i.position_y][i.position_x][1]
                    continue

                '''Si mouton sur une case d'herbe, herbe mangee'''
                if self.monde.carte[i.position_y][i.position_x][0] == -1:
                    self.monde.herbeMangee(i.position_y, i.position_x)
                
                '''Reproduction Mouton'''
                apparait_ou_non = randint(1, 100)
                if apparait_ou_non <= i.taux_reproduction :
                    self.moutons.append(Mouton(i.position_x, i.position_y, self.monde.carte))
                    self.monde.carte[i.position_y][i.position_x].append('Mouton')

                '''Déplacement Mouton'''
                del self.monde.carte[i.position_y][i.position_x][1]
                i.deplacement()
                i.place_mouton()
        return self.resultats_herbe, self.resultats_moutons


monde1 = Monde(50, 30)
mouton1 = Mouton(2,1,monde1.carte)

sim1 = Simulation(20,100,20,monde1, monde1.dimension)
print(sim1.simMouton())