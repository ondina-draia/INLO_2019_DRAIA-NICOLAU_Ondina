# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:37:36 2019

@author: castr
"""

#SQLAlchemy part 1

#Creation d'une table
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, ForeignKey, join, or_, asc
# Pour SQLite
engine = create_engine('sqlite:///college.db', echo=True)
# Pour MySQL
# engine = create_engine("mysql://user:passwd@localhost/college",echo=True)
meta = MetaData()
students = Table('students', meta,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('lastname', String), )
addresses = Table('addresses', meta,
                  Column('id', Integer, primary_key=True),
                  Column('st_id', Integer, ForeignKey('students.id')),
                  Column('postal_add', String),
                  Column('email_add', String))
meta.create_all(engine)

#Insertion de données
ins = students.insert().values(name='Ravi', lastname='Kapoor')
conn = engine.connect()
result = conn.execute(ins)

#Insertion de données multiples
conn.execute(students.insert(),
                     [ {'name':'Rajiv', 'lastname' : 'Khanna'},
                       {'name':'Komal','lastname' : 'Bhandari'},
                       {'name':'Abdul','lastname' : 'Sattar'},
                       {'name':'Priya','lastname' : 'Rajhans'},
                      ])

#Requête Select
s = students.select().where(students.c.id > 2)
result = conn.execute(s)
for row in result:
    print(row)
    
#requete select complexe
from sqlalchemy import and_
from sqlalchemy.sql import select, text
s = select([text("* from students")]) \
    .where(
            and_(
                    text("students.name between :x and :y"),
                    text("students.id > :z")
                    )
            )
result = conn.execute(s, x='A', y='L', z='2').fetchall()
print(result)

#Requête sur des tables multiples
s = select([students, addresses]).where(students.c.id == addresses.c.st_id)
result = conn.execute(s)
for row in result:
    print (row)
    

j = students.join(addresses, students.c.id == addresses.c.st_id)
stmt = select([students]).select_from(j)
result = conn.execute(stmt)
print(result.fetchall())

#and/or
stmt = select([students]).where(or_(students.c.name=='Ravi', students.c.id <3))
result = conn.execute(stmt)
print(result.fetchall())

#as/desc
stmt = select([students]).order_by(asc(students.c.name))
result = conn.execute(stmt)
for row in result:
    print (row)

