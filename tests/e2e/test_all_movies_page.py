from flask import Flask
from src.repositories import movie_repository
from src.models.movie import Movie
from app import app, create_movie
from src.repositories.movie_repository import MovieRepository


def test_movies_response():
    client = app.test_client()
    response = client.get('/movies')

    assert response.status_code == 200


def test_movies_displayed():
    
    #add a movie and reload page to get data
    ed_movie = movie_repository.movie_repository_singleton.create_movie(title='Edward Scissorhands',director='Tim Burton',rating= '4.5')
    
    client = app.test_client()
    response = client.get('/movies')

    #data checks
    assert b'<h1 class="mb-5">All Movies</h1>' in response.data
    assert b'<th> Title </th>' in response.data
    assert b'<td>Edward Scissorhands</td>' in response.data

    #edge case
    assert b'<td>Ang Lee</td>' not in response.data

    response.close()
    #close the session 


    #add another movie and reload page to refresh data
    pi_movie = movie_repository.movie_repository_singleton.create_movie(title='Life of Pi', director='Ang Lee',rating= '4')
    client = app.test_client()
    response = client.get('/movies')

    #data checks
    assert b'<td>Life of Pi</td>' in response.data 

    response.close()
    #close the session 
