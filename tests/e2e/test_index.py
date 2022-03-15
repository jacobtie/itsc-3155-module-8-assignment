def test_home_page(app):
    response = app.get('/')
    response_data = response.data

    assert b'<h1 class="mb-5">Movie Rating App</h1>' in response_data
