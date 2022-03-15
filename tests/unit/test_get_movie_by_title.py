# TODO: Feature 3

from src.models.movie import Movie
from src.repositories.movie_repository import MovieRepository

def test_search_movie_model():
    movie = Movie('Batman', 'Matt Reeves', 5.9)
    assert MovieRepository.get_movie_by_title('Batman') == 'Batman'
    assert MovieRepository.get_movie_by_title('The X Files') == None