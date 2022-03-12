# TODO: Feature 1
from app import list_all_movies #from app.py import the function list_all_movies
from src.repositories.movie_repository import MovieRepository

def test_list_all_movies():
    MovieRepository.create_movie('Voices of a Distant Star', 'Shinkai', 5)
    MovieRepository.create_movie('Memories', 'Otmomo', 4)
    MovieRepository.create_movie('Matrix', 'Wachowski', 5)

    movie_list = []
    movie_list = list_all_movies()
    counter = 0
    movie_directory = {}
    for movies in movie_list:
        movie_directory[movie_list.title] = movie_list.rating
    
    for key in movie_directory.keys():
        movie_list[counter] = key
        counter += 1

    # movie1 = Movie('Voices of a Distant Star', 'Shinkai', 5)
    # movie2 = Movie('Memories', 'Otmomo', 4)
    # movie3 = Movie('Matrix', 'Wachowski', 5)
    # movies = [movie1, movie2, movie3]
    # movie_directory = {}
    # for movie in movies:
    #     movie_directory[movie.title] = movie.rating
