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
                if i[0] >= self.__duree_repousse:
                    i[0] = -1 # -1 représente une case d'herbe sur la case
    
    def herbeMangee(self,i,j):
        self.carte[i][j][0] = 0

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