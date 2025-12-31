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

    return {"msg": f'High Card: {high_card(hand_info["values"])}'}
