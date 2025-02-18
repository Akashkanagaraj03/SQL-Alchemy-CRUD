from connection import engine
from models import *

#Create tables
Base.metadata.create_all(engine)

