# TODO: Feature 2

from src.repositories.movie_repository  import movie_repository_singleton

def test_create_movie():
    title = 'Saving Private Ryan'
    director = 'Steven Spielberg'
    rating = int(5)
    movie = movie_repository_singleton.create_movie(title, director, rating)

    
    assert movie.title == title
    assert movie.director == director
    assert movie.rating == rating

    movie_2 = movie_repository_singleton._db.pop()

    assert movie_2.title == title
    assert movie_2.director == director
    assert movie_2.rating == rating



    # assert movie[0] == 'Saving Private Ryan'
    #assert movie[1] == 'Steven Spielburg'
    #assert movie[2] == 5
