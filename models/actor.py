from sqlalchemy import Column, String, Integer, Date

from models.base import Base

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, bday):
        self.name = name
        self.birthday = bday