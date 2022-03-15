from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton


def test_search_movies_page(test_app: FlaskClient):
    movie_repository_singleton.create_movie('A New Hope', 'George Lucas', 5)

    # Case 1 Found
    response = test_app.get('/movies/search?title=A+New+Hope')
    response_data = response.data
    assert b'<p class="mb-3">Search Result: A New Hope directed by George Lucas has a rating of 5</p>' in response_data

    # Case 2 Not Found
    response = test_app.get('/movies/search?title=Return of the Jedi')
    response_data = response.data
    assert b'<p class="mb-3">Movie not found</p>' in response_data

    # Case 3 No Input
    response = test_app.get('/movies/search')
    response_data = response.data
    assert b'<p class="mb-3"></p>' in response_data
