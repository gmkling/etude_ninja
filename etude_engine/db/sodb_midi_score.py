# sodb_music.py

from sqlalchemy import *
from db.sodb import Base

class sodb_midi_score(Base):
    __tablename__='sodb_midi_score'
    id_midi_score = Column(Integer, primary_key=True)
    sodb_recordings_id = Column(Integer, nullable=False)
    score_filename = Column(String(128))

    def __init__(self, sodb_recordings_id: object=None,
                 score_filename: object=None):
        self.sodb_recordings_id = sodb_recordings_id or None
        self.score_filename = score_filename or None

    def __repr__(self):
        return "<sodb_music(sodb_recordings_id='%d', score_filename='%s'" % (
                             self.sodb_recordings_id, self.score_filename)
# 'id_music', 'int(11)', 'NO', 'PRI', NULL, ''
# 'composer', 'varchar(45)', 'YES', '', NULL, ''
# 'title', 'varchar(45)', 'YES', '', NULL, ''
# 'opus_num', 'int(11)', 'YES', '', NULL, ''
# 'date', 'date', 'YES', '', NULL, ''
# 'notation_filename', 'varchar(45)', 'YES', '', NULL, ''
# 'instrumentation', 'varchar(128)', 'YES', '', NULL, ''
