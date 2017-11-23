from sqlalchemy import Column, Integer, String

from subtitledscreenings.db.db_setup import Base


class Screening(Base):
    __tablename__ = "screenings"
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)
    date = Column(String)
    time = Column(String)
    age = Column(String)

    def __init__(self, title, date, time, age):
        self.title = title
        self.date = date
        self.time = time
        self.age = age

    def __repr__(self):
        return '<Screening %r>' % (self.title)
