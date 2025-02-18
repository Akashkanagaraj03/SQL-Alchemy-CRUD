from models import *
from connection import engine
from sqlalchemy.orm import Session

session = Session(bind = engine)

update_item = session.query(Review).filter_by(user_id = 4, movie_id = 6).first()

session.delete(update_item)
session.commit()
session.close()

