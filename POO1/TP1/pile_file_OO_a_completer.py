class Pile:
    '''class representing a pile'''
 
    def __init__(self):
        '''create an empty pile'''
        self.pile = []

    def estVide(self):
        '''return TRUE if the pile is empty'''
        return self.pile == []
 
    def empiler(self, element):
        '''add an element to the pile'''
        return self.pile.append(element)
 
    def depiler(self):
        '''delete the last element of the pile'''
        return self.pile.pop()

    def sommet(self):
        '''return the last element of the pile'''
        return self.pile[-1]

class File:
    '''class representing a queue'''
 
    def __init__(self):
        '''create an emty queue'''
        self.file = []

    def estVide(self):
        '''return TRUE if the queue is empty'''
        return self.file == []
 
    def enfiler(self, element):
        '''add an element to the queue'''
        return self.file.append(element)
 
    def defiler(self):
        '''delete the first element from the queue'''
        return self.file.pop(0)
    
    def tete(self):
        '''return the element at the beginning of the queue'''
        return self.file[0]

if __name__ == "__main__": # ne pas toucher au code ci-dessous
	f = File()
	for i in range(5):
		f.enfiler(i)
	while not f.estVide():
		print(f.defiler())
	try:
		f.defiler()
	except IndexError as e:
		print(e)
	try:
		print(f.tete())
	except IndexError as e:
		print(e)

	p = Pile()
	for i in range(5):
		p.empiler(i)
	while not p.estVide():
		print(p.depiler())
	try:
		p.depiler()
	except IndexError as e:
		print(e)
	try:
		print(p.sommet())
	except IndexError as e:
		print(e)