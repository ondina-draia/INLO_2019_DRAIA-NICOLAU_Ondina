from point import Point

class Polygone():
    '''class representing a polygon'''
    
    def __init__(self, sommets):
        '''defines a list of corners (as lists of 2 coordinates, x and y) which will be the corners of the polygon'''
        self.__sommets = [sommets[x:x+2] for x in range(0, len(sommets), 2)] #takes the list of coordinates that we give (format ex: [1,2,3,4] and create a list corners)
        # takes the list and separes it in couples inside []s
        
    def getSommet(self, i):
        '''returns the corner at the i position of index'''
        return '[' + str(self.__sommets) + ']'            
    
    def aireSelf(self):
       '''return the polygon's area'''
       n = len(self.__sommets) # number of corners
       area = 0 #initializing area size at 0
       for i in range(n):
           j = (i + 1) % n # allows it to take only the odd indexes from the lists ( = y)
           area += (self.__sommets[i])[0] * (self.__sommets[j])[1] #computes the area from the x of each corner and adds it to the total area size
           area -= (self.__sommets[j])[0] * (self.__sommets[i])[1] #computes the area from the y of each corner and adds it to the total area size
       area = abs(area) / 2 # final step of the formula
       return area #returns the area size of the polygon
        
    def __str__(self): 
        '''returns the expression of a polygon'''
        return str(self.__sommets) 

class Triangle(Polygone):
    '''class representing a triangle
    a triangle is a polygon'''
    
    def __init__(self, a, b, c):
        '''builds a triangle from 3 corners'''
        sommets = [a, b, c] #enables the code to take only the first three apexes
        Polygone.__init__(self, sommets) #recalls the methods from Polygon mother class

class Rectangle(Polygone):
    '''class representing a rectangle
    a rectangle is a polygon'''
    
    def __init__(self, xMin, xMax, yMin, yMax):
        '''builds a rectangle from 4 corners'''
        self.__sommets = (xMin, yMin, xMax, yMax) #uses 4 coordinates as a couple of 2 points
        Polygone.__init__(self, self.__sommets) #recalls the method from Polygon mother class