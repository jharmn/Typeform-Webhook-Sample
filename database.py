import os
from peewee import SqliteDatabase, Model, PrimaryKeyField, CharField, BooleanField, TextField

CWD = os.getcwd()
DATABASE = CWD+'/db/formconf.db'
SCHEMA = CWD+'/db/schema.sql'

def get_db():
    return SqliteDatabase(DATABASE, threadlocals=True)

class Attendee(Model):
    id = PrimaryKeyField()
    name = CharField()
    website = CharField()
    source = CharField()
    email = CharField(unique = True)
    party = BooleanField()
    other = TextField()

    class Meta:
        database = get_db()

def create_tables():
    db = get_db() 
    db.connect()
    db.create_tables([Attendee])
