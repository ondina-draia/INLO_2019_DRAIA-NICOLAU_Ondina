# Etape 17 But : écrire la fonction de restauration, qui
#reconstruit un graphe à partir de sa description enregistrée dans un fichier à l'aide de la fonction précédente.

from tkinter import Tk, Frame, Canvas, Label, Button, Radiobutton, Listbox, \
        Menu, StringVar, RIGHT, BOTH, TOP, X, Y, W, BOTTOM, RIDGE, SUNKEN, END
import tkinter.messagebox
import tkinter.simpledialog
import tkinter.filedialog 
import sys                                                         

CREATION_SOMMET      = "Création de sommet : cliquez pour désigner l'emplacement"
DEBUT_CREATION_ARETE = "Création d'arête : cliquez pour désigner l'origine"
SUITE_CREATION_ARETE = "Création d'arête (suite) : désignez l'extremité"             
DEFINITION_ETIQUETTE = "Définition d'étiquette : désignez le sommet"

R = 3                       # rayon des sommets
COULEUR_SOMMET = "black"    # couleur des sommets
COULEUR_SOMMET2 = "red"     # couleur des sommets mis en évidence

sommetEnDeplacement = None  # (parfois) sommet en cours d'être déplacé

                            # trois dictionnaires:
attributs = { }             # associe à chaque sommet les arêtes attenantes
                            # (avec un premier élément expliqué plus tard)
extremites = { }            # associe à chaque arête ses deux extrémités

sommetAssocie = { }         # associe à chaque étiquette le sommet correspondant

nombreSommets = 0           # nombre de sommets créés
nombreAretes = 0            # nombre d'aretes créées

application = Tk()
application.title("Edigraph")

etatCourant = StringVar(application)
etatCourant.set(CREATION_SOMMET)

def sommetVoisin(x, y):
        # on recherche un objet dessiné dans le canevas près de (x, y)
    pres = 10
    objets = canevas.find_enclosed(x - pres, y - pres, x + pres, y + pres)
    for o in objets:                  # on passe en revue les objets
        if canevas.type(o) == 'oval': # jusqu'à trouver un ovale
            return o                  # on prend le premier
    return None

def rafraichirCompteurs(nSommets, nAretes):
    global nombreSommets, nombreAretes

    nombreSommets = nSommets
    nombreAretes = nAretes
    etiqNbrSommets.config(text = str(nombreSommets) + " sommets")
    etiqNbrAretes.config(text = str(nombreAretes) + " arêtes")

def creationSommet(x, y):
    sommet = canevas.create_oval(x - R, y - R, x + R, y + R,
                fill = COULEUR_SOMMET, width = 0)
    s = str(nombreSommets)                                                           
    etiquette = canevas.create_text(x + 2 * R, y - R, text = s, anchor=W)            
    attributs[sommet] = [ etiquette ]   # au lieu de "garde-place"                   

    rafraichirCompteurs(nombreSommets + 1, nombreAretes)

def creationArete(orig, extr):
    x0, y0 = centre(orig)
    x1, y1 = centre(extr)
    arete = canevas.create_line(x0, y0, x1, y1)

    extremites[arete] = (orig, extr)
    attributs[orig].append(arete)
    attributs[extr].append(arete)

    rafraichirCompteurs(nombreSommets, nombreAretes + 1)

def cocheCaseCreationSommet():
    barreEtat.config(text=CREATION_SOMMET)

def cocheCaseCreationArete():
    barreEtat.config(text=DEBUT_CREATION_ARETE)

def cocheCaseDefEtiquette():
    barreEtat.config(text=DEFINITION_ETIQUETTE)

def centre(sommet):
    a, b, c, d = canevas.coords(sommet)
    return (a + c) / 2, (b + d) / 2

def definitionEtiquette(sommet):
    etiquette = attributs[sommet][0]
    texte = canevas.itemcget(etiquette, "text")
    if not texte.isdigit():
        tkinter.messagebox.showwarning("Définition étiquette",
                "L'etiquette de ce sommet a déjà été définie")
    else:
        texte = tkinter.simpledialog.askstring("Étiquette",
                "Donner la nouvelle valeur" + '\u00A0' + ':', initialvalue = texte)
        if texte != None:
            canevas.itemconfigure(etiquette, text = texte)
            listeEtiquettes.insert(END, texte)
            sommetAssocie[texte] = sommet

def pressionBoutonGauche(event):
    global sommetSelectionne

    if etatCourant.get() == CREATION_SOMMET:
        creationSommet(event.x, event.y)

    elif etatCourant.get() == DEBUT_CREATION_ARETE:
        s = sommetVoisin(event.x, event.y)
        if s != None:
            sommetSelectionne = s
            etatCourant.set(SUITE_CREATION_ARETE)
            barreEtat.config(text=SUITE_CREATION_ARETE)

    elif etatCourant.get() == SUITE_CREATION_ARETE:
        s = sommetVoisin(event.x, event.y)
        if s != None:
            creationArete(sommetSelectionne, s)
            etatCourant.set(DEBUT_CREATION_ARETE)
            barreEtat.config(text=DEBUT_CREATION_ARETE)

    else: # etatCourant.get() == ETAT_DEFINITION_ETIQUETTE
        s = sommetVoisin(event.x, event.y)
        if s != None:
            definitionEtiquette(s)

def replacer(arete):
    sommet0, sommet1 = extremites[arete]
    x0, y0 = centre(sommet0)
    x1, y1 = centre(sommet1)
    canevas.coords(arete, x0, y0, x1, y1)

def deplacementSommet(x, y):
    canevas.coords(sommetEnDeplacement, x - R, y - R, x + R, y + R)
    liste = attributs[sommetEnDeplacement]
    canevas.coords(liste[0], x + 2 * R, y - R)
    for arete in liste[1:]:
        replacer(arete)

def pressionBoutonDroit(event):
    global sommetEnDeplacement
    s = sommetVoisin(event.x, event.y)
    if s != None:
        sommetEnDeplacement = s

def mouvementBoutonDroit(event):
    if sommetEnDeplacement != None:
        deplacementSommet(event.x, event.y)

def relachementBoutonDroit(event):
    global sommetEnDeplacement
    sommetEnDeplacement = None

def toutEffacer():
    canevas.addtag_all("a_effacer")
    canevas.delete("a_effacer")
    rafraichirCompteurs(0, 0)

def pressionBoutonEffacer():
    if tkinter.messagebox.askyesno("Attention",
            "Vous voulez vraiment tout détruire" + '\u00A0' + '?'):
        toutEffacer()

def actionSurListe(evt):
    selections = listeEtiquettes.curselection()  # ex.: ("3", "5", "9")
    selection = selections[0]                    # ex.: "3"
    i = int(selection)                           # ex.: 3
    texte = listeEtiquettes.get(i)               # le texte correspondant
    sommet = sommetAssocie[texte]                # le sommet correspondant

    if canevas.itemcget(sommet, "fill") == COULEUR_SOMMET:
        canevas.itemconfigure(sommet, fill=COULEUR_SOMMET2)
    else:
        canevas.itemconfigure(sommet, fill=COULEUR_SOMMET)

def comMenuQuitter():
    if tkinter.messagebox.askyesno("Attention",
            "Vous voulez vraiment quitter ce programme" + '\u00A0' + "?"):
        sys.exit(0)

def comMenuAPropos():
    tkinter.messagebox.showinfo(
            "À propos de...",
            "Edigraph\n\n" +
            "un éditeur de graphes purement démonstratif\n" +
            "de la réalisation des interfaces graphiques avec Tkinter    \n\n"  +
            "(C) 2005-2017 H. Garreta & L. Tichit")

def enregistrerGraphe():                                                            
    fichier = tkinter.filedialog.asksaveasfile()                                    
    if fichier == None:                                                             
        return                                                                      
                                                                                    
    liste = canevas.find_all()                                                      
    for item in liste:                                                              
        if canevas.type(item) == "oval":                                            
            dep = attributs[item]                                                   
            print('"' + canevas.itemcget(dep[0], "text") + '"',                     
                  file=fichier, end=' ')                                            
            print(centre(item), file=fichier, end=' ')                              
            for arete in dep[1:]:                                                   
                voisin = extremites[arete][0]                                       
                if voisin == item:                                                  
                    voisin = extremites[arete][1]                                   
                s = canevas.itemcget(attributs[voisin][0], "text")                  
                print('"' + s + '"', file=fichier, end=' ')                         
            print(file=fichier)                                                     
                                                                                    
    fichier.close()                                                                 

def restaurerGraphe():
    fichier = tkinter.filedialog.askopenfile()
    if fichier == None:
        return
    lst_coord = []
    lst_etiquettes = []
#    dict_etiq_coord = {}
    for line in fichier:
        import re
        coord = re.findall("([0-9]*[\.0][0-9\.0])", line) #recupere les coordonnees 
        lst_coord.append(coord)
        print(coord)
        connexion = re.findall("[\"][A-Za-z0-9]*[\"]",line) #recupere les etiquettes
        connexion = [c.strip('"') for c in connexion]
        lst_etiquettes.append(connexion)
        print(connexion)
        creationSommet(float(coord[0]),float(coord[1])) #cree les sommets
    
    for i in range(len(lst_coord)-1):
        canevas.create_line(lst_coord[i][0],lst_coord[i][1], lst_coord[i+1][0], lst_coord[i+1][1]) #prototype: cree des arretes
    
        

barreEtat = Label(application, text=CREATION_SOMMET,
            bd=1, relief=SUNKEN, anchor=W)
barreEtat.pack(side=BOTTOM, fill=X)

canevas = Canvas(application, bg="#C8FFFF", width=400, height=400)
canevas.pack(side=RIGHT, fill=BOTH, expand=True, padx=2, pady=2)

canevas.bind("<Button-1>", pressionBoutonGauche)
canevas.bind("<Button-3>", pressionBoutonDroit)
canevas.bind("<Motion>", mouvementBoutonDroit)
canevas.bind("<ButtonRelease-3>", relachementBoutonDroit)

panneauSup = Frame(application, width=150, height = 200,
            padx=4, pady=4, bd=2, relief = RIDGE)
panneauSup.pack(side=TOP)

lab = Label(panneauSup, text="Bouton gauche :")
lab.grid(row=0, sticky=W)

rb = Radiobutton(panneauSup, variable=etatCourant, text="Création sommet",
                value=CREATION_SOMMET, command=cocheCaseCreationSommet)
rb.grid(row=1, sticky=W)
rb = Radiobutton(panneauSup, variable=etatCourant, text="Création arête",
                value=DEBUT_CREATION_ARETE, command=cocheCaseCreationArete)
rb.grid(row=2, sticky=W)
rb = Radiobutton(panneauSup, variable=etatCourant, text="Définition étiquette",
                value=DEFINITION_ETIQUETTE, command=cocheCaseDefEtiquette)
rb.grid(row=3, sticky=W)

bouton = Button(panneauSup, text="Tout effacer", command=pressionBoutonEffacer)
bouton.grid(row=4)

panneauInf = Frame(application)
panneauInf.pack(side=BOTTOM, fill=BOTH, expand=True)

etiqNbrAretes = Label(panneauInf)
etiqNbrAretes.pack(side=BOTTOM, anchor=W)
etiqNbrSommets = Label(panneauInf)
etiqNbrSommets.pack(side=BOTTOM, anchor=W)

rafraichirCompteurs(0, 0)

lab = Label(panneauInf, text="Étiquettes :")
lab.pack(side=TOP, anchor=W)

listeEtiquettes = Listbox(panneauInf)
listeEtiquettes.pack(side=BOTTOM, fill=Y, expand=True)
listeEtiquettes.bind("<Double-Button-1>", actionSurListe)

barreDeMenus = Menu(application)
application.config(menu = barreDeMenus)

menuFichier = Menu(barreDeMenus)
barreDeMenus.add_cascade(label="Fichier", menu=menuFichier)

menuFichier.add_command(label="Nouveau", command=pressionBoutonEffacer)
menuFichier.add_command(label="Ouvrir...", command=restaurerGraphe)
menuFichier.add_command(label="Enregistrer sous...", command=enregistrerGraphe)
menuFichier.add_separator()
menuFichier.add_command(label="Quitter", command=comMenuQuitter)

menuAide = Menu(barreDeMenus)
barreDeMenus.add_cascade(label="Aide", menu=menuAide)

menuAide.add_command(label="À propos", command=comMenuAPropos)

application.mainloop()