import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Astronauts API is running!" in response.data

def test_api_astronauts(client):
    response = client.get("/api/astronauts")
    assert response.status_code == 200
    assert response.is_json
    assert isinstance(response.get_json(), list)

def test_dashboard(client):
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Astronauts Dashboard" in response.data
