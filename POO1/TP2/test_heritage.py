# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 18:23:24 2019

@author: castr
"""

"""programme de test construisant et affichant des polygones de
diverses sortes et permettant de vérifier que la méthode aire est correcte"""

from heritage_complet import Polygone, Triangle, Rectangle, PolygoneRegulier

#test pour Polygone

s = [3,4,5,9,8,5] #coordinates list for the corners of the polygon
P = Polygone(s) #will create a polygon from the list given
print(P)
print(P.getSommet(1)) #lets us obtain the coordinates for the second corner defined
print(P.aireSelf()) #allows to obtain the size of the area of the polygon

#test pour Triangle

T = Triangle([3,4],[4,5],[4,5])
print(T)

#test pour Rectangle
R = Rectangle(1,2,3,4) #allows us to obtain a rectangle
print(R)

#test pour Polygone Regulier 

PR = PolygoneRegulier((3,8),7,5)
print(PR)