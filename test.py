# from flask import Flask, redirect, render_template, request
from src.repositories.movie_repository import movie_repository_singleton

returned_search = [] #empty list to store the searched repository movie

#search_input = request.args.get('search_input') #gets the input from the movie search form
search_input = 'abc'
returned_search.clear() #clears any previous searches from list variable
searched_movie = movie_repository_singleton.get_movie_by_title(search_input) #searches movie repository for the input movie
returned_search.append(searched_movie) #stores the movie in the empty list  

for searched_movie in returned_search: 
    print(searched_movie.title)
    print(searched_movie.director)
    print(searched_movie.rating)