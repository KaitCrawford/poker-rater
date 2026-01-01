from typing import Annotated

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, computed_field


CARD_RANKING = "234567890JQKA"  # Note that 10 is represented by '0'


class Hand(BaseModel):
    cards: list[str] = []

    @computed_field
    @property
    def values(self) -> list:
        ranks = [CARD_RANKING.find(c[0]) for c in self.cards]
        ranks.sort()
        return [CARD_RANKING[i] for i in ranks]

    @computed_field
    @property
    def suits(self) -> list:
        return [c[1] for c in self.cards]

    @computed_field
    @property
    def value_counts(self) -> dict:
        values = [c[0] for c in self.cards]
        # This uses the card ranking as the key so we can use it for easy ordering
        return {CARD_RANKING.find(v): values.count(v) for v in values}

    def high_card(self) -> str:
        return self.values[-1]

    def has_pair(self) -> bool:
        if 2 in self.value_counts.values():
            return True
        else:
            return False

    def has_two_pair(self) -> bool:
        if sum(1 for v in self.value_counts.values() if v==2) ==2:
            return True
        else:
            return False

    def has_three_of_a_kind(self) -> bool:
        if 3 in self.value_counts.values():
            return True
        else:
            return False

    def has_straight(self) -> bool:
        return "".join(self.values) in CARD_RANKING

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
            self.has_flush() and
            self.has_straight() and
            self.values[-1] == "A"
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
async def get_hand_rating(hand: Annotated[Hand, Query()] = None) -> dict:
    if not hand or not hand.cards:
        return {"msg": "Welcome"}

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
    return {"msg": f'High Card: {hand.high_card()}'}


"""
Assumptions/Notes:
- Only assessing ranking for High games, not low games or high-low split games

TODO:
- Validation!!!! (and tests)
-- Ideally this would involve making a Card class
- Support for 5 high straight
- Support for aces low rules
- run linting tools
"""
