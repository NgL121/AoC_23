CARDS = {'high': [], '1 pair': [], '2 pair': [], '3 kind': [], 'full': [], '4 kind': [], '5 kind': []}
RANK = {}
BID = {}
CARD_RANK = {'A':13, 'K':12, 'Q':11,'J':10, 'T':9,'9':8, '8':7,'7':6,'6':5,'5':4,'4':3,'3':2,'2':1}


def check_card(cards):
    num_cards = len(set(cards))
    if num_cards == len(cards):
        CARDS['high'].append(cards)
    elif num_cards == 1:
        CARDS['5 kind'].append(cards)
    elif num_cards == 2:
        for card in cards:
            if cards.count(card) == 3:
                CARDS['full'].append(cards)
                break
            if cards.count(card) == 4:
                CARDS['4 kind'].append(cards)
                break

    elif num_cards == 3:
        added = False
        for card in cards:
            if cards.count(card) == 3:
                CARDS['3 kind'].append(cards)
                added = True
                break
        if not added:
            CARDS['2 pair'].append(cards)

    else:
        CARDS['1 pair'].append(cards)

output = 0

with open('input.txt', 'r') as data:
    lines = [line.strip() for line in data.readlines()]

    cards = []
    for line in lines:
        line = line.split()
        cards.append(line[0])
        BID[line[0]] = int(line[1])

    for card in cards:
        check_card(card)

    current_stand = 1
    for house in CARDS.keys():
        CARDS[house].sort(key = lambda x: (CARD_RANK[x[0]], CARD_RANK[x[1]], CARD_RANK[x[2]], CARD_RANK[x[3]], CARD_RANK[x[4]]))
        for idx, card in enumerate(CARDS[house]):
            output += BID[card] * (idx + current_stand)

        current_stand += len(CARDS[house])

    print(RANK)
    print(BID)
    print(CARDS)
    print(output)