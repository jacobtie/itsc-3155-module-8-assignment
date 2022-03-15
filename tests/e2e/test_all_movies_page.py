# TODO: Feature 1
from app import app
from src.repositories.movie_repository import MovieRepository

@pytest.fixture()
def test_app():
  return app.test_client()

def test_list_all_movies_page(test_app):
  response = test_app.get('/movies')
  assert b'<h1 class="mb-5">All Movies</h1>' in response.data

  assert b'<th scope="col">Ratings</th>' in response.data

def test_list_content_page(test_app):
    movie_list = MovieRepository()
    movie_list.create_movie("Hello World", "Hirdhay Tomphson", 5)
    response = test_app.get('/movies')
    
    assert b'<td>Hello World</td>' in response.data