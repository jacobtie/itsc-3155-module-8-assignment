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
    movie_title = request.form.get('title')
    movie_director = request.form.get('director')
    movie_rating = request.form.get('rating')
    # get all the necessary info from the html form (title, director, rating)

    movie_db = movie_repository_singleton  # object for movie_repository
    movie_db.create_movie(movie_title, movie_director, movie_rating)  # create a movie using the above features
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)


if __name__ == "__main__": 
    app.run(debug=True)