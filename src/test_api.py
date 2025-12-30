from fastapi.testclient import TestClient
from .api import app


client = TestClient(app)

def test_get_home_with_no_data():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome"}
