from flask.testing import FlaskClient


def test_create_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies/new')
    response_data = response.data