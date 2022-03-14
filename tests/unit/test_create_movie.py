# TODO: Feature 2
from src.models.movie import Movie
from repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    title = 'Saving Private Ryan'
    director = 'Steven Spielberg'
    rating = int(5)
    movie = movie_repository_singleton.create_movie(title, director, rating)

    assert movie == ['Saving Private Ryan', 'Steven Spielburg', 5]

