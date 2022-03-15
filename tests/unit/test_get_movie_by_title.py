# TODO: Feature 3
from src.repositories.movie_repository  import movie_repository_singleton


def test_get_movie_by_title():
    
    movie_repository_singleton.create_movie('Saving Private Ryan', 'Steven Speilburg', 5)

    movie = movie_repository_singleton.get_movie_by_title('Saving Private Ryan')

    assert movie.title == 'Saving Private Ryan'
    assert movie.director == 'Steven Speilburg'
    assert movie.rating == 5

    

