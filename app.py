from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie


from src.models.movie import Movie
app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movies = movie_repository_singleton.get_all_movies()
    return render_template('list_all_movies.html', list_movies_active=True, movies = movies)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2  by Nick koehler
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get('title')
    name = request.form.get('name')
    rating = request.form.get('rating')

    create_movie(title, name, rating)
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    return render_template('search_movies.html', search_active=True)

@app.post('/movies/search/<movie>')
def feature3(movie):
    
    movie = request.form["mname"]
    if movie_repository_singleton.get_movie_by_title(movie) == None:
        return "404"
    else:
        return movie_repository_singleton.get_movie_by_title(movie)
    
    

app.run()