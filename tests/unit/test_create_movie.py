import pytest
from src.models.movie import Movie
from src.repositories.movie_repository import movie_repository_singleton

def test_create_movie():
    testmovie = movie_repository_singleton.create_movie('Sonic Movie', 'Jeff Fowler', 5)
    emptymovie = movie_repository_singleton.create_movie('','','')

    assert testmovie.title == 'Sonic Movie'
    assert testmovie.director == 'Jeff Fowler'
    assert testmovie.rating == 5

def test_empty_movie():
    emptymovie = movie_repository_singleton.create_movie('','','')

    with pytest.raises(Exception):
        assert emptymovie.title == 'Sonic Movie' 
        assert emptymovie.director == 'Jeff Fowler'
        assert emptymovie.rating == 5

 