def extract_hand_info(hand: list) -> dict:
    """
    This function will probably be refactored as multiple attr functions on the Hand class
    """
    ranks = [card_ranking.find(c[0]) for c in hand]
    ranks.sort()
    sorted_vals = [card_ranking[i] for i in ranks]

    values = [c[0] for c in hand]
    suits = [c[1] for c in hand]
    # This uses the card ranking as the key so we can use it for easy ordering
    value_counts = {card_ranking.find(v): values.count(v) for v in values}

    return {"values": sorted_vals, "suits": suits, "val_counts": value_counts}

def has_four_of_a_kind(values_dict: dict) -> bool:
    if 4 in values_dict.values():
        return True
    else:
        return False

def has_three_of_a_kind(values_dict: dict) -> bool:
    if 3 in values_dict.values():
        return True
    else:
        return False

def has_pair(values_dict: dict) -> bool:
    if 2 in values_dict.values():
        return True
    else:
        return False

def has_full_house(values_dict: dict) -> bool:
    if has_three_of_a_kind(values_dict) and has_pair(values_dict):
        return True
    else:
        return False

def has_two_pair(values_dict: dict) -> bool:
    if sum(1 for v in values_dict.values() if v==2) ==2:
        return True
    else:
        return False

def has_straight(sorted_vals) -> bool:
    return "".join(sorted_vals) in card_ranking

def has_flush(suits) -> bool:
    return suits.count(suits[0]) == 5

def has_straight_flush(hand_info) -> bool:
    return has_flush(hand_info["suits"]) and has_straight(hand_info["values"])

def has_royal_flush(hand_info) -> bool:
    return (
        has_flush(hand_info["suits"]) and
        has_straight(hand_info["values"]) and
        hand_info["values"][-1] == "A"
    )

def high_card(values) -> str:
    return values[-1]


if __name__ == "__main__":
    # input = "KH,2H,KS,2S,6D"
    input = "KH,QH,AH,0H,JH"

    hand = input.split(",")

    card_ranking = "234567890JQKA"  # Note that 10 is represented by '0'

    hand_info = extract_hand_info(hand)
    print(hand_info)
    print(has_royal_flush(hand_info))
    print(has_straight_flush(hand_info))
    print(has_flush(hand_info["suits"]))
    print(has_straight(hand_info["values"]))
    print(has_four_of_a_kind(hand_info["val_counts"]))
    print(has_full_house(hand_info["val_counts"]))
    print(has_three_of_a_kind(hand_info["val_counts"]))
    print(has_two_pair(hand_info["val_counts"]))
    print(has_pair(hand_info["val_counts"]))
    print(high_card(hand_info["values"]))



"""
Assumptions/Notes:
- Only assessing ranking for High games, not low games or high-low split games
"""