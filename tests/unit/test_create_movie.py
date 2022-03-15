# TODO: Feature 2
from app import app
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    movie = movie_repository_singleton.create_movie("test","director","5")

    #make sure that the movie datatype works correctly
    assert movie.title == "test"
    assert movie.director == "director"
    assert movie.rating == "5"

    #ensure that it is in the database 
    assert movie in movie_repository_singleton._db

    movie2 = movie_repository_singleton.create_movie("test2","director2","3")

    #make sure that the movie datatype works correctly and doesnt get confused
    assert movie2.title == "test2"
    assert movie2.director == "director2"
    assert movie2.rating == "3"

    #ensure that both are in the database 
    assert movie in movie_repository_singleton._db
    assert movie2 in movie_repository_singleton._db