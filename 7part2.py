from datetime import datetime
from collections import Counter
startTime = datetime.now()

LETTER_CARDS = {
        'A' : 14,
        'K' : 13,
        'Q' : 12,
        'J' : 1,
        'T' : 10
    }

def get_list_hand_from_string_hand(string_hand):
    hand = []



    for char in string_hand:
        if char in LETTER_CARDS.keys():
            hand.append(LETTER_CARDS[char])
        else:
            hand.append(int(char))

    return tuple(hand)

def parse(input_data):
    lines = input_data.splitlines()

    hands = {}

    for line in lines:
        line_split = line.split()
        string_hand = line_split[0]
        bid = int(line_split[1])
        hands[get_list_hand_from_string_hand(string_hand)] = bid

    return hands

def get_hand_type(hand):
    card_counts = sorted(Counter(hand).values(), reverse=True)

    if card_counts == [5]:
        return "Five of a kind"
    elif card_counts == [4,1]:
        return "Four of a kind"
    elif card_counts == [3,2]:
        return "Full house"
    elif card_counts == [3,1,1]:
        return "Three of a kind"
    elif card_counts == [2,2,1]:
        return "Two pair"
    elif card_counts == [2,1,1,1]:
        return "One pair"
    else:
        return "High card"

def get_joker_hand_type(hand):

    card_counter = Counter(hand)
    most_common_card = card_counter.most_common(1)[0][0]
    if most_common_card == 1 and len(card_counter.most_common(2)) > 1:
        replace_joker_with = card_counter.most_common(2)[1][0]
    else:
        replace_joker_with = most_common_card

    revised_hand = [replace_joker_with if i == LETTER_CARDS["J"] else i for i in hand]

    return(get_hand_type(revised_hand))

HAND_TYPE_TO_VALUE = {
    "Five of a kind" : 6,
    "Four of a kind" : 5,
    "Full house" : 4,
    "Three of a kind": 3,
    "Two pair": 2,
    "One pair": 1,
    "High card": 0
}

def get_hand_value(hand):
    # hand value = hand_type_value, lacks_joker, card values
    if LETTER_CARDS["J"] in hand:
        type_value = HAND_TYPE_TO_VALUE[get_joker_hand_type(hand)]
        return (type_value,) + hand
    else:
        type_value = HAND_TYPE_TO_VALUE[get_hand_type(hand)]
        return (type_value,) + hand

def sort_hands(hands):
    return sorted(hands,key=get_hand_value)

def get_hand_rankings(hands):
    sorted_hands = sort_hands(hands)
    hand_to_rank = {}
    for i, hand in enumerate(sorted_hands):
        hand_to_rank[hand] = i+1

    return hand_to_rank

if __name__ == "__main__":
    with open('7input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""

    hand_to_bid = parse(input_data)
    hand_to_rank = get_hand_rankings(hand_to_bid.keys())

    running_sum = 0
    for hand, rank in hand_to_rank.items():
        bid = hand_to_bid[hand]
        running_sum += bid*rank
    
    print(running_sum)