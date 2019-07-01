# sodb_annotations.py

from sqlalchemy import *
from datetime import datetime
from etude_engine.db.sodb import Base

class sodb_annotations(Base):
    __tablename__='sodb_annotations'
    id_annotations = Column(Integer, primary_key=True)
    operator = Column(String(32))
    software_version = Column(String(32))
    date = Column(DateTime, nullable=False, default=datetime.now())
    annotation_metadata = Column(String(32))

    def __init__(self, operator: object = None,
                 software_version: object = None,
                 date: object = None,
                 annotation_metadata: object = None) -> object:
        self.operator = operator or None
        self.software_version = software_version or None
        self.date = date or None
        self.annotation_metadata = annotation_metadata or None

    def __repr__(self):
        return "<sodb_annotations(operator='%s', software_version='%s', date='%s', annotation_metadata='%s')>" % (
                             self.operator, self.software_version, self.date, self.annotation_metadata)

#'id_annotations', 'int(11)', 'NO', 'PRI', NULL, ''
#'operator', 'varchar(45)', 'YES', '', NULL, ''
#'software_version', 'int(11)', 'YES', '', NULL, ''
#'date', 'datetime', 'YES', '', NULL, ''
#'metadata', 'varchar(256)', 'YES', '', NULL, ''
