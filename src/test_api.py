from fastapi.testclient import TestClient

from .api import app

client = TestClient(app)


def test_home_with_no_data():
    response = client.get("/")
    assert response.status_code == 422
    assert response.json()["detail"][0]["msg"] == "Field required"


def test_home_with_high_card_hand():
    response = client.get("/?cards=4H&cards=6H&cards=JD&cards=3H&cards=QH")
    assert response.status_code == 200
    assert response.json() == {"msg": "High Card: Q"}


def test_home_with_high_card_10_hand():
    response = client.get("/?cards=4H&cards=6H&cards=9D&cards=3H&cards=0H")
    assert response.status_code == 200
    assert response.json() == {"msg": "High Card: 10"}


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


def test_home_with_5_high_straight_hand():
    response = client.get("/?cards=4H&cards=5D&cards=3C&cards=2H&cards=AH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Straight"}


def test_home_with_5_high_straight_flush_hand():
    response = client.get("/?cards=4H&cards=5H&cards=3H&cards=2H&cards=AH")
    assert response.status_code == 200
    assert response.json() == {"msg": "Straight Flush"}


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


def test_home_with_more_than_5_cards():
    response = client.get("/?cards=KH&cards=0H&cards=JH&cards=AH&cards=QH&cards=5H")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "List should have at most 5 items after validation, not 6"
    )


def test_home_with_less_than_5_cards():
    response = client.get("/?cards=KH&cards=0H&cards=JH&cards=AH")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "List should have at least 5 items after validation, not 4"
    )


def test_home_duplicate_cards():
    response = client.get("/?cards=KH&cards=0H&cards=KH&cards=AH&cards=QH")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Value error, Cards may not be duplicated."
    )


def test_card_code_too_long():
    response = client.get("/?cards=KHD&cards=0H&cards=KH&cards=AH&cards=QH")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Value error, Invalid Card: KHD (unrecognised card)"
    )


def test_card_code_too_short():
    response = client.get("/?cards=K&cards=0H&cards=KH&cards=AH&cards=QH")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Value error, Invalid Card: K (unrecognised card)"
    )


def test_card_invalid_value():
    response = client.get("/?cards=1H&cards=0H&cards=KH&cards=AH&cards=QH")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Value error, Invalid Card: 1H (unrecognised value)"
    )


def test_card_invalid_suit():
    response = client.get("/?cards=AG&cards=0H&cards=KH&cards=AH&cards=QH")
    assert response.status_code == 422
    assert (
        response.json()["detail"][0]["msg"]
        == "Value error, Invalid Card: AG (unrecognised suit)"
    )
