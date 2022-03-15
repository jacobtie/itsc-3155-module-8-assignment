# TODO: Feature 3

from flask.testing import FlaskClient


def test_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<form action="/movies/display" method="post">' in response_data
    assert b'<input type="text" class="form-control" id="movie_name" name="movie_name" placeholder="Movie Name">' in response_data
    assert b'<button type="submit" class="btn btn-primary my-1">Submit</button>' in response_data

def test_display_rating_page(test_app: FlaskClient):
    response = test_app.get('/movies/display')
    response_data = response.data

    assert b'<h1 class="mb-5">Movie Ratings</h1>' in response_data
    assert b'<table class="table">' in response_data
    assert b'<tr><td>{{title}}</td><td>{{rating}}</td></tr>' in response_data
