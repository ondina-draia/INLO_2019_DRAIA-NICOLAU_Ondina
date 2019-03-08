import mysql.connector
 
monServeur = "ensembldb.ensembl.org" 
monLogin = "anonymous" 
connexion = mysql.connector.connect(host = monServeur, user = monLogin) 
curseur = connexion.cursor() # permet d'effectuer des requetes 

curseur.execute("select version()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Version du serveur MySQL distant : ", row[0]) 

curseur.execute("select now()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Date actuelle sur le serveur distant : ", row[0]) 


curseur.execute("select user()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print(type(row)) #fetchone c'est un tuple (une ligne de la table)
print("Date actuelle sur le serveur distant : ", row[0]) 


curseur.execute("select database()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Base de donnée selectionnée : ", row[0]) 

#Question 2
curseur.execute("show databases") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print(row[0]) 

curseur.execute("show databases like '%homo_sapiens_core%'") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print(row[0])

##Question 3
#Je ne sais pas comment sélectionner de façon automatique la derniere version de la base de donnee
curseur.execute("use homo_sapiens_core_95_38") #exécuter la base qu'on veut selectionner

curseur.execute("select database()") # ne retourne qu’une seule ligne 
row = curseur.fetchone() # on recupere la ligne resultat 
print("Base de donnée selectionnée : ", row[0])  #mtn ça affiche qu'elle est la base de donnee qui est selectionnée


#Question 4 il faut utiliser gene-id et transcript_id (clé primaire)
curseur.execute("show tables") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print(row[0]) 

#Decrit le contenu de la table gene
curseur.execute("describe gene") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print(row[0])   

#Decrit le contenu de la table transcript
curseur.execute("describe transcript") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print(row[0])  

#Lister tous les transcripts du gene ayant le plus de transcripts
#Probleme avec ça, je ne suis pas certaine de la syntaxe et d'avoir compris ce qu'il demande d'autant plus que le programme ne tourne pas
curseur.execute("select transcript_id, gene_id from transcript where gene_id= (select MAX(transcript_id) from transcript);") # retourne plusieurs lignes 
rows = curseur.fetchall() # on recupere les lignes resultat 
print(type(rows)) #fetchall c'est une liste de tuple (toute la table)
for row in rows:
    print(row[0])  


#Question 5

curseur.close()
connexion.close()

