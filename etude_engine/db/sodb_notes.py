# sodb_notes.py

from sqlalchemy import *
from etude_engine.db.sodb import Base

class sodb_notes(Base):
    __tablename__='sodb_notes'
    id_notes = Column(Integer, primary_key=True)
    freq = Column(Float)
    amp = Column(Float)
    dur = Column(Float)
    attack_dur = Column(Float)
    decay_dur = Column(Float)
    sustain_dur = Column(Float)
    release_dur = Column(Float)
    ''' These fields are selected with handles/panes in GUI'''
    sf_in = Column(Integer)
    sf_out = Column(Integer)
    sodb_sf_data_id = Column(Integer, ForeignKey("sodb_sf_data.id_sf_data"))
    sodb_recordings_id = Column(Integer, ForeignKey("sodb_recordings.id_recordings"))
    sodb_annotations_id = Column(Integer, ForeignKey("sodb_annotations.id_annotations"))

    def __init__(self, freq: object=None,
                 amp: object=None,
                 dur: object=None,
                 attack_dur: object=None,
                 decay_dur: object=None,
                 sustain_dur: object=None,
                 release_dur: object=None,
                 sf_in: object=None,
                 sf_out: object=None,
                 sodb_sf_data_id: object=None,
                 sodb_recordings_id: object=None,
                 sodb_annotations_id: object=None):
        self.freq = freq or None
        self.amp = amp or None
        self.dur = dur or None
        self.attack_dur = attack_dur or None
        self.decay_dur = decay_dur or None
        self.sustain_dur = sustain_dur or None
        self.release_dur = release_dur or None
        self.sf_in = sf_in or None
        self.sf_out = sf_out or None
        self.sodb_sf_data_id = sodb_sf_data_id or None
        self.sodb_recordings_id = sodb_recordings_id or None
        self.sodb_annotations_id = sodb_annotations_id or None

    def __repr__(self):
        return "<sodb_notes(freq='%d', amp='%d', dur='%d', attack_dur='%d', decay_dur='%d', " \
               "sustain_dur='%d', release_dur='%d', sf_in='%i', sf_out='%i', sodb_sf_data_id='%i', " \
               "sodb_recordings_id='%i', sodb_annotations_id='%i')>" % (
                   self.freq, self.amp, self.dur, self.attack_dur, self.decay_dur, self.sustain_dur, self.release_dur,
                   self.sf_in, self.sf_out, self.sodb_sf_data_id, self.sodb_recordings_id, self.sodb_annotations_id)

#'id_notes', 'int(11)', 'NO', 'PRI', NULL, ''
#'freq', 'float', 'YES', '', NULL, ''
#'amp', 'float', 'YES', '', NULL, ''
#'dur', 'float', 'YES', '', NULL, ''
#'attack_dur', 'int(11)', 'YES', '', NULL, ''
#'decay_dur', 'int(11)', 'YES', '', NULL, ''
#'sustain_dur', 'int(11)', 'YES', '', NULL, ''
#'release_dur', 'int(11)', 'YES', '', NULL, ''
#'sodb_sf_data_idsodb_sf_data', 'int(11)', 'NO', 'MUL', NULL, ''
#'sodb_recordings_idsodb_recordings', 'int(11)', 'NO', 'MUL', NULL, ''
#'sodb_annotations_idsodb_annotations', 'int(11)', 'NO', 'MUL', NULL, ''

