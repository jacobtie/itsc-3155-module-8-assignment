from urllib import response
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton

def test_list_all_movies(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data
    
    assert b'<table class="table">'
    assert b'</table>'
    for movie in movie_repository_singleton.get_all_movies():
        assert f'<th scope="row">{movie.title}</th>'
        assert f'<td>{movie.director}</td>'
        assert f'<td>{movie.rating}</td>'
