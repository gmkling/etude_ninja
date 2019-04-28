# sodb_music.py

from sqlalchemy import *
from db.sodb import Base

class sodb_music(Base):
    __tablename__='sodb_music'
    id_music = Column(Integer, primary_key=True)
    composer = Column(String(32))
    title = Column(String(32))
    opus_num = Column(Integer)
    date = Column(Date)
    notation_filename = Column(String(128))
    instrumentation = Column(String(128))

    def __init__(self, composer: object=None,
                 title: object=None,
                 opus_num: object=None,
                 date: object=None,
                 notation_filename: object=None,
                 instrumentation: object=None):

        self.composer = composer or None
        self.title = title or None
        self.opus_num = opus_num or None
        self.date = date or None
        self.notation_filename = notation_filename or None
        self.instrumentation = instrumentation or None

    def __repr__(self):
        return "<sodb_music(composer='%s', title='%s', opus_num='%d', date='%s', notation_filename='%s', instrumentation='%s')>" % (
                             self.composer, self.title, self.opus_num, self.date, self.notation_filename, self.instrumentation)
# 'id_music', 'int(11)', 'NO', 'PRI', NULL, ''
# 'composer', 'varchar(45)', 'YES', '', NULL, ''
# 'title', 'varchar(45)', 'YES', '', NULL, ''
# 'opus_num', 'int(11)', 'YES', '', NULL, ''
# 'date', 'date', 'YES', '', NULL, ''
# 'notation_filename', 'varchar(45)', 'YES', '', NULL, ''
# 'instrumentation', 'varchar(128)', 'YES', '', NULL, ''
