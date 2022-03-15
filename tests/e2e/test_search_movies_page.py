from flask.testing import FlaskClient


def test_home_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data

    assert b'<h1 class="mb-5">Movie Rating App</h1>' in response_data
