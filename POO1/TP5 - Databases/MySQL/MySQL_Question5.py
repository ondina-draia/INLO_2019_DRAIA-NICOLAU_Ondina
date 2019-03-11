## QUESTION 5: faire un script python afin de repondre a quelques questions

## Quelques exemples avec MySQL:
# - exemple 1: quels sont les noms des pilotes qui pilotent un avion au depart de Paris?
# - exemple 2: quelle est la capacite de chaque vol?
# - exemple 3: combien d'airbus contient la compagnie?

import mysql.connector

# Se connecter
monServeur = "dbs-perso.luminy.univmed.fr"
monLogin = "m18002965"
motDePasse = "mz!DYWYT"
connexion = mysql.connector.connect(host = monServeur, user = monLogin, password = motDePasse, database = monLogin)
curseur = connexion.cursor() # permet d'effectuer des requetes

# Verifier la base de donnee selectionee: ici on a deja selectionner notre base de donnee personelle
curseur.execute("select database()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Base de donnée selectionnée : ", row[0])

# Affiche toutes les tables de notre base de donnee
curseur.execute("show tables") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
for row in rows:
    print("Liste tables: ", row[0])

# Visualiser les colonnes de la tables "AVION"
curseur.execute("describe AVION") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
for row in rows:
    print("Table avion: ", row[0])

# Visualiser les colonnes de la tables "PILOTE"
curseur.execute("describe PILOTE") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
for row in rows:
    print("Table pilote: ", row[0])

# Visualiser les colonnes de la tables "VOL"
curseur.execute("describe VOL") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
for row in rows:
    print("Table vol: ", row[0])

# Exemple 1: quels sont les noms des pilotes qui pilotent un avion au depart de Paris?
curseur.execute("select P.NOM from PILOTE as P, VOL as V where V.PILOTE_ID=P.PILOTE_ID and VILLE_DEP='PARIS'") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
for row in rows:
    print("Pilotes au départ de Paris: ", row[0])

# Exemple 2: quelle est la capacite de chaque vol?
curseur.execute("select A.CAPACITE from AVION as A, VOL as V where A.AVION_ID=V.AVION_ID") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
for row in rows:
    print("Capacité des vols: ", row[0])

# Exemple 3: combien d'airbus contient la compagnie?
curseur.execute("select count(*) from AVION where TYPE like 'A%'") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
for row in rows:
    print("Nombre d'airbus: ", row[0])

# Se deconnecter
curseur.close()
connexion.close()

## NB: en passant par python pour acceder a MySQL, on ne peut pas afficher des tableaux,
## mais seulement un resultat par lignes (meme si on peut afficher plusieurs lignes).
