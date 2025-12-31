from typing import Annotated

from fastapi import FastAPI, Query

from .main import *

app = FastAPI()


@app.get("/")
async def get_hand_rating(cards: Annotated[list[str] | None, Query(alias="card")] = None) -> dict:
    if not cards:
        return {"msg": "Welcome"}

    hand = cards
    hand_info = extract_hand_info(hand)

    if has_three_of_a_kind(hand_info["val_counts"]):
        return {"msg": "Three of a kind"}
    if has_two_pair(hand_info["val_counts"]):
        return {"msg": "Two Pair"}
    if has_pair(hand_info["val_counts"]):
        return {"msg": "Pair"}
    return {"msg": f'High Card: {high_card(hand_info["values"])}'}
