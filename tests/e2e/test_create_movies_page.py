# TODO: Feature 2  by Nick koehler
from urllib import response
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movies(test_app: FlaskClient):
    response = test_app.post('/movies', title='danny' name='grapes', rating='1')
    response_data = response.data

    assert response_data.movie.title == 'danny'
    assert response_data.movie.name == 'grapes'
    assert response_data.movie.rating == '1'

