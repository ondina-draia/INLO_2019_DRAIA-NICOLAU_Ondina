#!/usr/bin/python3
# -*- coding: utf-8 -*-

from modeleAnnuaire import ModeleAnnuaire
import cmdVueAnnuaire as vue
import tkinter.messagebox, tkinter.filedialog

repertoire_global = ModeleAnnuaire() #variable storing the data of the application


def chercher(Nom, Prenom, Telephone, Adresse, Ville):
    '''comand for button "chercher"
    look for a contact using "Nom"'''
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
    '''comand for button "inserer"
    add a contact: "Nom" needs to be specified'''
    
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
    '''command for button "effacer"
    delete values from all fields'''
    
    if tkinter.messagebox.askyesno("Attention",
            "Voulez-vous vraiment tout effacer" + '\u00A0' + '?'): #message box to check if user really wants to delete values from fields
        supprimer(Nom, Prenom, Telephone, Adresse, Ville) #delete values from fields


def enregistrer():
    '''command for "Enregistrer sous..." in menu (in "Fichier")
    save data in a file'''
    
    tkinter.messagebox.showwarning("Excuses...",
            "La fonction 'enregistrer' n'est pas encore implémentée") 

    #fichier = tkinter.filedialog.asksaveasfile()
    #if fichier == None:
    #    return
    #print(file = repertoire_global)
    #fichier.close()
    
    # AttributeError: 'ModeleAnnuaire' object has no attribute 'write'
    # Tichit advice: utilisez soit un fichier texte et un parser, soit le module pickle
       
                                                                             
def restaurer():
    '''command for "Ouvrir" in menu (in "Fichier")
    open saved data from a file'''
    
    tkinter.messagebox.showwarning("Excuses...",
            "La fonction 'restaurer' n'est pas encore implémentée")
    
    #fichier = tkinter.filedialog.askopenfile()
    #if fichier == None:
    #    return

def quitter(application):
    '''command for "quitter" in menu (in "Fichier")
    exit button for application'''
    
    #from tkinter import Tk
    if tkinter.messagebox.askyesno("Attention",
            "Vous voulez vraiment quitter ce programme" + '\u00A0' + "?"):
        application.destroy() #destroy graphical view


def propos():
    '''command for "A propos" in menu (in "Aide")
    description of the application'''
    
    tkinter.messagebox.showinfo(
            "À propos de...",
            "Annuaire\n\n" +
            "un annuaire basique pour créer un répertoire\n" +
            "et chercher des contacts dans ce répertoire avec Tkinter    \n\n"  +
            "(C) 2019 O. Draia-Nicolau & M. Murray")
