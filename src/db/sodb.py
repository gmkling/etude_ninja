# sodb.py

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from db.sodb_annotations import *
from db.sodb_music import *
from db.sodb_notes import *
from db.sodb_recordings import *
from db.sodb_sf_data import *
from sqlalchemy.orm import sessionmaker
import datetime

def validate_date(date_text):
    # This function will validate a date as yyyy-mm-dd

    # This is to protect against the false negatives
    if isinstance(date_text, datetime.date):
        return True
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        return False
    return True

class Sodb:

    def __init__(self):
        self.sodb_engine = create_engine('mysql+mysqlconnector://root:.242__donoho@localhost/sodb',
                                    echo=True, pool_pre_ping=True)
        self.sodb_connection = self.sodb_engine.connect()

        Internal = sessionmaker(bind=self.sodb_engine)

        self.session = Internal()
        #Base.metadata.create_all(self.sodb_engine)
        #self.session.commit()

    def __del__(self):
        self.sodb_connection.close()

    def show_tables(self):
        result = self.sodb_engine.execute("show tables")
        for row in result:
            print("table:", row['Tables_in_sodb'])
        result.close()

    def test(self):
        if (self.sodb_engine):
            print("Connected to sodb.")
            return True

    def add_object(self, obj):
        # do some validation, esp with dates
        if isinstance(obj, sodb_music):
            if not validate_date(obj.date):
                obj.date='1970-01-01'
                print("Fixed sodb_music date.")
        if isinstance(obj,sodb_recordings):
            print("Object matching sodb_recording")
            if not validate_date(obj.date_recorded):
                obj.date_recorded='1970-01-01'
                print("Fixed sodb_recordings date.")

        # use .add() on the session
        self.session.add(obj)

    def commit_changes(self):
        # see that we have changes made
        # commit them
        self.session.commit()

    def rollback_changes(self):
        # check that there are changes
        # roll it back with .rollback()
        self.session.rollback()

    def close(self):
        # close the thing
        self.session.close()