import mysql.connector

## QUESTION 1

# Se connecter a la base de donnees 
monServeur = "ensembldb.ensembl.org" 
monLogin = "anonymous" 
connexion = mysql.connector.connect(host = monServeur, user = monLogin) 
curseur = connexion.cursor() # permet d'effectuer des requetes 

# Verifie la version utilisee
curseur.execute("select version()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Version du serveur MySQL distant : ", row[0]) 

# Verifie le serveur utilise
curseur.execute("select now()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Date actuelle sur le serveur distant : ", row[0]) 

# Verifie la date de connexion
curseur.execute("select user()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print(type(row)) #fetchone c'est un tuple (une ligne de la table)
print("Date actuelle sur le serveur distant : ", row[0]) 

# Verifie la base de donnee selectionee: ici aucune pour l'instant
curseur.execute("select database()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Base de donnée selectionnée : ", row[0]) 


## QUESTION 2

# Affiche toutes les bases de donnes presentes
curseur.execute("show databases") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Liste des bases de données: ", row[0]) 

# Affiche toutes les bases de donnes contenant "homo_sapiens_core_"
curseur.execute("show databases like '%homo_sapiens_core\_%'") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Bases de données intéressantes: ", row[0])


## QUESTION 3

# Recupere automatiquement la base de donnee Huamine la plus recente
curseur.execute("show databases like '%homo_sapiens_core\_%'") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat
for row in rows:
    new = row[-1]
curseur.execute("use " + new) # ne retourne qu’une seule ligne 

# Verifie la base de donnee selectionee: maintenant la base de donnee Humaine la plus recente est selectionnee
curseur.execute("select database()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Base de donnée selectionnée : ", row[0]) 


## QUESTION 4

# Affiche toutes les tables de notre base de donnee
curseur.execute("show tables") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Liste tables: ", row[0]) 

# Decrit le contenu de la table gene
curseur.execute("describe transcript") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Table transcript: ", row[0])

# Selectionne le gene avec le plus de transcrit
curseur.execute("select transcript_id from transcript where gene_id = (select max(gene_id) from transcript)") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print("Nombre de transcrits: ", row[0]) 

# Se deconnecter de la base de donnee
curseur.close()
connexion.close()