from typing import Annotated
from annotated_types import Len

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, BeforeValidator, computed_field


CARD_RANKING = "234567890JQKA"  # Note that 10 is represented by '0'
VALID_SUITS = "HDCS"


def validate_card(value: str) -> str:
    """
    Valid cards are represented by a 2 character code: value and suit
    """
    if len(value) != 2:
        raise ValueError(f"Invalid Card: {value} (unrecognised card)")
    if value[0] not in CARD_RANKING:
        raise ValueError(f"Invalid Card: {value} (unrecognised value)")
    if value[1] not in VALID_SUITS:
        raise ValueError(f"Invalid Card: {value} (unrecognised suit)")
    return value


class Card(BaseModel):
    code: Annotated[str, BeforeValidator(validate_card)]

    @computed_field
    @property
    def value(self) -> str:
        return self.code[0]

    @computed_field
    @property
    def suit(self) -> str:
        return self.code[1]


def has_duplicates(value: list) -> list:
    if len(set(value)) != len(value):
        raise ValueError("Cards may not be duplicated.")
    return value


def format_cards(value: list[str]) -> list[dict]:
    # Note: This transformation of the data is necessary for the Card instances to be
    # created. It might have been better to do this all as POST requests and send the
    # cards as json dicts
    return [{"code": c} for c in value]


class Hand(BaseModel):
    cards: Annotated[
        list[Card],
        Len(min_length=5, max_length=5),
        BeforeValidator(format_cards),
        BeforeValidator(has_duplicates),
    ]

    @computed_field
    @property
    def values(self) -> list:
        # Returns a list of the card values ordered by rank
        ranks = [CARD_RANKING.find(c.value) for c in self.cards]
        ranks.sort()
        return [CARD_RANKING[i] for i in ranks]

    @computed_field
    @property
    def suits(self) -> list:
        return [c.suit for c in self.cards]

    @computed_field
    @property
    def value_counts(self) -> dict:
        values = [c.value for c in self.cards]
        # This uses the card ranking as the key so we can use it for easy ordering
        return {CARD_RANKING.find(v): values.count(v) for v in values}

    def high_card(self) -> str:
        if self.values[-1] == "0":
            return 10
        return self.values[-1]

    def has_pair(self) -> bool:
        if 2 in self.value_counts.values():
            return True
        else:
            return False

    def has_two_pair(self) -> bool:
        if sum(1 for v in self.value_counts.values() if v == 2) == 2:
            return True
        else:
            return False

    def has_three_of_a_kind(self) -> bool:
        if 3 in self.value_counts.values():
            return True
        else:
            return False

    def has_straight(self) -> bool:
        hand_vals = "".join(self.values)
        if hand_vals in f"{CARD_RANKING[0:4]}A":
            # Support for 5 high straight (hand_vals would be 2345A)
            return True
        return hand_vals in CARD_RANKING

    def has_flush(self) -> bool:
        return self.suits.count(self.suits[0]) == 5

    def has_full_house(self) -> bool:
        if self.has_three_of_a_kind() and self.has_pair():
            return True
        else:
            return False

    def has_four_of_a_kind(self) -> bool:
        if 4 in self.value_counts.values():
            return True
        else:
            return False

    def has_straight_flush(self) -> bool:
        return self.has_flush() and self.has_straight()

    def has_royal_flush(self) -> bool:
        return (
            self.has_flush()
            and self.has_straight()
            and self.values == ["0", "J", "Q", "K", "A"]
        )


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8000",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_hand_rating(hand: Annotated[Hand, Query()]) -> dict:
    if hand.has_royal_flush():
        return {"msg": "Royal Flush"}
    if hand.has_straight_flush():
        return {"msg": "Straight Flush"}
    if hand.has_four_of_a_kind():
        return {"msg": "Four of a kind"}
    if hand.has_full_house():
        return {"msg": "Full House"}
    if hand.has_flush():
        return {"msg": "Flush"}
    if hand.has_straight():
        return {"msg": "Straight"}
    if hand.has_three_of_a_kind():
        return {"msg": "Three of a kind"}
    if hand.has_two_pair():
        return {"msg": "Two Pair"}
    if hand.has_pair():
        return {"msg": "Pair"}
    return {"msg": f"High Card: {hand.high_card()}"}


"""
Assumptions/Notes:
- Only assessing ranking for High games, not low games or high-low split games

TODO:
- Support for aces low rules
- run linting tools
"""
