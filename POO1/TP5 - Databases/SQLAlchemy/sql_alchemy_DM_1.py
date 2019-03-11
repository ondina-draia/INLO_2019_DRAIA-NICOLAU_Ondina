# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:55:57 2019

@author: DRAIA-NICOLAU Ondina
"""

#Devoir Maison. Effectuez une requête vers ENSEMBL (ou vers votre propre base de données
#MySQL à l’université) en utilisant SQLAlchemy

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://anonymous@ensembldb.ensembl.org/homo_sapiens_core_95_38", echo=True)
conn = engine.connect()

from sqlalchemy.sql import select, text
s = select([text("* from gene limit 10;")]) 
result = conn.execute(s).fetchall()
print(result)

