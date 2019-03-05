#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import Tk, Label, Entry, Button, StringVar
import cmdControleurAnnuaire as ctrl


def installerComposants():
    
    global champNom #view for "Nom" button
    Nom = StringVar()
    lab = Label(application, text = 'Nom').grid(row = 0, column = 0)
    champNom = Entry(application, textvariable = Nom).grid(row = 0, column = 1, padx = 5, pady = 5)
    
    global champPrenom #view for "Prenom" button
    Prenom = StringVar()
    lab = Label(application, text = 'Prénom').grid(row = 1, column = 0)
    champPrenom = Entry(application, textvariable = Prenom).grid(row = 1, column = 1, padx = 5, pady = 5)

    global champTelephone #view for "Telephone" button
    Telephone = StringVar()
    lab = Label(application, text = 'Téléphone').grid(row = 2, column = 0)
    champTelephone = Entry(application, textvariable = Telephone).grid(row = 2, column = 1, padx = 5, pady = 5)
    
    global champAdresse #view for "Adresse" button
    Adresse = StringVar()
    lab = Label(application, text = 'Adresse').grid(row = 3, column = 0)
    champAdresse = Entry(application, textvariable = Adresse).grid(row = 3, column = 1, padx = 5, pady = 5)
    
    global champVille #view for "Ville" button
    Ville = StringVar()
    lab = Label(application, text = 'Ville').grid(row = 4, column = 0)
    champVille = Entry(application, textvariable = Ville).grid(row = 4, column = 1, padx = 5, pady = 5)
    
    #linking command functions to pressing the buttons
    Button(application, text = 'Chercher', command = lambda: ctrl.chercher(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 0)
    Button(application, text = 'Inserer', command = lambda: ctrl.inserer(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 1)
    Button(application, text = 'Effacer', command = lambda: ctrl.effacer(Nom, Prenom, Telephone, Adresse, Ville)).grid(row = 6, column = 2)
    
    
def afficheMessage(s):
	print(s)

def afficheWarning(s):
	print(s, file=sys.stderr)

#barreDeMenus = Menu(application)
#application.config(menu = barreDeMenus)
#menuFichier = Menu(barreDeMenus)
#barreDeMenus.add_cascade(label="Fichier", menu=menuFichier)
#menuFichier.add_command(label="Nouveau", command=pressionBoutonEffacer)
#menuFichier.add_command(label="Ouvrir...", command=restaurerGraphe)
#menuFichier.add_command(label="Enregistrer sous...", command=enregistrerGraphe)
#menuFichier.add_command(label="Quitter", command=comMenuQuitter)

if __name__ == '__main__':
    application = Tk()
    application.title("Annuaire")
    installerComposants()
    application.mainloop()