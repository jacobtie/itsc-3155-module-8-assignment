# TODO: Feature 3

from src.models.movie import Movie

def test_search_movie_model():
    movie = Movie('Bounty Hunter', 'Khan', 5.9)
    
    assert movie.title == 'Star Wars'
    assert movie.rating == 5