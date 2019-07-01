# sodb_recordings.py

from sqlalchemy import *
from etude_engine.db.sodb import Base

class sodb_recordings(Base):
    __tablename__='sodb_recordings'
    id_recordings = Column(Integer, primary_key=True)
    primary_performer = Column(String(64))
    other_performers = Column(String(128))
    record_label = Column(String(32))
    date_recorded = Column(Date)
    medium = Column(String(32))
    sodb_music_id_recording = Column(Integer)

    def __init__(self, primary_performer: object=None,
                 other_performers: object=None,
                 record_label: object=None,
                 date_recorded: object=None,
                 medium: object=None,
                 sodb_music_id_recording: object=None,
                 sodb_sf_data_id_sf_data: object=None):
        self.primary_performer=primary_performer or None
        self.other_performers=other_performers or None
        self.record_label=record_label or None
        self.date_recorded=date_recorded or None
        self.medium=medium or None
        self.sodb_music_id_recording=sodb_music_id_recording or None


    def __repr__(self):
        return "<sodb_recordings(primary_performer='%s', other_performers='%s', record_label='%s', date_recorded='%s', medium='%s', sodb_music_id_music='%d', sodb_sf_data_id_sf_data='%d' )>" % (
                             self.primary_performer, self.other_performers, self.record_label, self.date_recorded, self.medium, self.sodb_music_id_recording, self.sodb_sf_data_id_sf_data)


#'id_recordings', 'int(11)', 'NO', 'PRI', NULL, ''
#'primary_performer', 'varchar(45)', 'YES', '', NULL, ''
#'other_performers', 'varchar(256)', 'YES', '', NULL, ''
#'record_label', 'varchar(45)', 'YES', '', NULL, ''
#'date_recorded', 'date', 'YES', '', NULL, ''
#'medium', 'enum(\'CD\',\'LP\',\'TAPE\',\'45\',\'CYL\')', 'YES', '', NULL, ''
#'sodb_music_id_music', 'int(11)', 'NO', 'MUL', NULL, ''
#'sodb_sf_data_id_sf_data', 'int(11)', 'NO', 'MUL', NULL, ''
