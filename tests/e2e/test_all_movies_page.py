# TODO: Feature 1
from flask.testing import FlaskClient


def test_table_page(test_app: FlaskClient):
    response = test_app.get('/movies')
    response_data = response.data

    assert b'<h1 class="mb-5">All Movies</h1>' in response_data
