# sodb.py

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
from etude_engine.db.sodb_annotations import *
from etude_engine.db.sodb_music import *
from etude_engine.db.sodb_notes import *
from etude_engine.db.sodb_recordings import *
from etude_engine.db.sodb_sf_data import *
from etude_engine.db.sodb_midi_transcription import *
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

    # we need to factor the session out of here as a data member
    # and make this a more pure data interface


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

    # I'm not sure this is the way
    # def update_entry(self, obj):
    #     # Figure what table we're talking about
    #     theRow=[]
    #     if isinstance(obj, sodb_music):
    #         theRow = self.session.query(sodb_music).where(id_music==obj.id_music))
    #     # keying off the id in obj, edit the entry for it
    #     stmt = update(theRow) \
    #         values(name='user #5')



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

    def search_compositions(self, obj):
        # do a search on the sodb_music table
        self.the_query = self.session.query(sodb_music)

        # for every field with an entry, filter the query
        if isinstance(obj, sodb_music):
            if obj.id_music is not None:
                self.the_query = self.the_query.filter(sodb_music.id_music==obj.id_music)
            if obj.composer is not None:
                self.the_query = self.the_query.filter(sodb_music.composer.ilike(obj.composer))
            if obj.opus_num is not None:
                self.the_query = self.the_query.filter(sodb_music.opus_num==obj.opus_num)
            if obj.date is not None:
                self.the_query = self.the_query.filter(sodb_music.date==obj.date)
            if obj.title is not None:
                self.the_query = self.the_query.filter(sodb_music.title.ilike(obj.title))
            if obj.notation_filename is not None:
                self.the_query = self.the_query.filter(sodb_music.notation_filename.ilike(obj.notation_filename))
            if obj.instrumentation is not None:
                self.the_query = self.the_query.filter(sodb_music.instrumentation.ilike(obj.instrumentation))
        return self.the_query