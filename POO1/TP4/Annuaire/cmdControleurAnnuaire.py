#!/usr/bin/python3
# -*- coding: utf-8 -*-

from modeleAnnuaire import ModeleAnnuaire
import cmdVueAnnuaire as vue
import tkinter.messagebox

repertoire_global = ModeleAnnuaire() #variable storing the data of the application


def chercher(Nom, Prenom, Telephone, Adresse, Ville):
    '''comand for button "chercher"'''
    nom = Nom.get()
    
    #test if field "Nom" is empty
    if not Nom.get():
        vue.afficheWarning("Champ \"Nom\" vide: Vous devez au minimum spécifier un nom")
        return False
    
    #test if "Nom" entered is present in data
    elif not repertoire_global.estPresent(nom):
        vue.afficheWarning(nom + ": absent du répertoire")
        return False
    
    #return data corresponding to "Nom"
    else:
        prenom, tel, adresse, ville = repertoire_global.chercher(nom)
        #Nom.set(nom) #
        Prenom.set(prenom) #set "Prenom" field value to corresponding "Nom"
        Telephone.set(tel) #set "Telephone" field value to corresponding "Nom"
        Adresse.set(adresse) #set "Adresse" field value to corresponding "Nom"
        Ville.set(ville) #set "Ville" field value to  corresponding "Nom"
        return True

      
def inserer(Nom, Prenom, Telephone, Adresse, Ville):
    '''comand for button "inserer"'''
    
    #test if field "Nom" is empty
    if not Nom.get():
        vue.afficheWarning("Champ \"Nom\" vide: vous devez au minimum spécifier un nom")
        return False
    
    #adds the entered values to the data
    else:
        data = ( Prenom.get(), Telephone.get(), Adresse.get(), Ville.get() )
        nom = Nom.get() 
        repertoire = ModeleAnnuaire()
        repertoire.inserer(nom, data)
        tkinter.messagebox.showinfo(nom +": ajouté au répertoire")
        supprimer(Nom, Prenom, Telephone, Adresse, Ville)
        global repertoire_global #appel de la variable globale afin de la modifier
        repertoire_global.inserer(nom, data)
        #print(repertoire_global)
        return repertoire


def supprimer(Nom, Prenom, Telephone, Adresse, Ville):
    '''delete fields from labels'''
    
    Nom.set('') #set "Nom" field value to back to nothing
    Prenom.set('') #set "Prenom" field value to back to nothing
    Telephone.set('') #set "Telephone" field value to back to nothing
    Adresse.set('') #set "Adresse" field value to back to nothing
    Ville.set('') #set "Ville" field value to back to nothing


def effacer(Nom, Prenom, Telephone, Adresse, Ville):
    '''command for button "effacer"'''
    
    if tkinter.messagebox.askyesno("Voulez-vous vraiment tout effacer" + '\u00A0' + '?'): #message box to check if user really wants to delete values from fields
        supprimer(Nom, Prenom, Telephone, Adresse, Ville) #delete values from fields
