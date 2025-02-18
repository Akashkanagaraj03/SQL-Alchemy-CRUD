from sqlalchemy import select
from models import *
from connection import engine
from sqlalchemy.orm import Session

session = Session(bind = engine)

update_item = session.query(Review).filter_by(user_id = 4, movie_id = 6).first()

update_item.review_txt = "Edited movie review"

session.commit()
session.close()

