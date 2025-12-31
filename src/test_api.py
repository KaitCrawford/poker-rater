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
