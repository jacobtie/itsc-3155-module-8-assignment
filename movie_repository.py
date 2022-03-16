from src.models.movie import Movie


class MovieRepository:

    def __init__(self) -> None:
        # In memory database which is a simple list of movies
        self._db: list[Movie] = []

    def get_all_movies(self) -> list[Movie]:
        # Simply return all movies from the in-memory database
        return self._db

    def get_movie_by_title(self, title: str) -> Movie | None:
        # Perform a linear search through the in-memory database
        for movie in self._db:
            # If the movie title matches, return the movie
            if movie.title == title:
                return movie
        # If we made it this far, no movies matched so return None
        return None

    def create_movie(self, title: str, director: str, rating: int) -> Movie:
        # Create the movie instance
        movie = Movie(title, director, rating)
        # Save the instance in our in-memory database
        self._db.append(movie)
        # Return the movie instance
        return movie


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
