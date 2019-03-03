#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from tkinter import Tk, Label, Entry, Button, StringVar
import cmdControleurAnnuaire as ctrl


def installerComposants():
    
    global champNom
    Nom = StringVar()
    lab = Label(application, text = 'Nom').grid(row = 0, column = 0)
    champNom = Entry(application, textvariable = Nom).grid(row = 0, column = 1, padx = 5, pady = 5)
    ctrl.inserer(Nom)
    
    global champPrenom
    lab = Label(application, text = 'Prénom').grid(row = 1, column = 0)
    champPrenom = Entry(application).grid(row = 1, column = 1, padx = 5, pady = 5)

    global champTelephone
    lab = Label(application, text = 'Téléphone').grid(row = 2, column = 0)
    champTelephone = Entry(application).grid(row = 2, column = 1, padx = 5, pady = 5)
    
    global champAdresse
    lab = Label(application, text = 'Adresse').grid(row = 3, column = 0)
    champAdresse = Entry(application).grid(row = 3, column = 1, padx = 5, pady = 5)
    
    global champVille
    lab = Label(application, text = 'Ville').grid(row = 4, column = 0)
    champVille = Entry(application).grid(row = 4, column = 1, padx = 5, pady = 5)
    
    Button(application, text = 'Chercher', command = ctrl.chercher).grid(row = 6, column = 0)
    Button(application, text = 'Inserer', command = ctrl.inserer).grid(row = 6, column = 1)
    #Button(application, text = 'Effacer', command = ctrl.effacer).grid(row = 6, column = 2)
    
    
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