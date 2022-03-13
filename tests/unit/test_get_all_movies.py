#https://www.youtube.com/watch?v=sL_PWBOABWo 
#https://codethechange.stanford.edu/guides/guide_flask_unit_testing.html
# TODO: Feature 1
# import os, sys, json
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app import app

def test_list_all_movies():
    response = app.test_client().get('/movies') #gets the /movies page and stores to response
    
    assert response._status_code == 200 #checks if the reuqest above is successful