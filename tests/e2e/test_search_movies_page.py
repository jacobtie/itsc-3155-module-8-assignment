from flask import Flask
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton
from app import app


def test_search_page(test_app: FlaskClient):
    movie_repository_singleton.create_movie("Star Wars", "George Lucas", 5)
    response = test_app.get('/movies/search', query_string={"input_movie": "Star Wars"})
    response = test_app.get('/movies/search', query_string={"input_movie": "not a movie"})
    response_data = response.data

    assert b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data
    assert b'<p class="mb-5">Search for a movie rating below</p>' in response_data

    assert b'<div class="mb-5">' in response_data
    assert b'<form action="/movies/search" method="get" class="row row-cols-lg-auto g-3 align-items-center">' in response_data
    assert b'<div class="col-12">' in response_data
    assert b'<label for="movie" class="visually-hidden">Movie Titile</label>' in response_data
    assert b'<div class="input-group">' in response_data
    assert b'<div class="input-group-text">Movie Title:</div>' in response_data
    assert b'<input type="text" class="form-control" id="input_movie" name="input_movie" autocomplete="off">' in response_data
    assert b'</div>' in response_data
    assert b'</div>' in response_data
    assert b'<div class="col-12">' in response_data
    assert b'<button type="submit" value="Submit" class="btn btn-primary name">Search</button>' in response_data
    assert b'</div>' in response_data
    assert b'</form>' in response_data
    assert b'</div>' in response_data

    # assert b'{% if search_movie %}' in response_data

    assert b'<div class="mt-5">' in response_data
    assert b'<div class="card text-center">' in response_data
    assert b'<div class="card-header">Your Result</div>' in response_data
    assert b'<div class="card-body">' in response_data
    assert b'<p> Star Wars directed by George Lucas has a 5 star rating.</p>' in response_data
    assert b'</div>' in response_data
    assert b'</div>' in response_data
    assert b'</div>' in response_data

    # assert b'{% else %}' in response_data

    assert b'<div class="mt-5">' in response_data
    assert b'<div class="card text-center">' in response_data
    assert b'<div class="card-header">Your Result</div>' in response_data
    assert b'<div class="card-body">' in response_data
    assert b'<p> Not Found`</p>' in response_data
    assert b'</div>' in response_data
    assert b'</div>' in response_data
    assert b'</div>' in response_data

    # assert b'{% endif %}' in response_data






