# TODO: Feature 1
from urllib import response
from app import app
def test_movie_page():
    test_app = app.test_client()
    response = test_app.get('/movies')
    assert b"<th scope='col'>Title</th>" in response.data
    assert b"<th scope='col'>Director</th>" in response.data
    assert b"<th scope='col'>Rating</th>" in response.data
