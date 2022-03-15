# TODO: Feature 2
from repositories.movie_repository import MovieRepository

def test_create_movie():
    movie_list = MovieRepository()
    #checks for 1 movie
    movie_list.create_movie('spiderman','directorman', 5)
    allmov = movie_list._db
    counter = 0
    for movie in allmov:
        if movie.title == 'spiderman':
            counter = counter + 1
    assert counter == 1
    #checks if duplicates are stored
    movie_list.create_movie('spiderman','directorman', 4)
    allmov = movie_list._db
    counter = 0
    for movie in allmov:
        if movie.title == 'spiderman':
            counter = counter + 1
    assert counter == 1



