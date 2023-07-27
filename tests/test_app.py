import sys
import os
import pytest

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_successful_swap_case_string(client):
    data = {"string": "abcDEF"}
    response = client.post("/", json=data)
    assert response.status_code == 200
    assert response.json == {"result": "ABCdef"}

def test_missing_string_parameter(client):
    data = {}
    response = client.post("/", json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Invalid input. 'string' parameter not found or not a string."}

def test_invalid_string_parameter(client):
    data = {"string": 123}
    response = client.post("/", json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Invalid input. 'string' parameter not found or not a string."}

def test_internal_server_error(client):
    # Simulate an internal server error
    data = "invalid_data"
    response = client.post("/", data=data)
    assert response.status_code == 500
    assert response.json == {"error": "Internal Server Error"}

def test_not_found_error(client):
    # Simulate a request to an undefined route
    response = client.get("/undefined_route")
    assert response.status_code == 404
    assert response.json == {"error": "Not Found"}
