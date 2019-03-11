# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:55:57 2019

@author: DRAIA-NICOLAU Ondina
"""

#Devoir Maison. Effectuez une requête vers ENSEMBL (ou vers votre propre base de données
#MySQL à l’université) en utilisant SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy import and_
from sqlalchemy.sql import select, text
import pymysql

db = pymysql.connect("ensembldb.ensembl.org","anonymous","","homo_sapiens_core_95_38" )
cursor = db.cursor()
cursor.execute("select * from gene limit 10;")
myresults = cursor.fetchall()
for x in myresults:
    print(*x)
cursor.close()
db.close()