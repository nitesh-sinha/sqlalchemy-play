from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref
from models.base import Base


class Stuntman(Base):
    __tablename__ = 'stuntmen'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    # As per the relationship defined below, whenever we load an instance
    # of Stuntman, SQLAlchemy will also load and populate the Actor associated
    # with this stuntman. Also the actor object will get a property called
    # "stuntman" that is not a list.
    # One-to-one relationship between actor and stuntman
    actor = relationship("Actor", backref=backref("stuntman", uselist=False))

    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor

