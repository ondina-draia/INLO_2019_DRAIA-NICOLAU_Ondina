import mysql.connector

#Se connecter a la base de donnees 
monServeur = "ensembldb.ensembl.org" 
monLogin = "anonymous" 
connexion = mysql.connector.connect(host = monServeur, user = monLogin) 
curseur = connexion.cursor() # permet d'effectuer des requetes 

#verifie la version utilisee
curseur.execute("select version()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Version du serveur MySQL distant : ", row[0]) 

#verifie le serveur utilise
curseur.execute("select now()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Date actuelle sur le serveur distant : ", row[0]) 

#verifie la date de connexion
curseur.execute("select user()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print(type(row)) #fetchone c'est un tuple (une ligne de la table)
print("Date actuelle sur le serveur distant : ", row[0]) 

#verifie la base de donnee selectionee: ici aucune pour l'instant
curseur.execute("select database()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Base de donnée selectionnée : ", row[0]) 


## QUESTION 2

#affiche toutes les bases de donnes presentes
curseur.execute("show databases") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Liste des bases de données: ", row[0]) 

#affiche toutes les bases de donnes contenant "homo_sapiens_core_"
curseur.execute("show databases like '%homo_sapiens_core_%'") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Bases de données intéressantes: ", row[0])


## QUESTION 3

#affiche la base de donnee Humaine la plus recente
curseur.execute("use homo_sapiens_core_95_38") #exécuter la base qu'on veut selectionner

curseur.execute("select database()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Base de donnée selectionnée : ", row[0])  #mtn ça affiche qu'elle est la base de donnee qui est selectionnée

# Pour selectionnner la base de donnee de facon automatique, on avait pense a faire une boucle:
# depuis la liste de toutes les "bases de donnees interessantes" on voulait selectionner la derniere
# (soit la plus recente) mais cela ne marchait pas car il s'agissait d'un tuple.


## QUESTION 4 il faut utiliser gene-id et transcript_id (clé primaire)

#affiche toutes les tables de notre base de donnee
curseur.execute("show tables") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Liste tables: ", row[0]) 

##decrit le contenu de la table gene
curseur.execute("describe transcript") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Table transcript: ", row[0])

#selectionne le gene avec le plus de transcrit
curseur.execute("select transcript_id from transcript where gene_id = (select max(gene_id) from transcript)") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Nombre de transcrits: ", row[0]) 


## QUESTION 5

curseur.close()
connexion.close()