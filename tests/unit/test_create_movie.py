# TODO: Feature 2 by Nick koehler
from urllib import response
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movies(test_app: FlaskClient):
    response = test_app.post('/movies', title='danny' name='grapes', rating='1')
    response_data = response.data

    assert bool(movie_repository_singleton.get_all_movies())
# TODO: Feature 2
