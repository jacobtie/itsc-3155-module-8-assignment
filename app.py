from flask import Flask, redirect, render_template
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1 (Can Ngo)
    # Create a dictionary mapping the movie title to the movie's rating
    movie_ratings = dict()
    # loop through all movies we have right now
    for movie in movie_repository_singleton.get_all_movies():
        # map the corresponding title to its rating
        movie_ratings[movie.title] = movie.rating
    # make list_movies_active be equal to the movie_ratings dictionary.
    # This will make it so list_all_movies.html will present the movie_ratings dictionary as the list_movies_active
    return render_template('list_all_movies.html', list_movies_active=movie_ratings)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
