from models import create_user, create_movie, create_review
from connection import engine
from sqlalchemy.orm import Session

session = Session(bind = engine)

user_1, user_2 = [
    create_user('Akash', 'akash@hpe.com'),
    create_user('Violet', 'violet@hpe.com'),
]

movie_1, movie_2, movie_3 = [
    create_movie('Space Movie','Sci-fi',1996),
    create_movie('Indiana Jones','Adventure',2002),
    create_movie('Lord of the Rings','Fantasy',2000),
]

review_1, review_2, review_3, review_4 = [
    create_review( user_1, movie_1, 1, 'Movie was bad.'),
    create_review( user_1, movie_2, 4, 'Movie was very good.'),
    create_review( user_1, movie_3, 5, 'Tolkein is the greatest writer ever.'),
    create_review( user_2, movie_3, 2, 'Movie was mediocre.'),
]

session.add_all([
    user_1, user_2,
    movie_1, movie_2, movie_3,
    review_1, review_2, review_3, review_4,
])

session.commit()