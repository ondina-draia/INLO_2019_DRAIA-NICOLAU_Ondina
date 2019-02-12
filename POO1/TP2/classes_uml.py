# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 19:28:36 2019

@author: castr
"""

class Matiere:
    """stocke les matieres disponibles"""
#stocke les matieres disponibles
#renvoie une matiere de notre choix 
#renvoie les matieres disponibles
        
    def __init__(self, matieres):
        
        self.__matiere = matieres
        self.__mat = []
        for i in range(len(self.__matiere)):
            self.__mat.append(self.__matiere[i]) #cree une liste de matieres disponibles
            
              
    def __str__(self):
        return str(self.__mat)
    
    def getMatiere(self,i):
        return self.__mat[i]
    
    def showMatieres(self):
        for i in range(len(self.__mat)):
            print(self.__mat[i])
    
        
class Etudiant(Matiere):
    """Permet d'enregistrer toutes les informations concernant les étudiants"""
    #stocke les informations de l'etudiant   
    #stocke les informations sur les matieres suivies
    #calcule les moyennes / matiere et generale
    #renvoies les données de l'etudiant, les matieres suivies, ses moyennes et moyenne generale et les matieres non suivies
    
    def __init__(self, nom, prenom, tel, email, annee, matieres_suivies, notes):
        self.nom = nom
        self.prenom = prenom
        self.tel = tel
        self.email = email
        self.annee = annee 
        
        self.__matieres_suivies = matieres_suivies
        self.__mat_suiv = []
        for i in range(len(self.__matieres_suivies)):
            self.__mat_suiv.append(self.__matieres_suivies[i]) #fait un liste des matieres suivies
        
        self.__notes = notes
        self.__notes_list = []
        for i in range(len(self.__notes)):
            self.__notes_list.append(self.__notes[i]) #fait une liste des notes obtenues
            
        self.__dict_notes = dict(zip(self.__mat_suiv, self.__notes_list)) #fait un dictionnaire matiere/note obtenue
            
                
    def __str__(self):
        return "nom: %s prenom: %s  tel: %s e mail: %s annee: %s notes pour chaque matiere:: %s " % (self.nom, self.prenom, self.tel, self.email, self.annee, self.__dict_notes)
    
    def moyenne_generale(self):
        return sum(self.__notes_list) / len(self.__notes_list) #calcule la moyenne des notes
    
    
### Test:     
    

if __name__=='__main__':
    matieres = ["coloriage", "manger"]
    matieres_suivies = ["coloriage", "boire"]
    matieres_disponibles = Matiere(matieres)
    print(matieres_disponibles) #affiche les matieres
    print(matieres_disponibles.getMatiere(1)) #affiche la 1ere matiere
    print(matieres_disponibles.showMatieres()) #montre les matieres disponibles
    etudiant = Etudiant("jaques","k","0635458","jak@mail.com","2012", matieres_suivies, [1,2])
    print(etudiant) #renvoie les informations du l'etudiant
    print(etudiant.moyenne_generale()) #donne la moyenne des matieres
    
### Tentative pour une fonction pour verifier quelles matieres sont suivies et lequelles non, je n'ai pas eu le temps de finir
"""def verifier_matieres( matieres_dispo, matieres_suivies):
        
        matieres_dispo = Matiere(matieres_dispo)01

      dict_matieres = dict.fromkeys(self._matieres_suivies, 0)
        for i, j in matieres_dispo, self.__dict_matieres.keys:
            if i == j:
                dict_matieres[j] = 1
            else:
                dict_matieres[j] = 0
        return dict_matieres"""