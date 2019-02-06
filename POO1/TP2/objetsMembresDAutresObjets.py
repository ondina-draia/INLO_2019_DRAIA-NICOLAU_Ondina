from point import Point

class Rectangle:
    '''class representing a rectangle'''
    
    def __init__(self, x0, y0, x1, y1):
        '''build a rectangle from 2 points'''
        self.coinSE = Point(x0, y0)
        self.coinNO = Point(x1, y1)
    
    def __str__(self):
        '''return rectangle as text'''
        return '[' + str(self.coinSE) + ';' + str(self.coinNO) +']'

print('Test de la question B: avec r2=r1')
if __name__ == '__main__':
    r1 = Rectangle(1, 2, 3, 4)
    r2 = r1
    print("r1: " + str(r1) + ", r2: " + str(r2))
    r1.coinNO = Point(0, 0)
    print("r1: " + str(r1) + ", r2: " + str(r2))
    r1.coinSE.homothetie(2)
    print("r1: " + str(r1) + ", r2: " + str(r2))
# r2 est toujours égal à r1, même après modification de r1.
# Tout au long de ce test, r2 est bien une duplication de r1.

import copy

print()
print('Test de la question C: avec r2=copy.copy(r1)')
if __name__ == '__main__':
    r1 = Rectangle(1, 2, 3, 4)
    r2 = copy.copy(r1)
    print("r1: " + str(r1) + ", r2: " + str(r2))
    r1.coinNO = Point(0, 0)
    print("r1: " + str(r1) + ", r2: " + str(r2))
    r1.coinSE.homothetie(2)
    print("r1: " + str(r1) + ", r2: " + str(r2))
# r2 est égal r1 si r1 n'est pas modifié.
# Aprés modification de r1, r2 garde la première copie de r1.
# Cependant, r2 est influencé par les modifications de r1 lorsqu'une méthode est utilisée.

print()
print('Test de la question D: avec r2=copy.deepcopy(r1)')
if __name__ == '__main__':
    r1 = Rectangle(1, 2, 3, 4)
    r2 = copy.deepcopy(r1)
    print("r1: " + str(r1) + ", r2: " + str(r2))
    r1.coinNO = Point(0, 0)
    print("r1: " + str(r1) + ", r2: " + str(r2))
    r1.coinSE.homothetie(2)
    print("r1: " + str(r1) + ", r2: " + str(r2))
# r2 est égal à r1 au début, mais ceci n'est plus le cas dès la modification de r1.
# En effet, deeepcopy() réalise une copie définitive:
# même si r1 est modifié cela n'influence pas r2 car la copie est déjà faite et reste définitive.

