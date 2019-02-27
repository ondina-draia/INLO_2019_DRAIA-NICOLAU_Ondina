import sys
from tkinter import Tk, Label, Entry, Button

def installerComposants():
    
    global champNom
    lab = Label(application, text = 'Nom')
    lab.grid(row = 0, column = 0)
    champNom = Entry(application)
    champNom.grid(row = 0, column = 1, padx = 5, pady = 5)
    
    global champPrenom
    lab = Label(application, text = 'Prénom')
    lab.grid(row = 1, column = 0)
    champPrenom = Entry(application)
    champPrenom.grid(row = 1, column = 1, padx = 5, pady = 5)

    global champTelephone
    lab = Label(application, text = 'Téléphone')
    lab.grid(row = 2, column = 0)
    champTelephone = Entry(application)
    champTelephone.grid(row = 2, column = 1, padx = 5, pady = 5)
    
    global champAdresse
    lab = Label(application, text = 'Adresse')
    lab.grid(row = 3, column = 0)
    champAdresse = Entry(application)
    champAdresse.grid(row = 3, column = 1, padx = 5, pady = 5)
    
    global champVille
    lab = Label(application, text = 'Ville')
    lab.grid(row = 4, column = 0)
    champVille = Entry(application)
    champVille.grid(row = 4, column = 1, padx = 5, pady = 5)
    
    Button(application, text = 'Chercher').grid(row = 6, column = 0, columnspan = 1, padx = 2, pady = 2)
    Button(application, text = 'Inserer').grid(row = 6, column = 1, columnspan = 1, padx = 2, pady = 2)
    Button(application, text = 'Effacer').grid(row = 6, column = 2, columnspan = 1, padx = 2, pady = 2)
    
    
def afficheMessage(s):
	print(s)

def afficheWarning(s):
	print(s, file=sys.stderr)

if __name__ == '__main__':
    application = Tk()
    application.title("Annuaire")
    installerComposants()
    application.mainloop()