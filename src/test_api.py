from fastapi.testclient import TestClient
from .api import app


client = TestClient(app)

def test_home_with_no_data():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome"}

def test_home_with_high_card_hand():
    response = client.get("/?cards=4H&cards=6H&cards=JD&cards=3H&cards=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "High Card: Q"}

def test_home_with_pair_hand():
    response = client.get("/?cards=4H&cards=4D&cards=JD&cards=3H&cards=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Pair"}

def test_home_with_two_pair_hand():
    response = client.get("/?cards=4H&cards=4D&cards=JD&cards=JH&cards=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Two Pair"}

def test_home_with_three_of_kind_hand():
    response = client.get("/?cards=4H&cards=4D&cards=4C&cards=JH&cards=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Three of a kind"}

def test_home_with_straight_hand():
    response = client.get("/?cards=4H&cards=5D&cards=6C&cards=7H&cards=8H")
    assert response.status_code == 200
    assert response.json() == {"msg": "Straight"}

def test_home_with_flush_hand():
    response = client.get("/?cards=4H&cards=5H&cards=QH&cards=AH&cards=8H")
    assert response.status_code == 200
    assert response.json() == {"msg": "Flush"}

def test_home_with_full_house_hand():
    response = client.get("/?cards=4H&cards=4D&cards=QH&cards=QD&cards=QC")
    assert response.status_code == 200
    assert response.json() == {"msg": "Full House"}

def test_home_with_four_of_kind_hand():
    response = client.get("/?cards=4H&cards=QS&cards=QH&cards=QD&cards=QC")
    assert response.status_code == 200
    assert response.json() == {"msg": "Four of a kind"}

def test_home_with_straight_flush_hand():
    response = client.get("/?cards=4H&cards=5H&cards=6H&cards=7H&cards=8H")
    assert response.status_code == 200
    assert response.json() == {"msg": "Straight Flush"}

def test_home_with_royal_flush_hand():
    response = client.get("/?cards=KH&cards=0H&cards=JH&cards=AH&cards=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Royal Flush"}
