# TODO: Feature 2
from app import app
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    movie = movie_repository_singleton.create_movie("will","william","5")

    assert movie.title == "will"
    assert movie.director == "william"
    assert movie.rating == "5"