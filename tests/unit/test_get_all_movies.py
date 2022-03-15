#https://www.youtube.com/watch?v=sL_PWBOABWo 
#https://codethechange.stanford.edu/guides/guide_flask_unit_testing.html
# TODO: Feature 1

from app import app
from src.repositories.movie_repository import MovieRepository

def test_list_all_movies():
    response = app.test_client().get('/movies') #gets the /movies page and stores to response
    assert response._status_code == 200 #checks if the reuqest above is successful
    movie = MovieRepository() 
    assert len(movie.get_all_movies()) == 0
    movie.create_movie('The Matrix', 'Wachowski', 5)
    assert len(movie.get_all_movies()) == 1
    assert movie.get_movie_by_title('The Matrix').title == "The Matrix"
    movie.create_movie('Voices of a Distant Star', 'Shinkai', 5)
    assert len(movie.get_all_movies()) == 2 
    assert movie.get_all_movies().index(movie.get_movie_by_title('Voices of a Distant Star')) == 1
