from pytest import fail
from src.models.movie import Movie
from src.repositories.movie_repository import MovieRepository

def test_get_all_movies():
    repo = MovieRepository()
   
    

    repo.create_movie("Batman", "Caden", 4)
    repo.create_movie("Superman", "William", 5)
    repo.create_movie("Hulk", "Josh", 3)
    repo.create_movie("Star Wars", "George Lucas", 5)
    repo.create_movie("Cats", "Tom Hooper", 1)

  



    assert repo.get_movie_by_title("Batman").title == "Batman"
    assert repo.get_movie_by_title("Superman").title == "Superman"
    assert repo.get_movie_by_title('Hulk').title == "Hulk"
    assert repo.get_movie_by_title('Star Wars').title == "Star Wars"
    assert repo.get_movie_by_title('Cats').title == "Cats"



    movie01 = repo.get_movie_by_title("Batman")
    movie02 = repo.get_movie_by_title("Superman")
    movie03 = repo.get_movie_by_title("Hulk")
    movie04 = repo.get_movie_by_title("Star Wars")
    movie05 = repo.get_movie_by_title("Cats")     

    if movie01 == None:
        assert False
    else: 
        assert True

    
    if movie01 == None:
        assert False
    elif movie02 == None:
        assert False
    elif movie03 == None:
        assert False
    elif movie04 == None:
        assert False
    elif movie05 == None: 
        assert False
    else: 
        assert True