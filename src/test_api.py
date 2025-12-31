from fastapi.testclient import TestClient
from .api import app


client = TestClient(app)

def test_home_with_no_data():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome"}

def test_home_with_high_card_hand():
    response = client.get("/?card=4H&card=6H&card=JD&card=3H&card=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "High Card: Q"}

def test_home_with_pair_hand():
    response = client.get("/?card=4H&card=4D&card=JD&card=3H&card=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Pair"}

def test_home_with_two_pair_hand():
    response = client.get("/?card=4H&card=4D&card=JD&card=JH&card=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Two Pair"}

def test_home_with_three_of_kind_hand():
    response = client.get("/?card=4H&card=4D&card=4C&card=JH&card=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Three of a kind"}

def test_home_with_straight_hand():
    response = client.get("/?card=4H&card=5D&card=6C&card=7H&card=8H")
    assert response.status_code == 200
    assert response.json() == {"msg": "Straight"}
