from flask import Flask
from src.repositories import movie_repository
from src.models.movie import Movie
from app import app, create_movie
from src.repositories.movie_repository import MovieRepository
import pytest
import unittest

# TODO: Feature 1

def test_all():
    temp = MovieRepository()
    temp_list = MovieRepository.get_all_movies(self=temp)
    assert len(temp_list) == 0
    temp.create_movie(title='Title', director='Director', rating= '5')
    temp_list = MovieRepository.get_all_movies(self=temp)
    assert(len(temp_list) == 1)
