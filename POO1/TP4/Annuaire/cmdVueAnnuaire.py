#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import Tk, Label, Entry, Button, StringVar, Menu
import cmdControleurAnnuaire as ctrl

def installerComposants():
    
    #view for "Nom" button
    global champNom #allows updates of "champNom"
    Nom = StringVar() #allows different entries in entry field "Nom"
    lab = Label(application, text = 'Nom').grid(row = 0, column = 0) #to know where to enter "Nom"
    champNom = Entry(application, textvariable = Nom).grid(row = 0, column = 1, padx = 5, pady = 5) #create the field where value can be entered
    
    #view for "Prenom" button
    global champPrenom #allows updates of "chamPrenom"
    Prenom = StringVar() #allows different entries in entry field "Prenom"
    lab = Label(application, text = 'Prénom').grid(row = 1, column = 0) #to know where to enter "Prenom"
    champPrenom = Entry(application, textvariable = Prenom).grid(row = 1, column = 1, padx = 5, pady = 5) #create the field where value can be entered
    
    #view for "Telephone" button
    global champTelephone #allows updates of "champTelephone"
    Telephone = StringVar() #allows different entries in entry field "Telephone"
    lab = Label(application, text = 'Téléphone').grid(row = 2, column = 0) #to know where to enter "Telephone"
    champTelephone = Entry(application, textvariable = Telephone).grid(row = 2, column = 1, padx = 5, pady = 5) #create the field where value can be entered
    
    #view for "Adresse" button
    global champAdresse  #allows updates of "champAdresse"
    Adresse = StringVar() #allows different entries in entry field "Adresse"
    lab = Label(application, text = 'Adresse').grid(row = 3, column = 0) #to know where to enter "Adresse"
    champAdresse = Entry(application, textvariable = Adresse).grid(row = 3, column = 1, padx = 5, pady = 5) #create the field where value can be entered
    
    #view for "Ville" button
    global champVille  #allows updates of "champVille"
    Ville = StringVar() #allows different entries in entry field "Ville"
    lab = Label(application, text = 'Ville').grid(row = 4, column = 0) #to know where to enter "Ville"
    champVille = Entry(application, textvariable = Ville).grid(row = 4, column = 1, padx = 5, pady = 5) #create the field where value can be entered
    
    #linking command functions to pressing the buttons: buttons "Chercher", "Inserer" and "Effacer"
    Button(application, text = 'Chercher', command = lambda: ctrl.chercher(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 0)
    Button(application, text = 'Inserer', command = lambda: ctrl.inserer(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 1)
    Button(application, text = 'Effacer', command = lambda: ctrl.effacer(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 2)
    
    #view for menu and linking commands to action
    barreDeMenus = Menu(application) #menu-bar contains: "Fichier" and "Aide"
    application.config(menu = barreDeMenus)
    
    menuFichier = Menu(barreDeMenus) #in menu "Fichier" contains: "Nouveau", "Ouvrir", "Enregustrer sous..." and "Quitter"
    barreDeMenus.add_cascade(label = "Fichier", menu = menuFichier)
    menuFichier.add_command(label = "Nouveau", command = lambda: ctrl.effacer(Nom, Prenom, Telephone, Adresse, Ville)) #use of function "effacer" in ctrl when "Nouveau" is selected
    menuFichier.add_command(label="Ouvrir...", command = ctrl.restaurer) #use of function "restaurer" in ctrl when "Ourvrir" is selected
    menuFichier.add_command(label="Enregistrer sous...", command = ctrl.enregistrer) #use of function "enregistrer" in ctrl when "Enregister sous..." is selected
    menuFichier.add_separator() #adds doted line between "Enregister sous..." and "Quitter"
    menuFichier.add_command(label="Quitter", command = lambda: ctrl.quitter(application)) #use of function "quitter" in ctrl when "Quitter" is selected
    
    menuAide = Menu(barreDeMenus)
    barreDeMenus.add_cascade(label="Aide", menu=menuAide) #in menu "Aide" contains: "A propos"
    menuAide.add_command(label="À propos", command = ctrl.propos) #use of function "propos" in "ctrl"
    
    
def afficheMessage(s): #not error messages
	print(s)

def afficheWarning(s): #error messages
	print(s, file=sys.stderr)


if __name__ == '__main__':
    application = Tk() #use of tkinter
    application.title("Annuaire") #gives a name to the application
    installerComposants() #summons function "installerComposants"
    application.mainloop() #launches the application
