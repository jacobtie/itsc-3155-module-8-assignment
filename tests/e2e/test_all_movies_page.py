from flask import Flask
from src.repositories import movie_repository
from src.models.movie import Movie
from app import app, create_movie
from src.repositories.movie_repository import MovieRepository

# TODO: Feature 1

def test_all():
    client = app.test_client()
    response = client.get('/movies')
    all_movies = movie_repository.get_all_movies()
    if len(all_movies) == 0:
        assert b"<p>There are no movies</p>"
    else:
        assert b"<th>Title</th>" in response.data


