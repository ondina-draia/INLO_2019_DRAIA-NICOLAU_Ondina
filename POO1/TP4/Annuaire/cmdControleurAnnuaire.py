#!/usr/bin/python3
# -*- coding: utf-8 -*-

from modeleAnnuaire import ModeleAnnuaire
import cmdVueAnnuaire as vue
import tkinter.messagebox

repertoire = {} #le dictionnaire qui va contenir toutes les données de notre application annuaire
#data = vue.installerComposants(vue.champPrenom, vue.champTelephone, vue.champAdresse, vue.champVille) #afin de remplir le répertoire, on ajoute les informations complémentaires au nom

def chercher():
    #if not vue.Nom.get(): #tester si Nom est vide
        vue.afficheWarning("Champ \"Nom\" vide: Vous devez au minimum spécifier un nom")
        return False
    if not repertoire.estPresent(vue.Nom):
        vue.afficheWarning(vue.Nom + ": absent du répertoire")
        return False
    else:
        print('test')
    #repertoire.chercher(vue.Nom, data)

def inserer(Nom):
    if Nom == '':
    #if not vue.installerComposants.nom.get(): #tester si nom est vide
        vue.afficheWarning("Champ \"Nom\" vide: vous devez au minimum spécifier un nom")
        return False
    else:
        #repertoire.inserer(vue.Nom, data)
        tkinter.messagebox.showinfo(Nom +": ajouté au répertoire")

'''
def effacer():
    vue.Nom.get() = ''
    vue.Prenom.get() = ''
    vue.Telephone.get() = ''
    vue.Adresse.get() = ''
    vue.Ville.get() = ''
    '''

#def chercher(repertoire, nom):
#	"""
#	Strip name and return the information associated with name
#
#	@param repertoire: repertoire to read from
#	@type repertoire: dict
#	@param name: name to look for
#	@type name: string
#	@return: success/failure
#	@rtype: bool
#	"""
#	nom = nom.strip()
#	if nom == '':
#		vue.afficheWarning("Champ \"Nom\" vide: Vous devez au minimum spécifier un nom")
#		return False
#	if not repertoire.estPresent(nom):
#		vue.afficheWarning(nom + ": absent du répertoire")
#		return False
#	prenom, tel, adresse, ville = repertoire.chercher(nom)
#	vue.afficheMessage(prenom + ' ' + nom + " (Tél. " + tel + ") " + adresse + ", " + ville)
#	return True

#def commande_inconnue(commande):
#	vue.afficheWarning("commande inconnue: " + commande)

#def exit():
#	vue.afficheMessage("Au revoir")
#	sys.exit(0)

#def inserer(repertoire, reponse):
#	"""
#	Read reponse; If correctly formated, insert (firstname, tel, address, city) into repertoire[name]; Strip everything beforehand
#
#	@param repertoire: repertoire to insert into
#	@type repertoire: dict
#	@param reponse: 5-word string slash(/)-separated: "name / firstname / tel / address / city"
#	@type reponse: string
#	@return: success/failure
#	@rtype: bool
#	"""
#	coordonnees = reponse.split("/")
#	if len(coordonnees) != 5:
#		vue.afficheWarning("trop ou pas assez d'infos (5 infos demandées : nom/prenom/tel/adresse/ville )")
#		return False
#	nom, prenom, tel, address, ville = coordonnees
#	nom = nom.strip()
#	if nom == '':
#		vue.afficheWarning("Champ \"Nom\" vide: vous devez au minimum spécifier un nom")
#		return False
#	data = (prenom.strip(), tel.strip(), address.strip(), ville.strip())
#	repertoire.inserer(nom, data)
#	vue.afficheMessage(nom + " ajouté au répertoire")
#	return True

#if __name__ == '__main__':
#	repertoire = ModeleAnnuaire()
#	print("Commandes:\n- Insérer:  +nom/prenom/tel/adresse/ville\n- Chercher: ?nom\n- Quitter:  !")
#	while True:
#		reponse = input("> ")
#		if len(reponse) > 0:
#			commande = reponse.lstrip()[0]
#			if commande == '!':
#				exit()
#			elif commande == '+':
#				inserer(repertoire, reponse[1:])
#			elif commande == '?':
#				chercher(repertoire, reponse[1:])
#			else:
#				commande_inconnue(commande)

