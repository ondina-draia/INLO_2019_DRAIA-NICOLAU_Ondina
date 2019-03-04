#!/usr/bin/python3
# -*- coding: utf-8 -*-

from modeleAnnuaire import ModeleAnnuaire
import cmdVueAnnuaire as vue
import tkinter.messagebox


repertoire_global = ModeleAnnuaire() #le dictionnaire qui va contenir toutes les données de notre application annuaire

def chercher(Nom):
    '''comand for button "chercher"'''
    nom = Nom.get()
    if not Nom.get(): #tester si Nom est vide
        vue.afficheWarning("Champ \"Nom\" vide: Vous devez au minimum spécifier un nom")
        return False
    elif not repertoire_global.estPresent(nom):
        vue.afficheWarning(Nom.get() + ": absent du répertoire")
        return False
    else:
        nom = Nom.get()
        prenom, tel, adresse, ville = repertoire_global.chercher(nom)
        print( prenom + ' ' + nom + " (Tél. " + tel + ") " + adresse + ", " + ville)
        return True
        
def inserer(Nom, Prenom, Telephone, Adresse, Ville):
    '''comand for button "inserer"'''
    if not Nom.get(): #tester si nom est vide
        vue.afficheWarning("Champ \"Nom\" vide: vous devez au minimum spécifier un nom")
        return False
    else:
        data = ( Prenom.get(), Telephone.get(), Adresse.get(), Ville.get())
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
    Nom.set('')
    Prenom.set('')
    Telephone.set('')
    Adresse.set('')
    Ville.set('')

def effacer(Nom, Prenom, Telephone, Adresse, Ville):
    '''comand for button "effacer"'''
    if tkinter.messagebox.askyesno("Voulez-vous vraiment tout effacer" + '\u00A0' + '?'):
        supprimer(Nom, Prenom, Telephone, Adresse, Ville)
               

        

        
