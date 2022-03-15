from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton



def test_get_movie_by_title():
    movie = Movie('Star Wars', 'George Lucas', 5)
    test1 = movie_repository_singleton.create_movie('A New Hope', 'George Lucas', 5)
    assert type(movie) == Movie
    assert movie.title == 'Star Wars'
    assert movie.director == 'George Lucas'
    assert movie.rating == 5

    # Case 1: Movie found
    assert movie_repository_singleton.get_movie_by_title('A New Hope').title == test1.title
    # Case 2: Movie Not Found
    assert movie_repository_singleton.get_movie_by_title('Return of The Jedi') == None
    # Case 3: No Input
    assert movie_repository_singleton.get_movie_by_title('') == None
