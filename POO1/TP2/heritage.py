from point import Point

class Polygone:
    '''class representing a polygon'''

    def sommets(self): #devrait être une variable et non pas une méthode
        '''list the apexes of the polygon''' #doit également être une liste

    def __init__(self, coor): #coor représente la liste des coordonnées
        '''build the polygon from the apexes'''
        self.__sommets = []
        for i in range(0, len(coor)-1, 2):
            (self.__sommets).append(Point(coor[i], coor[i+1]))
    
    def __str__(self):
        '''return the polygon as text'''
    
    def getSommets(self, i):
        '''return the i-th apex of the polygon'''
    
    def aire(self):
        '''compute the area of the polygon'''
        largeur = self.ne.x - self.so.x
        hauteur = self.ne.y - self.so.y
        return abs(largeur * hauteur) #calcul d'une aire pour un rectangle
        #pour un polygone, il faut prendre en compte le nombre de sommets variables
        #indication de Tichit à la fin du TP
    