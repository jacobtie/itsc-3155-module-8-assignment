# TODO: Feature 3
from app import search_movies
from src.repositories.movie_repository import movie_repository_singleton
def test_search():
    movie_repository_singleton.create_movie('Movie', 'Person', 3)
    movie = movie_repository_singleton.get_movie_by_title("Movie")
    movieNot = movie_repository_singleton.get_movie_by_title("Memories")
    space = movie_repository_singleton.get_movie_by_title("")
    assert movie.title == "Movie"
    assert movie.director == "Person"
    assert movie.rating == 3
    assert movieNot == None
    assert space == None
