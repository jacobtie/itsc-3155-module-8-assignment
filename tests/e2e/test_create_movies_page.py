# TODO: Feature 2

from app import app
def test_index_page():
    test_app = app.test_client()
    response = test_app.get('/movies/new')
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response.data
    assert b'<form action="/movies" method="post">' in response.data
    

    


