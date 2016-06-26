from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

engine = create_engine('sqlite:///papertowns.db')
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class Town(Base):
    __tablename__ = 'towns'

    title = Column(String)
    image_url = Column(String, primary_key=True)
    submission_url = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    def __repr__(self):
       return self.title

Base.metadata.create_all(engine)
