# TODO: Feature 2
from app import app
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie
#https://flask.palletsprojects.com/en/2.0.x/testing/ testing assistance for html / flask form

def test_create_movies_page():
    test_app = app.test_client()

    title = "Star Wars"
    director = "George Lucas"
    rating = "5"
    # movie info

    test_app.post("/movies", data = 
        {
            "title" : title,
            "director" : director,
            "rating" : rating
        })
    # post the movie info using the create rating page

    page = test_app.get("movies")

    # now we get the movies page and see if the content appears
    assert b'Star Wars' in page.data
    assert b'George Lucas' in page.data
    assert b'5' in page.data
