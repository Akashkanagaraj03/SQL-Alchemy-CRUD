from sqlalchemy import select
from models import *
from connection import engine
from sqlalchemy.orm import Session

session = Session(bind = engine)

#fetching all users
users = session.query(User).all()
print("\nUsers in the table:")
for user in users:
    print(f'{user.id}. {user.name}')

#fetching reviews of a certain movie -> result_1
# statement_1 = select(Review).join(Movie).where(Movie.id == 6)                #does not use orm
# result_1 = session.scalars(statement_1)
result_1 = session.query(Review).join(Movie).filter(Movie.id == 6)             #uses orm

#fetching all movies reviews by a certain user -> result_2
# statement_2 = select(Review.movie_id).join(User).where(User.id == 4)         #does not use orm
# statement_3 = select(Movie).where(Movie.id.in_(statement_2))
#result_2 = session.scalars(statement_3)
sub_query = session.query(Review.movie_id).join(User).filter(User.id == 4)   #uses orm
result_2 = session.query(Movie).filter(Movie.id.in_(sub_query)).all()

print("\nReviews of The Lord of the Rings:")
for review in result_1:
    print(review.review_txt)
print("\nMovies reviewed by user 4:")
for movie in result_2:
    print(movie.title)

session.close()