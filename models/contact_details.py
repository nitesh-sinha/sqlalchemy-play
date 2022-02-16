from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from models.base import Base


class ContactDetails(Base):
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    address = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    # One actor can have many contact details
    # For one-to-many relationship, the "many" side(here ContactDetails)
    # always has FK to the "one" side(here Actor)
    # Justification argument: https://stackoverflow.com/a/3294168
    actor = relationship("Actor", back_populates='contact_details')

    def __init__(self, phone_num, address, actor):
        self.phone_number = phone_num
        self.address = address
        self.actor = actor