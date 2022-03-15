# TODO: Feature 1
from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie
import pytest
movie_repository_singleton = MovieRepository()
def test_no_movies():
    movie = movie_repository_singleton.get_all_movies()
    assert movie == []
def test_all_movies():
    movie_repository_singleton.create_movie("Batman", "Direc Tor", 7)
    movie = movie_repository_singleton.get_all_movies()
    assert movie[0].title == "Batman"
    assert movie[0].director == "Direc Tor"
    assert movie[0].rating == 7

