# TODO: Feature 3
from src.repositories.movie_repository import MovieRepository

def test_search_movies_page():
    movie = MovieRepository()
    assert movie.get_all_movies().count(0) == 0 #test no movies added
    movie.create_movie('The Matrix', 'Wachowski', 5) #adding movie
    assert movie.get_movie_by_title('The Matrix').title == 'The Matrix' #test title of movie search matches movie created
    assert movie.get_movie_by_title('The Matrix').rating == 5 #test rating of movie search matches movie rating created
    assert movie.get_movie_by_title('The Matrix').director == "Wachowski" #test director of movie search matches movie director created
    assert movie.get_movie_by_title('Memories') == None #test for a movie not created. 