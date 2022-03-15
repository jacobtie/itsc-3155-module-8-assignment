# TODO: Feature 3

from flask.testing import FlaskClient


def test_search_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<tr><td>{{title}}</td><td>{{rating}}</td></tr>' in response_data