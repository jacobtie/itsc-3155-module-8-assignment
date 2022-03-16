from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.route('/movies/search')
def search_movies():
    # TODO: Feature 3
    movie = request.args.get('movie')
    # movie_repository_singleton.create_movie("Fire","Hans","5")
    movie = movie_repository_singleton.get_movie_by_title(movie)
    if movie == None:
        return render_template('search_movies.html', search_active=True, data = "Movie not found")
    else:
        return render_template('search_movies.html', search_active=True, data = "The rating of " +  movie.title + " is " + movie.rating)
        
    