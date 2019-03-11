# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:01:47 2019

@author: castr
"""

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
        
    def import_db(self, db): #fetches phone book data from a phone book type database
        from sqlalchemy import create_engine
        path = str( "sqlite:///" + db) #local database connected from same directory
        engine = create_engine(path, echo=False) 
        conn = engine.connect()
        from sqlalchemy.sql import select, text
        s = select([text("* from users")]) #get all users informations
        result = conn.execute(s).fetchall()
        noms = [] #emptye 'noms' list
        for nom in range(len(result)):
            noms.append(result[nom][0]) #inserts all names from the database into 'noms' list
        datas = []
        for data in range(len(result)):
            datas.append(result[data][1:]) #inserts all other data connected to the names into datas list
        for nom in range(len(noms)):
            for data in range(len(noms)):
                self.__annuaire[nom] = data #inserts all this data to the phonebook
        

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
    a1.import_db("annuaire.db") #connection to local phone book database
    print(6, not a1.estPresent("Leboswki"))
   
    
if __name__ == "__main__":
    testModeleAnnuaire()