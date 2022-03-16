# TODO: Feature 2
from flask.testing import FlaskClient
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie

def test_create_movies_page(test_app: FlaskClient):
    test_avatar = {
        "movieTitle":"Avatar",
        "movieDirector":"James Cameron",
        "movieRating":3
    }
    response_form_data = test_app.post("/movies", data=test_avatar)
    # Make sure user is redirected
    assert response_form_data.status_code == 302
    assert movie_repository_singleton.get_all_movies()[0].title == "Avatar"
    assert movie_repository_singleton.get_all_movies()[0].director == "James Cameron"
    # Rating is converted to string because it's coming from a form
    assert movie_repository_singleton.get_all_movies()[0].rating == "3"

    # Test another film to make sure film is appended correctly
    test_psycho = {
        "movieTitle":"Psycho",
        "movieDirector":"Alfred Hitchcock",
        "movieRating":4
    }
    response_form_data = test_app.post("/movies", data=test_psycho)
    assert response_form_data.status_code == 302
    assert movie_repository_singleton.get_all_movies()[1].title == "Psycho"
    assert movie_repository_singleton.get_all_movies()[1].director == "Alfred Hitchcock"
    assert movie_repository_singleton.get_all_movies()[1].rating == "4"