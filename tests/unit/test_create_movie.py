from src.repositories.movie_repository import MovieRepository
from src.models.movie import Movie

def test_create_movie():
    test_movie_repository = MovieRepository()
    batman = test_movie_repository.create_movie('The Batman', 'Matt Reeves', 4)
    test_list = test_movie_repository.get_all_movies()
    assert type(test_list[0]) == Movie
    assert test_list[0].title == 'The Batman'
    assert test_list[0].director == 'Matt Reeves'
    assert test_list[0].rating == 4
    assert test_list[0].title == batman.title
    assert test_list[0].director == batman.director
    assert test_list[0].rating == batman.rating

    # Repeat test to make sure another Movie is appended correctly
    nightcrawler = test_movie_repository.create_movie('Nightcrawler', 'Dan Gilroy', 5)
    test_list = test_movie_repository.get_all_movies()
    assert type(test_list[1]) == Movie
    assert test_list[1].title == 'Nightcrawler'
    assert test_list[1].director == 'Dan Gilroy'
    assert test_list[1].rating == 5
    assert test_list[1].title == nightcrawler.title
    assert test_list[1].director == nightcrawler.director
    assert test_list[1].rating == nightcrawler.rating