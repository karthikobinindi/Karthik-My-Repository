import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

@pytest.fixture
def movie_data():
    return {
        "id": 105,
        "movie_name": "Dune",
        "language": "English",
        "duration": "2h 35m",
        "price": 280
    }

def test_get_all_movies():
    response = requests.get(f"{BASE_URL}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_movie(movie_data):
    response = requests.post(f"{BASE_URL}/api/movies", json=movie_data)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Dune"

def test_book_ticket():
    booking = {"movie_id": 101, "tickets": 2}
    response = requests.post(f"{BASE_URL}/api/bookings", json=booking)
    assert response.status_code == 201
    assert response.json()["total_price"] == 500
