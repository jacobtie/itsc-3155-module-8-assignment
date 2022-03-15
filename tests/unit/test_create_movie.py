# TODO: Feature 2
from src.models.movie import Movie

def test_create_movie():
    movie = Movie('Forrest Gump', 'Robert Zemeckis', 4)

    assert type(movie) == Movie
    assert movie.title == 'Forrest Gump'
    assert movie.director == 'Robert Zemeckis'
    assert movie.rating == 4