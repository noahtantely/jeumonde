from classeMonde import Monde
from classeMouton import Mouton
import random
from random import randint


class Simulation:
    def __init__(self,nombre_moutons, nombre_moutons_max,fin_du_monde, monde, dimension):
        self.nombre_moutons = nombre_moutons #entier
        self.fin_du_monde = fin_du_monde #entier : horloge max
        self.monde = monde #héritance de classe etrangere
        self.horloge = 0
        self.dimension = dimension #héritance d'attribut de classe etrangere
        self.moutons = [Mouton(randint(0,self.dimension-1), randint(0,self.dimension-1), self.monde) for i in range(nombre_moutons)] #liste
        self.nombre_moutons_max = nombre_moutons_max
        self.resultats_herbe = [] #liste
        self.resultats_moutons = [] #liste

    def get_carte(self):
        print(self.monde.carte)
    def getmouton(self):
       print([i for i in self.moutons])

    def simMouton(self):
        for i in self.moutons :
            print(i)
            i.place_mouton()
        while not(self.moutons) or self.horloge != self.fin_du_monde or len(self.moutons) > self.nombre_moutons_max :
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
                '''Si mouton sur une case d'herbe, herbe mangee'''
                if self.monde.carte[i.position_y][i.position_x][0] == -1:
                    self.monde.herbeMangee(i.position_y, i.position_x)
                '''Reproduction Mouton'''
                apparait_ou_non = randint(1, 100)
                if apparait_ou_non <= i.taux_reproduction :
                    self.moutons.append(Mouton(i.position_x, i.position_y, self.monde.carte))
                    self.monde.carte[i.position_y][i.position_x].append('Mouton')
        return self.resultats_herbe, self.resultats_moutons

monde1 = Monde(5, 9)
mouton1 = Mouton(2,1,monde1)
mouton1.place_mouton()
sim1 = Simulation(5,10,10,monde1,5)
sim1.simMouton()