# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 11:26:57 2019

@author: Draia-Nicolau Ondina
"""
#Devoir Maison. Modifiez le modèle du carnet d’adresse afin que les données soient insérées et
#récupérées depuis une base de données (SQLite ou MySQL) par l’intermédiaire de SQLAlchemy

#Creation d'une base de données comprenant les donnees d'un annuaire 

import sqlite3
conn = sqlite3.connect('annuaire.db')
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
        nom TEXT PRIMARY KEY,
        prenom TEXT,
        adresse TEXT,
        ville TEXT,
        telephone INTEGER
        
)
""")
conn.commit()

#Insertion d'un user dans l'annuaire
cursor.execute("""INSERT INTO users(nom, prenom, adresse, ville, telephone) VALUES(?, ?, ?, ?, ?)""",
("Lebowski","Jeffrey", "10231 Charing Cross Road", "Los Angeles", "0765895677"))
conn.commit()

#Insertion en bloc d'autre users dans l'annuaire (5)
users = []
users.append(("larson","olivier","15rue de la folie", "suce-sur-erdre", "0658547587"))
users.append(("jean-louis", "louis-jean", "90, chemin de la bosse enchantee", "barcelone", "078483186"))
cursor.executemany("""
INSERT INTO users(nom, prenom, adresse, ville, telephone) VALUES(?, ?, ?, ?, ?)""", users)
conn.commit()

#Ensuite modifier code du modele afin qu'il prenne en compte ces donnees par l'intermediare de sqlalchemy