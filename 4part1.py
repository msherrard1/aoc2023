import re

def load_cards(input_data):
    cards = {}

    for line in input_data.splitlines():
        split_string = re.split(r"[:|]",line)
        card_id = int(split_string[0].split()[1])
        winning_nums = [int(x) for x in split_string[1].split()]
        have_nums = [int(x) for x in split_string[2].split()]
        cards[card_id] = (winning_nums, have_nums)
    
    return cards

def check_card_value(card_content):
    winning_nums = card_content[0]
    have_nums = card_content[1]
    matches = 0

    for have_num in have_nums:
        for winning_num in winning_nums:
            if have_num == winning_num:
                matches += 1
        
    if matches == 0:
        return 0
    else:
        return 2**(matches-1)

if __name__ == "__main__":
    with open('4input.txt', 'r') as f:
        input_data = f.read()

#     input_data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    cards = load_cards(input_data)
    running_sum = 0
    for card_id, card_content in cards.items():
        running_sum += check_card_value(card_content)
    print(running_sum)