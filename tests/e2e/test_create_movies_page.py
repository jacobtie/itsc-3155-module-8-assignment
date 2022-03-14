# TODO: Feature 2
# importing app to send requests to client
#we are testing this function in app.py outside this folder
# @app.post('/movies')
# def create_movie():
#     # TODO: Feature 2
#     #when user submits form, create a new movie
#     title = request.form.get('title')
#     director = request.form.get('director')
#     rating = request.form.get('rating')
#     movie_repository_singleton.create_movie(title, director, rating)
#     # After creating the movie in the database, we redirect to the list all movies page
#     return redirect('/movies')
import pytest



@pytest.fixture(scope='module')


def test_create_movie(client):
    response = client.post('/movies', data=dict(title='Matrix', director='Wachowski', rating='5'))
    # test to see if the response is a redirect to the list all movies page
    assert response.location == 'http://localhost/movies'
