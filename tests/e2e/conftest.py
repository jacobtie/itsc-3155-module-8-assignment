import pytest
from app import app as a


@pytest.fixture(scope='module')
def app():
    return a.test_client()
