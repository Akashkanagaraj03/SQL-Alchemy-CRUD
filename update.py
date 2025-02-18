from models import *
from connection import engine
from sqlalchemy.orm import Session

session = Session(bind = engine)

with session.begin():
    try:
        update_item = session.query(Review).filter_by(user_id = 4, movie_id = 6).first()
        update_item.review_txt = "Edited movie review" if update_item else print("Item does not exist")

    except Exception as e:
        print(f'Error:{e}')
        session.rollback()

    else:
        session.commit()
        print("Data Updated.")

    finally:
        session.close()