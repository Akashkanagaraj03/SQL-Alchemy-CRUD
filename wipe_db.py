from sqlalchemy.orm import Session
from connection import engine
from models import *

session = Session(engine)

with session.begin():
    try:
        session.query(Review).delete()
        session.query(User).delete()
        session.query(Movie).delete()

    except Exception as e:
        print(f'Error:{e}')
        session.rollback()

    else:
        session.commit()
        print("All data has been deleted.")

    finally:
        session.close()