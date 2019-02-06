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
        return "Point(x=" + str(self.__x) + ", y=" + str(self.__y) + ")"

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
        
class LignePol:
    """ Va representer des lignes polygonales, constituées d'un ensemble de points et de leurs sommets"""
    
    # deux variables d'instance privées
    def __init__(self,listecoordonnes):
    # definition de sommet comme etant une liste de point formé des coordonné 
    #de la liste fornie en argument
        self.__sommets=[]
        for i in range(0,len(listecoordonnes)-1,2):
            (self.__sommets).append(Point(listecoordonnes[i],listecoordonnes[i+1]))
            self.__nbsommet = len(self.__sommets)
    def __str__(self): 
        # renvoie une expression de la ligne polygonale sous forme de texte
        return "(" + str(self.__sommets) + ")"
    
    def getSommet(self, i):
        #renvoie le ième sommet
        return self.__sommets[i]
    
    def setSommet(self, i, p):
        #donne le point p pour valeur du ième sommet
        self.__sommets.insert(i,p)
        
    def homothetie(self, k):
        # qui applique à chaque sommet de la ligne polygonale une homothétie de centre (0, 0) et de rapport k
        for i in self.__sommets:
        	i.homothetie(k)
            
    def translation(self, dx, dy): 
        # qui applique à chaque sommet de la ligne polygonale une translation de vecteur (dx, dy)
        for i in self.__sommets:
            i.translation(dx, dy)
        
    def rotation(self, a):
        # qui applique à chaque sommet de la ligne polygonale une rotation de centre (0, 0) et d’angle a
        for i in self.__sommets:
            i.rotation(a)
        
    def tracer(self):
        #produit une ligne qui representerait le trace de la ligne polygonale sous la forme d'une cocotte
        print("tracer de ", end = '')
        for i in self.__sommets:
            if i != self.__sommets[-1]:
                print("(" + str(i.x()) + "," + str(i.y()) + ") à " , end='')
            else:
                print("(" + str(i.x()) + "," + str(i.y()) + ")" , end='')
        print()
        # nous avons pas repris la methode donnee dans l'enonce comme nous avons pas compris precisement ce qui
        # etait demandé concretement

#partie du code servant de test à nos classes        
s = [3,4,5,9,8,5] #liste des coordonnées sous forme de couples 2 par deux
LP = LignePol(s) #representation des points qui vont former la ligne polygonale
print(LP)
print(LP.getSommet(2)) #affiche un le 2eme sommet
pt = Point(3,4)
LP.setSommet(1, pt) #ajout un sommet pt à une certaine position i
print(LP)
LP.homothetie(5) #realise une homothetie de 5 sur la ligne polygonale
print(LP)
LP.translation(4,5) #fait une translation sur les coordonnees de la ligne polygonale LP
print(LP)
LP.rotation(8) # effectue une rotation sur les coordonnees de la ligne polygonale
print(LP)
LP.tracer() #permet de dire theoriquement comment les points seraient reliées entre eux 