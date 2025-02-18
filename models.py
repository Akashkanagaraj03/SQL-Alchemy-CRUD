from typing import List

from sqlalchemy import ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=True)
    email:Mapped[str] = mapped_column(unique=True)
    #relationships
    reviews:Mapped[List['Review']] = relationship(back_populates='user')

class Movie(Base):
    __tablename__ = 'movies'
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str] = mapped_column(nullable=False)
    genre:Mapped[str] = mapped_column()
    release_year:Mapped[int] = mapped_column()
    #relationships
    reviews:Mapped[List['Review']] = relationship(back_populates='movie')

class Review(Base):
    __tablename__ = 'reviews'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    movie_id:Mapped[int] = mapped_column(ForeignKey('movies.id'), nullable=False)
    rating:Mapped[int] = mapped_column(nullable=False)
    review_txt:Mapped[str] = mapped_column(Text, nullable=False)
    # relationships
    user:Mapped['User'] = relationship(back_populates='reviews')
    movie:Mapped['Movie'] = relationship(back_populates='reviews')
    #table arguments
    __table_args__ = (
        CheckConstraint('rating BETWEEN 0 AND 5', name='check_rating_range'),
    )


def create_user(name, email):
    return User(name = name, email = email)

def create_movie(title, genre, release_year):
    return Movie(title = title, genre = genre, release_year = release_year)

def create_review(user, movie, rating, review_txt):
    return Review(user = user, movie = movie, rating = rating, review_txt = review_txt)
