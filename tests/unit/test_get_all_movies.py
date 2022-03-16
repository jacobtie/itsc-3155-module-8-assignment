# TODO: Feature 1
from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton


def test_get_all_movies():
    movies = movie_repository_singleton.get_all_movies()
    assert type(movies) == list
