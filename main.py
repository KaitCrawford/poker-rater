input = "KH,2H,KS,2S,6D"

hand = input.split(",")


def extract_hand_values(hand: list):
    value_dict = {}
    for card in hand:
        if card[0] in value_dict:
            value_dict[card[0]] +=1
        else:
            value_dict[card[0]] = 1


    return value_dict

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

hand_values = extract_hand_values(hand)
print(hand_values)
print (has_four_of_a_kind(hand_values))
print (has_full_house(hand_values))
print (has_three_of_a_kind(hand_values))
print (has_two_pair(hand_values))
print (has_pair(hand_values))