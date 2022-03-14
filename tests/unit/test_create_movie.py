# TODO: Feature 2
from src.repositories.movie_repository import MovieRepository
# create test cases
def test_create_movie():
    # create a movie
    movies = MovieRepository()
    movies.create_movie('Voices of a Distant Star', 'Shinkai', 5)
    assert len(movies.get_all_movies()) == 1
    movies.create_movie('Memories', 'Otmomo', 4)
    movies.create_movie('Matrix', 'Wachowski', 5)
    assert len(movies.get_all_movies()) == 3
