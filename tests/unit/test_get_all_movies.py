from flask import Flask
import pytest
import unittest
from app import list_all_movies
from src.repositories import movie_repository
from src.models.movie import Movie

from src.repositories.movie_repository import MovieRepository



def test_movies_displayed():

    #create new instance
    new_repos = MovieRepository()
    #get the list of movies
    movie_list = MovieRepository.get_all_movies(self= new_repos)
    #make sure its empty
    assert len(movie_list) == 0

    #lets add something
    new_repos.create_movie(title='Edward Scissorhands',director='Tim Burton',rating= '4.5')
    #replace movie_list with the updated movie_list
    movie_list = MovieRepository.get_all_movies(self= new_repos)
    #check size
    assert(len(movie_list) == 1)

    new_repos.create_movie(title='Life of Pi', director= 'Ang Lee', rating='5')
    #replace movie_list with the updated movie_list
    movie_list = MovieRepository.get_all_movies(self= new_repos)
    #check size
    assert(len(movie_list) == 2)


    if __name__ == '__main__':
        test_movies_displayed.main()

        

