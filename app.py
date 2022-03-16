from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)
movies = {}
names = []
movies_directors = {}
movies_ratings = {} 

@app.get('/')
def index():
    return render_template('index.html')


@app.post('/movies')
def list_all_movies():
    # feature 1 location found 
    # TODO: Feature 1

    # obtain form data
    name = request.form.get('movie')
    director = request.form.get('director') 
    rating = request.form.get('rating')

    # store data in appropriate container
    names.append(name)
    movies_directors[name] = director 
    movies_ratings[name] = rating

    # render page
    return render_template('list_all_movies.html', movies_directors = movies_directors, movies_ratings = movies_ratings, names = names, list_movies_active=True)
    



@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    #Feature 2 - done by Ryan Braswell
    name = request.form.get('movie')
    director = request.form.get('director') #gets data from the webpage
    rating = request.form.get('rating')

    NewMovie = movie_repository_singleton.create_movie(name, director, rating) #creats movie object

    #After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')
 

@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)
