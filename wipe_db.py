from sqlalchemy.orm import Session
from connection import engine
from models import *

session = Session(engine)

session.query(Review).delete()
session.query(User).delete()
session.query(Movie).delete()


session.commit()

print("All data has been deleted.")