# TODO: Feature 1
from app import app
from src.repositories.movie_repository import movie_repository_singleton

def test_list_all_movies():
    # The application page is loaded
    test_app = app.test_client()
    # Suppose that we have a movie 'this_is_a_movie' with rating 1
    # Use a random number for now (although the ratings will be from 1 to 5)
    movie_repository_singleton.create_movie('this_is_a_movie', 'b', 1123123)
    # test the movies path after adding that movie
    response = test_app.get('/movies')
    # check to see if 'this_is_a_movie' is in the rendered HTML page
    assert b'this_is_a_movie' in response.data
    # create another movie called 'random_string' with rating 1
    movie_repository_singleton.create_movie('random_string', 'b', 11232221)
    # user clicks on the movies link and the HTML page is rendered
    response = test_app.get('movies')
    # both movies should still be there
    assert b'this_is_a_movie' in response.data
    assert b'random_string' in response.data
    assert b'1123123' in response.data
    assert b'11232221' in response.data
