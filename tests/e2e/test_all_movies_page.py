from flask import Flask
from src.repositories import movie_repository
from src.models.movie import Movie
from app import app, create_movie
from src.repositories.movie_repository import MovieRepository


def test_movies_response():
    c = app.test_c()
    r = c.get('/movies')

    assert r.status_code == 200


def test_movies_displayed():

    #Adds movie to the data, reload the page to view
    ed_movie = movie_repository.movie_repository_singleton.create_movie(title='The Batman',director='Matt Reeves',rating= '4.6')

    c = app.test_c()
    r = c.get('/movies')

    #Checks the data
    assert b'<h1 class="mb-5">All Movies</h1>' in r.data
    assert b'<th> Title </th>' in r.data
    assert b'<td>Edward Scissorhands</td>' in r.data

    #Extra case
    assert b'<td>Ang Lee</td>' not in r.data


    #Closes the session
    r.close() 


    #Adds second movie to the data, reload the page to view
    pi_movie = movie_repository.movie_repository_singleton.create_movie(title='Uncharted', director= 'Ruben Fleischer', rating='4.2')
    c = app.test_c()
    r = c.get('/movies')

    #Checks the data
    assert b'<td>Life of Pi</td>' in r.data 

    #Closes the session
    r.close()