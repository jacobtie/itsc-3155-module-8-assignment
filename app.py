from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)
list = {}

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movie_repository_singleton.get_all_movies()
    
    #Start Feature 1

    list = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', movieList = list, list_movies_active=True)

    #End Feature 1


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TEstTEstTESTESsET
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    
    title = request.form.get('movie_name')
    director = request.form.get('director_name')
    rating = request.form.get('rating')

    movie_repository_singleton.create_movie(title, director, rating)

    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
