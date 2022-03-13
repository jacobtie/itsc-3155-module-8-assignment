# TODO: Feature 1
from flask.testing import FlaskClient

def test_all_movies_page(test_app: FlaskClient):
    response = test_app.get('/movies') #gets the /movies page and stores to response
    response_data = response.data #gets the data from response and stores to response_data

    assert b'<h1 class="mb-5">All Movies</h1>' in response_data #checks if the All Movies header is in response_data
    assert b'<p class="mb-3">See our list of movie ratings below</p>' in response_data #checks if the paragraph is in response_data
    assert b'<th scope="col">Movie</th>' in response_data #checks if the table with the header is in response_data
    assert b'<th scope="col">Rating</th>' in response_data #checks if the table with the header is in response_data