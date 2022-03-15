from flask.testing import FlaskClient
# TODO: Feature 3
def search_movie_page(test_app: FlaskClient):
    response = test_app.get('/movies/search')
    response_data = response.data
    assert  b'<h1 class="mb-5">Search Movie Ratings</h1>' in response_data
    assert response.location == 'http://localhost/movies/search'