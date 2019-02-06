#!/usr/bin/python3
# -*- coding: utf-8 -*-

# avec les coordonnées CARTESIENNES

# Rappel de formules: x = r × cos(t), y = r × sin(t), r = sqrt(x2 + y2), t = atan(y / x) [ou, mieux,
# t = atan2(y, x) ]

import math

class Point:
    ''' class representing a point in 2-dimensions'''
    
    def __init__(self, x = 0, y = 0): #constructeur
        '''construct a point from cartesian coordinates x,y'''
        self.placement(x, y)

    def __eq__(self, autrePoint):
        return isinstance(autrePoint, Point) \
            and    self.x() == autrePoint.x() \
            and    self.y() == autrePoint.y()
        # comparaison : a == b répond à la question « a et b représentent-ils deux points égaux ? 

    def __repr__(self):
        return "Point(x=" + str(self.r()) + ", y=" + str(self.t()) + ")"

    def __str__(self):
        '''return cartesian coordinates of point'''
        return "(" + str(self.__x) + ", " + str(self.__y) + ")"
    # qui renvoie une expression textuelle du point, comme "(2.0, 3.0)"

    def x(self): return self.__x #qui renvoie les coordonnées cartésiennes du point

    def y(self): return self.__y #idem

    def r(self): return math.sqrt(self.__x ** 2 + self.__y ** 2)

    def t(self): return math.atan2(self.__y, self.__x) #r, t qui renvoient les coordonnées polaires du point 

    def distance(self, p):
        '''return Euclidian distance between 2 self and other Point'''
        return math.sqrt((self.__x - p.x())**2 + (self.__y - p.y())**2)

    def placement(self, x, y):
        '''sets the point at coordinates x, y
           raise ValueError if x or y is negative'''
        if x < 0 or y < 0:
            raise ValueError('Bad value: coordinates must be positive')
        self.__x = x
        self.__y = y

    def homothetie(self, k):
        self.__x = self.__x * k
        self.__y = self.__y * k
        #qui applique au point une homothétie de centre (0, 0) et de rapport k (k est un flottant) 
        #pour cela, il suffit de remplacer (x, y) par (k × x, k × y)
        #n mathematics, a homothety is a transformation of an affine
        #space determined by a point S called its center and a nonzero number λ called its ratio

    def translation(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy
        # qui applique au point une translation de vecteur (dx, dy) ; cela consiste à remplacer
        #(x, y) par (x + dx, y + dy)
        
    def rotation(self, a):
        coord_r = self.r()
        coord_t = self.t() + a
        self.__x = coord_r * math.cos(coord_t)
        self.__y = coord_r * math.sin(coord_t)
        """ qui applique au point une rotation de centre (0, 0) et d’angle a.
        Une manière – qui n’est pas la plus efficace – de faire cela
        consiste à calculer les coordonnées polaires (r, t)
        correspondant à (x, y) puis les coordonnées cartésiennes (x’, y’) correspondant à (r, t + a) """

if __name__=='__main__':
    p = Point(3, 4)
    p2 = "point"
    p3 = Point(3, 4)
    p4 = Point(4, 4)
    print(p==p, not p==p2, p==p3, not p==p4) # T T T T
    print(p) # (3, 4)
    p.homothetie(3.0)
    print(p) # (9, 12)
    p.translation(1, 1)
    print(p) # (10, 13)
    p.rotation(math.pi/2)
    print(p) # (-13, 10)
    print(p3.distance(p4)) # 1
    print(repr(p))

