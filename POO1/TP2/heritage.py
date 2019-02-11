#from point import Point

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

class PolygoneRegulier(Polygone):
    '''class representing a regular polygon
    a regular polygon is a polygon'''
    
    def __init__(self, centre, rayon, nombreSommets):
        '''builds a regular polygon from the centre (coordinates), the radius and the number of corners'''
        
        # Setting the variables
        import math #library required for cos, sin and pi
        self.__centre = list(centre) #transforms the coordinates of center into a list to use its elements seperately after
        X = [] #creates an empty list
        Y = [] #create an empty list
        self.__sommets = [] #creates an empty list
        
        # Calculations of the corners' coordinates
        for i in range(0, nombreSommets, 2): #computes the x-axes coordinates of the corners
            x = round(self.__centre[0] + rayon * math.cos(2*math.pi*i/nombreSommets), 3) #rounds up the result to the 3rd digit
            X.append(x) #saves the x-coordinates of all the corners
        for i in range(1, nombreSommets, 2): #computes the y-axes coordinates of the corners
            y = round(self.__centre[1] + rayon * math.sin(2*math.pi*i/nombreSommets), 3) #rounds up the result to the 3rd digit
            Y.append(y) #saves the y-coordinates of all the corners
        
        # Coordinate output
        for e in range(len(X)): #for all elements in both lists
            (self.__sommets).append(X[e]) #adds an element from X list into self.__sommets
            (self.__sommets).append(Y[e]) #then adds an element from Y list into self.__sommets
            e += 1 #starts again for the next elemenr of both lists
        Polygone.__init__(self, self.__sommets) #recalls the method from Polygon mother class
