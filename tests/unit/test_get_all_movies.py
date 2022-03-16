from flask import Flask
import pytest
import unittest
from app import list_all_movies
from src.repositories import movie_repository
from src.models.movie import Movie

from src.repositories.movie_repository import MovieRepository


def test_movies_displayed():

    #New instance created
    new_repo = MovieRepository()
    #Creates a variable to get the list of movies
    movielist = MovieRepository.get_all_movies(self= new_repo)
    #Checks to see if the list is empty
    assert len(movielist) == 0

    #Creates an entry to add to the movie list
    new_repo.create_movie(title='The Batman',director='Matt Reeves',rating= '4.6')
    #Adds the entry to the list
    movielist = MovieRepository.get_all_movies(self= new_repo)
    #Checks to see if there's one movie in the list
    assert(len(movielist) == 1)

    #Creates an entry to add to the movie list
    new_repo.create_movie(title='Uncharted', director= 'Ruben Fleischer', rating='4.2')
    #Adds the entry to the list
    movielist = MovieRepository.get_all_movies(self= new_repo)
    #Checks to see if there's two movies in the list
    assert(len(movielist) == 2)


    if __name__ == '__main__':
        test_movies_displayed.main()
