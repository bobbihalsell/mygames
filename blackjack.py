import random

cards = ["ACE", 2, 3, 4, 5, 6, 7, 8, 9, 10, "JACK", "QUEEN", "KING"]
instructions = '''\nAn ACE can be 1 or 11.
                  \rJACK, QUEEN, KING have value 10.
                  \r The aim is to get the sum of your cards as close to 21.
                  \rIf the sum of your cards is higher than 21 BUST and you lose.'''

def value_bj(cards):
    value = 0
    ace = False
    for i in range(len(cards)):
        if cards[i] in ["JACK", "QUEEN", "KING"]:
            value+=10
        elif cards[i] == 'ACE':
            value+=11
            ace = True
        else:
            value+=cards[i]
    if value > 21 and ace == True:
        value -= 10 
    if value > 21:
        return 0
    return value


        

def black_jack():
    print('\nYOU ARE PLAYING BLACK JACK')
    print(instructions)
    players_cards = []
    for _ in range(2):
        card = random.choice(cards)
        players_cards.append(card)
    comp_cards = []
    for _ in range(2):
        card = random.choice(cards)
        comp_cards.append(card)
    another = input(f'''\nYOUR CARDS: {players_cards}
                        \r COMPUTERS FIRST CARD: {comp_cards[0]}
                        \r Type 'Y' to get another card and 'N' to pass  ''').upper()
    if another == 'Y':
        pcard2 = random.choice(cards)
        players_cards.append(pcard2)
    if value_bj(comp_cards)<17:
        ccard2 = random.choice(cards)
        comp_cards.append(ccard2)
    players_score = value_bj(players_cards)
    comp_score = value_bj(comp_cards)
    print(f'''\nYOUR FINAL HAND: {players_cards} SCORE: {players_score}
              \rCOMPUTERS FINAL HAND: {comp_cards} SCORE: {comp_score}''')
    if players_score > comp_score:
        print('YOU WIN')
    elif players_score == comp_score:
        print('YOU TIE')
    else:
        print('YOU LOSE')


    
    
