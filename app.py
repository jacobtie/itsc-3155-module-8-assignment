from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)

returned_search = []

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


@app.get('/movies/search')
def search_movies():
    search_input = request.args.get('search_input')
    returned_search.clear() #clears any previous searches from list variable
    searched_movie = movie_repository_singleton.get_movie_by_title(str(search_input))
    returned_search.append(searched_movie)

    return render_template('search_movies.html', search_input=search_input, returned_search=returned_search, search_active=True)
