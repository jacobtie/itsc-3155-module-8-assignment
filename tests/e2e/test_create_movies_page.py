from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

def test_create_movies_page(test_app: FlaskClient):
    response = test_app.post("/movies", title='will', director='star', rating='3')
    response_data = response.data

    assert response_data.movie.title == 'will'
    assert response_data.movie.director == 'star'
    assert response_data.movie.rating == '3'