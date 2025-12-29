# input = "KH,2H,KS,2S,6D"
input = "KH,QH,9H,0H,JH"

hand = input.split(",")

card_ranking = "234567890JQKA"  # Note that 10 is represented by '0'


def extract_hand_values(hand: list):
    values = [c[0] for c in hand]
    suits = [c[1] for c in hand]
    # This uses the card ranking as the key so we can use it for easy ordering
    value_counts = {card_ranking.find(v): values.count(v) for v in values}

    return value_counts

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

def has_straight(hand) -> bool:
    ranks = [card_ranking.find(c[0]) for c in hand]
    ranks.sort()
    sorted_vals = [card_ranking[i] for i in ranks]
    return "".join(sorted_vals) in card_ranking


hand_values = extract_hand_values(hand)
print(hand_values)
print(has_straight(hand))
print (has_four_of_a_kind(hand_values))
print (has_full_house(hand_values))
print (has_three_of_a_kind(hand_values))
print (has_two_pair(hand_values))
print (has_pair(hand_values))


"""
Assumptions/Notes:
- Only assessing ranking for High games, not low games or high-low split games
"""