from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.orm import relationship
from models.base import Base

class Actor(Base):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    contact_details = relationship("ContactDetails", back_populates="actor")
    stuntman = relationship("Stuntman", back_populates="actor")

    def __init__(self, name, bday):
        self.name = name
        self.birthday = bday