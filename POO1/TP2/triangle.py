# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 17:40:57 2019

@author: castr
"""

#from point_base import Point
#import math

class Polygone():
    ''' class representing a polygon '''
    
    def __init__(self, sommets):
    # defines a list of corners (as lists of 2 coordinates, x and y) which will be the corners of the polygon
        self.__sommets = [sommets[x:x+2] for x in range(0, len(sommets), 2)] #takes the list of coordinates that we give (format ex: [1,2,3,4] and create a list corners)
        # takes the list and separes it in couples inside []s
        
    def getSommet(self, i):
        #returns the corner at the i position of index
        return self.__sommets[i]
            
    
    def aireSelf(self):
       #return the polygon's area
       n = len(self.__sommets) # number of corners
       area = 0 #initializing area size at 0
       for i in range(n):
           j = (i + 1) % n # allows it to take only the odd indexes from the lists ( = y)
           area += (self.__sommets[i])[0] * (self.__sommets[j])[1] #computes the area from the x of each corner and adds it to the total area size
           area -= (self.__sommets[j])[0] * (self.__sommets[i])[1] #computes the area from the y of each corner and adds it to the total area size
       area = abs(area) / 2 # final step of the formula
       return area #returns the area size of the polygon
        
    def __str__(self): 
        # returns the expression of a polygon
        return str(self.__sommets) 
    
class Triangle(Polygone):
    ''' class representing a triangle'''
    
    def __init__(self, a, b, c):
        sommets = [a, b, c] #enables the code to take only 3 apexes as it's a triangle
        Polygone.__init__(self, sommets) #recalls the methods from Polygon mother class
    

s = [3,4,5,9,8,5] #coordinates list for the corners of the polygon
P = Polygone(s) #will create a polygon from the list given
print(P)
print(P.getSommet(1)) #lets us obtain the coordinates for the second corner defined
print(P.aireSelf()) #allows to obtain the size of the area of the polygon 
T = Triangle([3,4],[4,5],[4,5]) # takes only 3 arguments 
print(T)

