# TODO: Feature 2
from src.models.movie import Movie

def test_movie():
    movie = Movie('Spiderman', 'Sam Raimi', 3)

    assert type(movie) == Movie
    assert movie.title == 'Spiderman'
    assert movie.director == 'Sam Raimi'
    assert movie.rating == 3
