from models import *
from connection import engine
from sqlalchemy.orm import Session

session = Session(bind = engine)

with session.begin():
    try:
        delete_item = session.query(Review).filter_by(user_id = 4, movie_id = 6).first()
        session.delete(delete_item)

    except Exception as e:
        print(f'Error:{e}')
        session.rollback()

    else:
        session.commit()
        print("Data Deleted.")

    finally:
        session.close()