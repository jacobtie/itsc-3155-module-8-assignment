from src.repositories.movie_repository import MovieRepository

# TODO: Feature 1
def test_get_all_movies():
    movie_list = MovieRepository()
    assert len(movie_list.get_all_movies) == 0

    movie_list.create_movie("Spider Man", "Haley", 3)
    assert len(movie_list.get_all_movies) == 1

    movie_list.create_movie("Hello World", "Hirdhay Tomphson", 5)
    assert len(movie_list.get_all_movies) == 2

