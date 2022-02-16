from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////Users/nitesh.sinha/Documents/sqlalchemy-db-test.sqlite3')
#engine = create_engine('sqlite://')

Session = sessionmaker(bind=engine)

Base = declarative_base()