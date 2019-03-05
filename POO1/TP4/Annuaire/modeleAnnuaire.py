#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class ModeleAnnuaire():
	'''description of "Annuaire"'''

	def __init__(self): #creates the 'annuaire' (phone book)
		self.__annuaire = {}

	def __str__(self): #organizes how the values will be showed and returned 
		l = []
		for k in self.__annuaire:
			data = self.__annuaire[k]
			l.append(str(k) + ': ' + str(data)) 
			l.sort()
		return '\n'.join(l)

	def chercher(self, nom): #searchs for a certain data associated to the given 'nom' key and returns it
		return self.__annuaire[nom]

	def estPresent(self, nom): #checks if an entry exists in the dictionnary and returns it
		return nom in self.__annuaire

	def inserer(self, nom, data): #inserts new data in the dictionnary and associates it with the given 'nom' value
	    self.__annuaire[nom] = data

def testModeleAnnuaire():
	a1 = ModeleAnnuaire()
	print(0, not a1.estPresent('a'))
	a1.inserer('a', 'b')
	a1.inserer('c', 'de')
	a1.inserer('f', ('g', 'h', 'i') )
	print(1, a1.estPresent('a'))
	print(2, not a1.estPresent('b'))
	print(3, a1.chercher('a') == 'b')
	print(4, a1.chercher('c') == 'de')
	print(5, a1.chercher('f') == ('g', 'h', 'i'))

if __name__ == "__main__":
	testModeleAnnuaire()
