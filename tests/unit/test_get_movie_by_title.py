from src.repositories.movie_repository import MovieRepository

def test_get_all_movies():
    repo = MovieRepository()
   
   #create and add movies to database
    repo.create_movie("Batman", "Caden", 4)
    repo.create_movie("Superman", "William", 5)
    repo.create_movie("Hulk", "Josh", 3)
    repo.create_movie("Star Wars", "George Lucas", 5)
    repo.create_movie("Cats", "Tom Hooper", 1)

    #Test
    assert repo.get_movie_by_title("Batman").title == "Batman"
    assert repo.get_movie_by_title("Superman").title == "Superman"
    assert repo.get_movie_by_title('Hulk').title == "Hulk"
    assert repo.get_movie_by_title('Star Wars').title == "Star Wars"
    assert repo.get_movie_by_title('Cats').title == "Cats"

    #create variables for test
    movie01 = repo.get_movie_by_title("Batman")
    movie02 = repo.get_movie_by_title("is not a movie")
    movie03 = repo.get_movie_by_title("")
    movie04 = repo.get_movie_by_title("StarWars")
    movie05 = repo.get_movie_by_title("Cats")     

    #Test
    assert movie01 is not None
    assert movie02 is None
    assert movie03 is None
    assert movie04 is None
    assert movie05 is not None
