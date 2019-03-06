# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:45:55 2019

@author: Draia-Nicolau Ondina
"""

#Python-MySQL

#!/usr/bin/python3
import mysql.connector

monServeur = "ensembldb.ensembl.org"
monLogin = "anonymous"
connexion = mysql.connector.connect(host = monServeur, user = monLogin)
curseur = connexion.cursor() # permet d'effectuer des requetes
curseur.execute("select version()") # ne retourne qu’une seule ligne
row = curseur.fetchall() # on recupere la ligne resultat
print("Version du serveur MySQL distant : ", row[0])
curseur.execute("select now()") # ne retourne qu’une seule ligne
rows = curseur.fetchall() # on recupere la ligne resultat
for row in rows:
    print("%s" % row[0])
    print("%d lignes renvoyées" % len(rows))
print("Date actuelle sur le serveur distant : ", row[0])

curseur.execute("show databses like '%sapiens_core%'") 
rows = curseur.fetchall()
print(rows)
curseur.close()
connexion.close()
    