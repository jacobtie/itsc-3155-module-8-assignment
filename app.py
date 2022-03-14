from flask import Flask, redirect, render_template, request, abort
from src.repositories.movie_repository import movie_repository_singleton
# from src.models.movie import Movie

app = Flask(__name__)

#result = [[]] #empty list in a list to store movie (not working)



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

    return redirect('/movies')

@app.get('/movies/search') #Route to the Search Movies form
def search_movies():
    #clear previous searches
    # result.pop[:]
    return render_template('search_movies.html')


@app.get('/result') #route to search resule
def result():
    input_movie = request.args.get('input_movie', 'Error: No Parameter')
    movie_repository_singleton.get_movie_by_title(input_movie) #returns a movie object
    # result.append(searched_movie) #add movie to empty result movie

    #variables for title and rating
    title = input_movie.title()
    #rating = input_movie.rating() #keep getting a typecast error, and cannot figure out how to fix
    
    return render_template('result.html', title=title, input_movie=input_movie)
    
    #rating=rating) #commented out b/c not working due to typecast error

#References for Implement #3: 
# https://www.geeksforgeeks.org/different-ways-to-clear-a-list-in-python/