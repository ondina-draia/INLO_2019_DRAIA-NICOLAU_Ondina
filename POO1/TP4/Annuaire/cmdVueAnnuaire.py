#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import Tk, Label, Entry, Button, StringVar, Menu
import cmdControleurAnnuaire as ctrl

def installerComposants():
    
    #view for "Nom" button
    global champNom
    Nom = StringVar()
    lab = Label(application, text = 'Nom').grid(row = 0, column = 0)
    champNom = Entry(application, textvariable = Nom).grid(row = 0, column = 1, padx = 5, pady = 5)
    
    #view for "Prenom" button
    global champPrenom
    Prenom = StringVar()
    lab = Label(application, text = 'Prénom').grid(row = 1, column = 0)
    champPrenom = Entry(application, textvariable = Prenom).grid(row = 1, column = 1, padx = 5, pady = 5)
    
    #view for "Telephone" button
    global champTelephone
    Telephone = StringVar()
    lab = Label(application, text = 'Téléphone').grid(row = 2, column = 0)
    champTelephone = Entry(application, textvariable = Telephone).grid(row = 2, column = 1, padx = 5, pady = 5)
    
    #view for "Adresse" button
    global champAdresse
    Adresse = StringVar()
    lab = Label(application, text = 'Adresse').grid(row = 3, column = 0)
    champAdresse = Entry(application, textvariable = Adresse).grid(row = 3, column = 1, padx = 5, pady = 5)
    
    #view for "Ville" button
    global champVille
    Ville = StringVar()
    lab = Label(application, text = 'Ville').grid(row = 4, column = 0)
    champVille = Entry(application, textvariable = Ville).grid(row = 4, column = 1, padx = 5, pady = 5)
    
    #linking command functions to pressing the buttons
    Button(application, text = 'Chercher', command = lambda: ctrl.chercher(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 0)
    Button(application, text = 'Inserer', command = lambda: ctrl.inserer(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 1)
    Button(application, text = 'Effacer', command = lambda: ctrl.effacer(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 2)
    
    #view for menu
    barreDeMenus = Menu(application) #menu-bar contains: "Fichier" and "Aide"
    application.config(menu = barreDeMenus)
    
    menuFichier = Menu(barreDeMenus) #in menu "Fichier" contains: "Nouveau", "Ouvrir", "Enregustrer sous..." and "Quitter"
    barreDeMenus.add_cascade(label = "Fichier", menu = menuFichier)
    menuFichier.add_command(label = "Nouveau", command = lambda: ctrl.effacer(Nom, Prenom, Telephone, Adresse, Ville))
    menuFichier.add_command(label="Ouvrir...", command = ctrl.restaurer)
    menuFichier.add_command(label="Enregistrer sous...", command = ctrl.enregistrer)
    menuFichier.add_separator()
    menuFichier.add_command(label="Quitter", command = lambda: ctrl.quitter(application))
    
    menuAide = Menu(barreDeMenus)
    barreDeMenus.add_cascade(label="Aide", menu=menuAide) #in menu "Aide" contains: "A propos"
    menuAide.add_command(label="À propos", command = ctrl.propos)
    
    
def afficheMessage(s):
	print(s)

def afficheWarning(s):
	print(s, file=sys.stderr)


if __name__ == '__main__':
    application = Tk()
    application.title("Annuaire")
    installerComposants()
    application.mainloop()