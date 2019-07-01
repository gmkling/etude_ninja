# sodb_sf_data.py

from sqlalchemy import *
from etude_engine.db.sodb import Base


class sodb_sf_data(Base):
    __tablename__='sodb_sf_data'
    id_sf_data = Column(Integer, primary_key=True)
    filename = Column(String(32))
    format = Column(String(32))
    sr = Column(Integer)
    bits = Column(Integer)
    dur = Column(Float)
    datasize = Column(Integer)
    source = Column(String(128))
    sodb_sf_datacol = Column(String(128))
    sodb_music_id_music = Column(Integer)

    def __init__(self, filename: object = None, format: object = None, sr: object = None, bits: object = None, dur: object = None, datasize: object = None, source: object = None,
                 sodb_sf_datacol: object = None,
                 sodb_music_id_music: object = None):
        self.filename = filename or None
        self.format = format or None
        self.sr = sr or None
        self.bits = bits or None
        self.dur = dur or None
        self.datasize = datasize or None
        self.source = source or None
        self.sodb_sf_datacol = sodb_sf_datacol or None
        self.sodb_music_id_music = sodb_music_id_music or None

    def __repr__(self):
        return "<sodb_sf_data(filename='%s', format='%s', sr='%d', bits='%d', dur='%d', datasize='%d', source='%s', sodb_sf_datacol='%s', sodb_music_id_music='%i' )>" % (
                             self.filename, self.format, self.sr, self.bits, self.dur, self.datasize, self.source, self.sodb_sf_datacol, self.sodb_music_id_music)

#'id_sf_data', 'int(11)', 'NO', 'PRI', NULL, ''
#'filename', 'varchar(45)', 'YES', '', NULL, ''
#'format', 'varchar(45)', 'YES', '', NULL, ''
#'sr', 'int(11)', 'YES', '', NULL, ''
#'bits', 'int(11)', 'YES', '', NULL, ''
#'dur', 'int(11)', 'YES', '', NULL, ''
#'datasize', 'int(11)', 'YES', '', NULL, ''
#'source', 'varchar(45)', 'YES', '', NULL, ''
#'sodb_sf_datacol', 'varchar(45)', 'YES', '', NULL, ''
#'sodb_music_id_music', 'int(11)', 'NO', 'PRI', NULL, ''
