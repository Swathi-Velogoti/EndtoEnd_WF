import pytest
from hello_world import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_world(client):
    """Test the hello world route."""
    rv = client.get('/')
    assert rv.data == b'Hello, World!'
