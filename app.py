from flask import Flask, redirect, render_template
from flask import request
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
    print("herenew")
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    mname = request.form.get('name')
    mdir=request.form.get('director')
    mrat=request.form.get('inlineRadioOptions')
    print(mname)
    print(mdir)
    print(mrat)
    if(movie_repository_singleton.get_movie_by_title(mname)==None):
        movie_repository_singleton.create_movie(mname, mdir, mrat)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
