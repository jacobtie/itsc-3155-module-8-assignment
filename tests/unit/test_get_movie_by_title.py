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

    # title01 = "Batman"
    # title02 = "Superman"
    # title03 = "Hulk"
    # title04 = "Star Wars"
    # title05 = "Cats"





    assert repo.get_movie_by_title("Batman").title == "Batman"
    assert repo.get_movie_by_title("Superman").title == "Superman"
    assert repo.get_movie_by_title('Hulk').title == "Hulk"
    assert repo.get_movie_by_title('Star Wars').title == "Star Wars"
    assert repo.get_movie_by_title('Cats').title == "Cats"

    try: 
        repo.get_movie_by_title("Batman")
        repo.get_movie_by_title("Superman")
        repo.get_movie_by_title("Hulk")
        repo.get_movie_by_title("Star Wars")
        repo.get_movie_by_title("Cats")
        assert False
    except:
        assert True