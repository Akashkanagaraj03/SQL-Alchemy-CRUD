from connection import engine
from models import *
from sqlalchemy.orm import sessionmaker

#Create tables
Base.metadata.create_all(engine)

