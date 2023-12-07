CARDS_P1 = {'high': [], '1 pair': [], '2 pair': [], '3 kind': [], 'full': [], '4 kind': [], '5 kind': []}
CARDS_P2 = {'high': [], '1 pair': [], '2 pair': [], '3 kind': [], 'full': [], '4 kind': [], '5 kind': []}
BID = {}
CARD_RANK_P1 = {'A':13, 'K':12, 'Q':11,'J': 10 , 'T':9,'9':8, '8':7,'7':6,'6':5,'5':4,'4':3,'3':2,'2':1}
CARD_RANK_P2 = {'A':13, 'K':12, 'Q':11,'J': 0 , 'T':9,'9':8, '8':7,'7':6,'6':5,'5':4,'4':3,'3':2,'2':1}

def get_val(cards):
    num_cards = len(set(cards))
    if num_cards == len(cards):
        return 'high'
    elif num_cards == 1:
        return '5 kind'
    elif num_cards == 2:
        for card in cards:
            if cards.count(card) == 3:
                return 'full'
            if cards.count(card) == 4:
                return '4 kind'

    elif num_cards == 3:
        for card in cards:
            if cards.count(card) == 3:
                return '3 kind'
        return '2 pair'

    else:
        return '1 pair'

def check_card(cards):
    joker_detect = cards.count('J')

    key = get_val(cards)

    CARDS_P1[key].append(card)

    if joker_detect == 0:
        CARDS_P2[key].append(cards)
        return

    house = {card: cards.count(card) for card in cards if card != 'J'}

    card_list = [card for card in house.keys()]
    card_list.sort(key = lambda x : house[x], reverse=True)

    if not card_list:
        key = '5 kind'
    else:
        new_cards = cards.replace('J', card_list[0])
        key = get_val(new_cards)

    CARDS_P2[key].append(cards)

output = [0, 0]

with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

    cards = []
    for line in lines:
        line = line.split()
        cards.append(line[0])
        BID[line[0]] = int(line[1])

    for card in cards:
        check_card(card)

    for idx_card, card in enumerate([CARDS_P1, CARDS_P2]):
        current_stand = 1
        if card == CARDS_P1:
            rank = CARD_RANK_P1
        else:
            rank = CARD_RANK_P2
        for house in card.keys():
            card[house].sort(key = lambda x: (rank[x[0]], rank[x[1]], rank[x[2]], rank[x[3]], rank[x[4]]))
            for idx, c in enumerate(card[house]):
                output[idx_card] += BID[c] * (idx + current_stand)

            current_stand += len(card[house])

    print('part 1:', output[0])
    print('part 2:', output[1])