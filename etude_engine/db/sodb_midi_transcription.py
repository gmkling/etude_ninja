# sodb_recordings.py

from sqlalchemy import *
from etude_engine.db.sodb import Base

class sodb_midi_transcription(Base):
    __tablename__='sodb_midi_transcription'
    id_midi_transcription = Column(Integer, primary_key=True)
    sodb_recordings_id = Column(Integer, nullable=False)
    midi_filepath = Column(String(128))
    csv_version_filepath = Column(String(128))

    def __init__(self, sodb_recordings_id: object=None,
                 midi_filepath: object=None,
                 csv_version_filepath: object=None):
        self.sodb_recordings_id=sodb_recordings_id or None
        self.midi_filepath=midi_filepath or None
        self.csv_version_filepath=csv_version_filepath or None


    def __repr__(self):
        return "<sodb_midi_transcription(sodb_recordings_id='%d', midi_filepath='%s', csv_version_filepath='%s')>" % (
                             self.sodb_recordings_id, self.midi_filepath, self.csv_version_filepath)

