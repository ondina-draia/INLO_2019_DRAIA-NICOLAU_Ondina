# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 14:13:31 2019

@author: castr
"""

import sqlite3
conn = sqlite3.connect('ma_base.db')
#conn = sqlite3.connect(':memory:') Cela permet de ne travailler qu’en mémoire principale, sans création de fichier sur le disque (2).
cursor = conn.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT,
        age INTEGER
)
""")
conn.commit()

cursor.execute("""INSERT INTO users(name, age) VALUES(?, ?)""",
("olivier", 30))
conn.commit()

data = {"name" : "clara", "age" : 31} # insertion avec une syntaxe differente (3)
cursor.execute("""INSERT INTO users(name, age) VALUES(:name, :age)""",
data)
conn.commit()

#Insertion en bloc (5)
users = []
users.append(("olivier", 30))
users.append(("jean-louis", 90))
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)
conn.commit()

# Récupération du dernier id (4)
id1 = cursor.lastrowid
print('dernier id: %d' % id1)

#Affichage du résultat d’une requête à résultat unique (6)
cursor.execute("""SELECT name, age FROM users""")
user1 = cursor.fetchone()
print(user1)

#Affichage du résultat d’une requête retournant plusieurs enregistrements (7)
cursor.execute("""SELECT id, name, age FROM users""")
rows = cursor.fetchall()
for row in rows:
    print('{0} : {1} - {2}'.format(row[0], row[1], row[2]))
    
#Modification d'un enregistrement (8)
id1 = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id1, ))
response = cursor.fetchone()
print(response)
cursor.execute("""UPDATE users SET age = ? WHERE id = 2""", (31, ))
conn.commit()
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id1, ))
response = cursor.fetchone()
print(response)

#Rollback: revenir au commit anterieur(9)
conn.rollback()
id = 2
cursor.execute("""SELECT id, name FROM users WHERE id=?""", (id,))
response = cursor.fetchone()

#suppression de la table (10)
cursor = conn.cursor()
cursor.execute("""DROP TABLE users""")
conn.commit()
    
conn.close()

#Remarques:
#création du fichier ma_base_db sur votre disque dur. Il contient l’intégralité de vos tables, index et données
#dans le repertoire courant

#curseur est un objet permettant d'exécuter des requêtes et de stocker les résultats. Si on
#veut conserver les résultats de différentes requêtes on peut créer différents curseurs

#la notion de commit. Aucune requête modifiant la base de données n’est exécutée
#réellement tant qu’un commit n’a pas eu lieu. Le système de commit permet de pouvoir
#revenir dans un état antérieur de la base de données en cas de problème.  