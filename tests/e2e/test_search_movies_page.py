from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton


def test_search_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data

    assert b'<form action="/movies/search" method="get" class="row row-cols-lg-auto g-3 align-items-center">' in response_data

    assert b'<input type="text" class="form-control" id="input_movie" name="input_movie" autocomplete="off">' in response_data

    assert b'<button type="submit" value="Submit" class="btn btn-primary name">Search</button>' in response_data

    assert b'<div class="card-header">Your Result</div>' not in response_data

    # {% if search_movie %}
    movie_repository_singleton.create_movie("Star Wars", "George Lucas", 5)
    response = test_app.get('/movies/search', query_string={"input_movie": "Star Wars"})
    response_data = response.data

    assert b'<p> Star Wars directed by George Lucas has a 5 star rating.</p>' in response_data

    # {% elif not search_movie %}
    response = test_app.get('/movies/search', query_string={"input_movie": "not a movie"})
    response_data = response.data

    assert b'<p> Not Found`</p>' in response_data